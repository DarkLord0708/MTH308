def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    """
    Standard Regula Falsi (False Position) method to find root of f(x) = 0.

    Parameters:
    f         -- Function
    a, b      -- Initial interval [a, b] with f(a) * f(b) < 0
    tol       -- Tolerance
    max_iter  -- Maximum iterations

    Returns:
    Approximated root or None
    """
    if f(a) * f(b) >= 0:
        print("Regula Falsi fails: f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    for i in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        fc = f(c)
        print(f"{i+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {fc:.6e}")

        if abs(fc) < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Max iterations reached.")
    return c

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = regula_falsi(f, 1, 2)
    print("\nApproximated root:", root)
