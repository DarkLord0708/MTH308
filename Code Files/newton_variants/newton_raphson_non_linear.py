import numpy as np

def f(X):
    """
    Defines the system of nonlinear equations.
    For this example:
      f1(x, y) = x^2 + y^2 - 4
      f2(x, y) = x - y
    """
    x, y = X[0], X[1]
    return np.array([x*y + x**2 - y**3 - 1, x + 2*y - x*(y**2) - 2])





def jacobian(X):
    """
    Computes the Jacobian matrix of the system.
    The Jacobian J is defined as:
      J = [df1/dx  df1/dy]
          [df2/dx  df2/dy]
    For our example:
      df1/dx = 2x,   df1/dy = 2y
      df2/dx = 1,    df2/dy = -1
    """
    x, y = X[0], X[1]
    return np.array([[y + 2*x, x - 3*(y**2)],
                     [1 - y**2 ,   2 - 2*x*y]])

def newton_raphson_system(F, J, X0, tol=1e-6, max_iter=100):
    """
    Solves the system F(X) = 0 using the Newton–Raphson method.
    
    Parameters:
      F       : Function that returns a numpy array of the system.
      J       : Function that returns the Jacobian matrix.
      X0      : Initial guess (numpy array).
      tol     : Tolerance for convergence.
      max_iter: Maximum number of iterations.
    
    Returns:
      The approximated solution vector.
    """
    X = X0
    for i in range(max_iter):
        F_val = F(X)
        J_val = J(X)
        
        # Solve for the update delta such that J * delta = F_val.
        delta = np.linalg.solve(J_val, F_val)
        
        # Update the guess.
        X_new = X - delta
        
        # Check for convergence (using the Euclidean norm).
        if np.linalg.norm(delta, ord=2) < tol:
            print(f"Converged in {i+1} iterations.")
            return X_new
        
        X = X_new
    
    print("Did not converge within the maximum number of iterations.")
    return X

if __name__ == "__main__":
    # Initial guess for x and y
    X0 = np.array([0.5, 1.5])
    
    solution = newton_raphson_system(f, jacobian, X0)
    print("Solution:", solution)


