def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Finds a root of f(x) = 0 using the Secant method.

    Parameters:
    f         -- Function to find the root of
    x0, x1    -- Initial guesses
    tol       -- Tolerance for convergence
    max_iter  -- Maximum number of iterations

    Returns:
    Approximate root or None
    """
    print("Iter\t x0\t\t x1\t\t x2\t\t f(x2)")
    for i in range(max_iter):
        if abs(x1 - x0) < 1e-14:
            print("Denominator too small. Method fails.")
            return None

        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        print(f"{i+1}\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {fx2:.6e}")

        if abs(fx2) < tol:
            return x2

        x0, x1 = x1, x2

    print("Max iterations reached.")
    return x2

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = secant(f, 1, 2)
    print("\nApproximated root:", root)
