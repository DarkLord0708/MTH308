def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding root of f(x) = 0.

    Parameters:
    f        -- Function for which the root is sought
    df       -- Derivative of f(x)
    x0       -- Initial guess
    tol      -- Tolerance for convergence
    max_iter -- Maximum number of iterations

    Returns:
    The approximated root or None if convergence fails.
    """
    print("Iter\t x_n\t\t f(x_n)\t\t Error")
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)

        if abs(dfx) < 1e-12:
            print("Derivative too small. Division by near-zero.")
            return None

        x1 = x0 - fx / dfx
        error = abs(x1 - x0)

        print(f"{i}\t {x1:.6f}\t {f(x1):.6e}\t {error:.2e}")

        if error < tol:
            print("Converged.")
            return x1

        x0 = x1

    print("Did not converge within maximum iterations.")
    return None


# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    root = newton_raphson(f, df, x0=1.5)
    print("\nRoot found:", root)
