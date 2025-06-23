import sympy as sp
import numpy as np

def compute_jacobian(f_exprs, variables):
    """
    Computes the symbolic Jacobian matrix for a system of functions.
    
    Parameters:
      f_exprs   : A list of Sympy expressions (each represents one equation).
      variables : A list of Sympy symbols with respect to which the derivatives are computed.
      
    Returns:
      A Sympy Matrix representing the Jacobian.
    """
    jacobian_matrix = sp.Matrix([[sp.diff(f, var) for var in variables] for f in f_exprs])
    return jacobian_matrix

def jacobian_numeric(f_exprs, variables):
    """
    Creates a numerical function to compute the Jacobian matrix of a system of equations.
    
    Parameters:
      f_exprs   : A list of Sympy expressions (the system of equations).
      variables : A list of Sympy symbols (the variables).
      
    Returns:
      A function that, given numerical values for the variables, returns the Jacobian as a NumPy array.
    """
    J_sym = compute_jacobian(f_exprs, variables)
    J_func = sp.lambdify(variables, J_sym, 'numpy')
    return J_func

def newton_raphson_system(F_func, J_func, X0, tol=1e-6, max_iter=100):
    """
    Solves the system F(X) = 0 using the Newton–Raphson method.
    
    Parameters:
      F_func  : A function that evaluates the system of equations numerically.
      J_func  : A function that evaluates the Jacobian matrix numerically.
      X0      : Initial guess (as a NumPy array).
      tol     : Tolerance for convergence.
      max_iter: Maximum number of iterations.
    
    Returns:
      The approximated solution vector.
    """
    X = X0
    for i in range(max_iter):
        # Evaluate the function and Jacobian at the current guess.
        F_val = np.array(F_func(*X), dtype=np.float64).flatten()
        J_val = np.array(J_func(*X), dtype=np.float64)
        
        # Solve for the update: J * delta = -F_val.
        delta = np.linalg.solve(J_val, -F_val)
        
        # Update the guess.
        X_new = X + delta
        
        # Check for convergence.
        if np.linalg.norm(delta, ord=2) < tol:
            print(f"Converged in {i+1} iterations.")
            return X_new
        
        X = X_new
    
    print("Did not converge within the maximum number of iterations.")
    return X

if __name__ == "__main__":
    # Define symbolic variables.
    x, y, z = sp.symbols('x y z')
    
    # Define the system of equations:
    # f1(x,y) = x^2 + y^2 - 4 and f2(x,y) = x - y.
    # f1 = x*y + x**2 - y**3 -1
    # f2 = x + 2*y -x*(y**2) - 2

    # f1 = sp.sin(x*y)+ sp.exp(y) - 7.10964
    # f2 = (x+y)**2 + sp.cos(x*(y**2)) - 24.1561

    # f1 = sp.exp(x*y) + x**2 + y - 1.2
    # f2 = x**2 + y**2 + x - 0.55

    f1 = x + y+ z -0.3
    f2 = x**2 + y**2 + z**2 - 0.03
    f3 = x**3 + y**3 + z**3 - 0.003


    f_exprs = [f1, f2, f3]

    variables = [x, y, z]
    
    # Create a numerical function for the system of equations.
    F_func = sp.lambdify(variables, f_exprs, 'numpy')
    
    # Create the numerical Jacobian function.
    J_func = jacobian_numeric(f_exprs, variables)
    
    # Set an initial guess for (x, y).
    X0 = np.array([0.5, 1.5, 3.5])
    
    # Solve the system using Newton–Raphson.
    solution = newton_raphson_system(F_func, J_func, X0)
    print("Solution:", solution)
