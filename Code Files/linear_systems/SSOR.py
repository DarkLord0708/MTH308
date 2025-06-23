import numpy as np
from tabulate import tabulate

def ssor(A, b, x0=None, omega=1.25, tol=1e-6, max_iter=25):
    """
    Solves Ax = b using the SSOR (Symmetric Successive Over-Relaxation) method.

    Parameters:
    A        -- Coefficient matrix (n x n)
    b        -- Right-hand side vector (n)
    x0       -- Initial guess (default: zero vector)
    omega    -- Relaxation factor (0 < omega < 2)
    tol      -- Convergence tolerance
    max_iter -- Maximum number of iterations

    Returns:
    x        -- Solution vector
    """
    n = len(b)
    x = x0 if x0 is not None else np.zeros(n)
    results = [['Iteration'] + [f'x{i+1}' for i in range(n)] + ['Error']]

    for itr in range(1, max_iter + 1):
        x_old = x.copy()

        # Forward SOR sweep
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma)

        # Backward SOR sweep
        for i in reversed(range(n)):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma)

        error = np.linalg.norm(x - x_old, ord=2)
        results.append([itr] + list(x.copy()) + [f"{error:.2e}"])

        if error < tol:
            print("Converged.")
            break

    return results

if __name__ == "__main__":
    A = np.array([
        [5, -2, 3],
        [-3, 9, 1],
        [2, -1, -7]
    ], dtype=float)

    b = np.array([-1, 2, 3], dtype=float)
    x0 = np.zeros(len(b))
    omega = 1.25

    results = ssor(A, b, x0, omega=omega, max_iter=10)
    print(f"\nSSOR Method Results (ω = {omega}):")
    print(tabulate(results[1:], headers=results[0], tablefmt="grid"))
