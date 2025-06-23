def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of f(x) = 0 using the bisection method.
    
    Parameters:
    f         -- Function for which root is sought
    a, b      -- Interval endpoints such that f(a) * f(b) < 0
    tol       -- Tolerance for stopping criterion
    max_iter  -- Maximum number of iterations
    
    Returns:
    Approximated root or None if not found.
    """
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {fc:.6e}")
        
        if abs(fc) < tol or abs(b - a) / 2 < tol:
            return c
        elif f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Max iterations reached.")
    return (a + b) / 2

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = bisection(f, 1, 2)
    print("\nApproximated root:", root)
