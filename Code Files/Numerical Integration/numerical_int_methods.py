import numpy as np
import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i * h)
    return (h / 2) * result


def simpsons_one_third_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires even n")
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        result += 4 * f(x) if i % 2 == 1 else 2 * f(x)
    
    return (h / 3) * result


def simpsons_three_eighth_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires n to be a multiple of 3")
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        result += 3 * f(x) if i % 3 != 0 else 2 * f(x)
    
    return (3 * h / 8) * result


def romberg_integration(f, a, b, max_level=4):
    R = np.zeros((max_level, max_level), dtype=float)
    h = b - a
    R[0, 0] = h / 2 * (f(a) + f(b))

    for i in range(1, max_level):
        h /= 2
        sum_f = sum(f(a + (2 * k - 1) * h) for k in range(1, 2**(i-1) + 1))
        R[i, 0] = 0.5 * R[i-1, 0] + h * sum_f

        for j in range(1, i+1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    return R[max_level - 1, max_level - 1]



f = lambda x: math.exp(-x**2)  # Example function
a = 0
b = 1
n = 6  # Choose according to method requirements

print("Trapezoidal:", trapezoidal_rule(f, a, b, n))
print("Simpson's 1/3:", simpsons_one_third_rule(f, a, b, n if n % 2 == 0 else n+1))
print("Simpson's 3/8:", simpsons_three_eighth_rule(f, a, b, 6))
print("Romberg Integration:", romberg_integration(f, a, b, 4))
