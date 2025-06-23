import numpy as np
from scipy.integrate import newton_cotes
import math

def composite_newton_cotes(f, a, b, n_intervals, degree):
    """
    Composite Newton-Cotes Integration.
    
    Parameters:
    f : function to integrate
    a, b : interval [a, b]
    n_intervals : number of subintervals (must be divisible by degree)
    degree : degree of the Newton-Cotes rule (1=trapezoid, 2=Simpson, etc.)
    """
    if n_intervals % degree != 0:
        raise ValueError("n_intervals must be divisible by the degree.")
    
    h = (b - a) / n_intervals
    total_integral = 0

    for i in range(0, n_intervals, degree):
        # Local interval
        x0 = a + i * h
        x = [x0 + j * h for j in range(degree + 1)]
        y = [f(xi) for xi in x]

        weights, _ = newton_cotes(degree, equal=1)
        local_integral = h * np.dot(weights, y)
        total_integral += local_integral

    return total_integral


f = lambda x: math.exp(-x**2)
a = 0
b = 1
n = 6

print("Degree 1 (Trapezoidal):", composite_newton_cotes(f, a, b,n, 1))
print("Degree 2 (Simpson's 1/3):", composite_newton_cotes(f, a, b,n, 2))
print("Degree 3 (Simpson's 3/8):", composite_newton_cotes(f, a, b,n, 3))