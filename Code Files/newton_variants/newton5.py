import sympy as sp
import numpy as np
from tabulate import tabulate

def compute_jacobian(f_exprs, variables):
    """
    Computes the symbolic Jacobian matrix for a system of equations.
    
    Parameters:
      f_exprs   : List of sympy expressions (each represents one equation).
      variables : List of sympy symbols with respect to which derivatives are computed.
      
    Returns:
      A sympy Matrix representing the Jacobian.
    """
    jacobian_matrix = sp.Matrix([[sp.diff(f, var) for var in variables] for f in f_exprs])
    return jacobian_matrix

def system_function_numeric(f_exprs, variables):
    """
    Converts a list of symbolic expressions into a numerical function.
    
    Parameters:
      f_exprs   : List of sympy expressions (system of equations).
      variables : List of sympy symbols.
      
    Returns:
      A function that takes numerical inputs for the variables and returns the system evaluated.
    """
    F_func = sp.lambdify(variables, f_exprs, 'numpy')
    return F_func

def jacobian_numeric(f_exprs, variables):
    """
    Converts the symbolic Jacobian into a numerical function.
    
    Parameters:
      f_exprs   : List of sympy expressions (system of equations).
      variables : List of sympy symbols.
      
    Returns:
      A function that, given numerical values, returns the Jacobian as a NumPy array.
    """
    J_sym = compute_jacobian(f_exprs, variables)
    J_func = sp.lambdify(variables, J_sym, 'numpy')
    return J_func

def newton_raphson(f_exprs, variables, initial_guess, tol=1e-6, max_iter=100):
    """
    Solves the system of equations F(X) = 0 using the Newton–Raphson method.
    
    Parameters:
      f_exprs       : List of sympy expressions representing the system of equations.
      variables     : List of sympy symbols.
      initial_guess : List or array of initial guess values for the variables.
      tol           : Tolerance for convergence.
      max_iter      : Maximum number of iterations.
      
    Returns:
      The approximated solution as a NumPy array.
    """
    # Convert symbolic system and Jacobian to numerical functions.
    F_func = system_function_numeric(f_exprs, variables)
    J_func = jacobian_numeric(f_exprs, variables)
    
    X = np.array(initial_guess, dtype=float)
    
    # List to hold iteration data for tabulation
    table_data = []
    f = open("solution.txt","w+")
    for i in range(max_iter):
        # Record the current iteration data
        table_data.append([i, X[0], X[1], X[2]])
        
        # Evaluate the function and Jacobian at the current guess.
        F_val = np.array(F_func(*X), dtype=float)
        J_val = np.array(J_func(*X), dtype=float)
        
        # Solve for the update delta such that J * delta = -F_val
        delta = np.linalg.solve(J_val, -F_val)
        
        # Update the guess
        X_new = X + delta
        
        # Check convergence using the Euclidean norm of delta.
        if np.linalg.norm(delta, ord=2) < tol:
            table_data.append([i+1, X_new[0], X_new[1], X_new[2]])
            print(f"Converged in {i+1} iterations.")
            table = tabulate(table_data, headers=["Iteration", "x", "y", "z"], tablefmt="grid")
            f.write(table)
            f.close()
            print(table)
            return X_new
        
        X = X_new
    
    print("Did not converge within the maximum number of iterations.")
    table = tabulate(table_data, headers=["Iteration", "x", "y", "z"], tablefmt="grid")
    f.write(table)
    f.close()
    print(table)
    return X

if __name__ == '__main__':
    # Define symbolic variables
    x, y, z = sp.symbols('x y z')

    # Define the system of nonlinear equations:
    f1 = x + y + z - 0.3
    f2 = x**2 + y**2 + z**2 - 0.03
    f3 = x**3 + y**3 + z**3 - 0.003

    f_exprs = [f1, f2, f3]
    variables = [x, y, z]

    # Initial guess for the solution
    initial_guess = [0.5, 1.5, 3.5]

    # Solve the system using the Newton-Raphson method
    solution = newton_raphson(f_exprs, variables, initial_guess)
    print("Solution:", solution)
