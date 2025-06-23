import sympy as sp

def partial_derivatives_and_values(expr, variables, values):
    """
    Computes the partial derivatives of a sympy expression with respect to given variables,
    and evaluates their numerical values at the given point.

    Parameters:
      expr      : A sympy expression representing the function.
      variables : A list of sympy symbols with respect to which the derivatives are computed.
      values    : A dictionary mapping each variable to its numerical value.
      
    Returns:
      A dictionary mapping each variable to a tuple: 
      (symbolic derivative, numerical value).
    """
    derivs = {}
    for var in variables:
        # Compute symbolic derivative
        derivative = sp.diff(expr, var)
        # Evaluate the derivative numerically at the given point
        numerical_value = float(derivative.evalf(subs=values))
        derivs[var] = (derivative, numerical_value)
    return derivs

if __name__ == '__main__':
    # Define symbolic variables
    x, y = sp.symbols('x y')

    # Define the function f(x, y) = x^2 + y^2 - 4
    f = x**2 + y**2 - 4

    # Define the point at which to evaluate the derivatives (e.g., x = 1, y = 1)
    values = {x: 1, y: 1}

    # Compute the partial derivatives and their numerical values
    derivs = partial_derivatives_and_values(f, [x, y], values)

    print("Partial derivatives and their numerical values for f(x, y) = x^2 + y^2 - 4:")
    for var, (deriv, num_val) in derivs.items():
        print(f"∂f/∂{var} = {deriv}  and its numerical value at {values} is {num_val}")