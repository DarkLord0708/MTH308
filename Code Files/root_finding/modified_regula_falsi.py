def regula_falsi_modified(f, a, b, tol=1e-6, max_iter=100):
    """
    Modified Regula Falsi (Illinois method) to improve convergence.

    Returns:
    Approximated root or None
    """
    if f(a) * f(b) >= 0:
        print("Modified Regula Falsi fails: f(a) and f(b) must have opposite signs.")
        return None

    fa, fb = f(a), f(b)
    count_a, count_b = 0, 0

    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    for i in range(max_iter):
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        print(f"{i+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {fc:.6e}")

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b, fb = c, fc
            count_b = 0
            count_a += 1
            if count_a >= 2:
                fa /= 2
        else:
            a, fa = c, fc
            count_a = 0
            count_b += 1
            if count_b >= 2:
                fb /= 2

    print("Max iterations reached.")
    return c

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = regula_falsi_modified(f, 1, 2)
    print("\nApproximated root:", root)
