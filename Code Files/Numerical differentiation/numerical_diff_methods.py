def richardson_extrapolation(f, x, h):
    """
    Compute the derivative using Richardson extrapolation.

    Parameters:
    f  -- the function
    x  -- the point at which derivative is evaluated
    h  -- step size

    Returns:
    Approximate value of f'(x)
    """
    D1 = (f(x + h) - f(x - h)) / (2 * h)
    D2 = (f(x + h/2) - f(x - h/2)) / (h)
    return D2 + (D2 - D1) / 3  # Extrapolated better estimate

def euler_method(f, x0, y0, h, n):
    """
    Euler's Method for solving ODEs.

    Parameters:
    f  -- dy/dx = f(x, y)
    x0 -- initial x
    y0 -- initial y
    h  -- step size
    n  -- number of steps

    Returns:
    List of (x, y) values
    """
    x_vals = [x0]
    y_vals = [y0]
    
    for i in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)

    return list(zip(x_vals, y_vals))

def runge_kutta_2(f, x0, y0, h, n):
    """
    Runge-Kutta 2nd Order Method for solving ODEs.

    Parameters:
    f  -- dy/dx = f(x, y)
    x0 -- initial x
    y0 -- initial y
    h  -- step size
    n  -- number of steps

    Returns:
    List of (x, y) values
    """
    x_vals = [x0]
    y_vals = [y0]

    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        y0 += 0.5 * (k1 + k2)
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)

    return list(zip(x_vals, y_vals))

import math

# Example function for testing
f = lambda x: math.sin(x)
df = lambda x: math.cos(x)

# Richardson
print("Richardson Derivative at pi/4:", richardson_extrapolation(f, math.pi/4, 0.1))
print("Actual Derivative:", df(math.pi/4))

# Euler and RK2
f_ode = lambda x, y: x + y  # dy/dx = x + y
print("\nEuler:", euler_method(f_ode, 0, 1, 0.1, 5))
print("\nRK2:", runge_kutta_2(f_ode, 0, 1, 0.1, 5))
