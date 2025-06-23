def lagrange_interpolation(x_vals, y_vals, x):
    """
    Computes the interpolated value at x using Lagrange interpolation.

    Parameters:
    x_vals -- list of known x-values
    y_vals -- list of corresponding y-values
    x      -- value at which interpolation is desired

    Returns:
    interpolated value at x
    """
    n = len(x_vals)
    result = 0.0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term
    return result


def neville_interpolation(x_vals, y_vals, x):
    """
    Computes the interpolated value at x using Neville's method.

    Parameters:
    x_vals -- list of known x-values
    y_vals -- list of corresponding y-values
    x      -- value at which interpolation is desired

    Returns:
    interpolated value at x
    """
    n = len(x_vals)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        Q[i][0] = y_vals[i]

    for j in range(1, n):
        for i in range(n - j):
            Q[i][j] = ((x - x_vals[i + j]) * Q[i][j - 1] +
                       (x_vals[i] - x) * Q[i + 1][j - 1]) / (x_vals[i] - x_vals[i + j])

    return Q[0][n - 1]


def newton_divided_diff(x_vals, y_vals):
    """
    Constructs the divided difference table and returns coefficients.

    Parameters:
    x_vals -- list of known x-values
    y_vals -- list of corresponding y-values

    Returns:
    list of divided difference coefficients (Newton polynomial coefficients)
    """
    n = len(x_vals)
    coef = y_vals.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x_vals[i] - x_vals[i - j])
    return coef


def newton_interpolation(x_vals, coef, x):
    """
    Evaluate Newton polynomial using divided difference coefficients.

    Parameters:
    x_vals -- list of known x-values
    coef   -- divided difference coefficients
    x      -- value to interpolate

    Returns:
    interpolated value at x
    """
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_vals[i]) + coef[i]
    return result


if __name__ == "__main__":
    x_points = [5, 6, 9, 11]
    y_points = [12, 13, 14, 16]
    x_to_interp = 10

    print("Lagrange:", lagrange_interpolation(x_points, y_points, x_to_interp))
    print("Neville:", neville_interpolation(x_points, y_points, x_to_interp))

    coef = newton_divided_diff(x_points, y_points)
    print("Newton (Divided Difference):", newton_interpolation(x_points, coef, x_to_interp))
