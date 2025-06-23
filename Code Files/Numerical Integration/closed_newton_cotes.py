import math
import numpy as np

import numpy as np

def newton_cotes(f, a, b, n):
    """
    Newton-Cotes integration of degree n over [a, b] using closed formulas.

    Parameters:
    f : function
        Function to integrate
    a, b : float
        Integration bounds
    n : int
        Degree of the Newton-Cotes formula (1 to 4 supported)

    Returns:
    float : Approximate integral of f over [a, b]
    """
    if n < 1 or n > 4:
        raise ValueError("This implementation supports n = 1 to 4 (degree of polynomial)")

    # Closed Newton-Cotes weights
    weights_dict = {
        1: [1, 1],                                # Trapezoidal Rule
        2: [1, 4, 1],                             # Simpson's 1/3 Rule
        3: [1, 3, 3, 1],                          # Simpson's 3/8 Rule
        4: [7, 32, 12, 32, 7],                    # Boole’s Rule (closed Newton-Cotes of degree 4)
    }

    weights = np.array(weights_dict[n])
    nodes = len(weights)
    h = (b - a) / (nodes - 1)

    x = np.linspace(a, b, nodes)
    y = np.array([f(xi) for xi in x])

    integral = h * np.dot(weights, y) / np.sum(weights_dict[n])  # Normalize weights
    return integral


f = lambda x: math.exp(-x**2)
a = 0
b = 1

print("Degree 1 (Trapezoidal):", newton_cotes(f, a, b, 1))
print("Degree 2 (Simpson's 1/3):", newton_cotes(f, a, b, 2))
print("Degree 3 (Simpson's 3/8):", newton_cotes(f, a, b, 3))