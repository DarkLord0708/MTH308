import sys
import numpy as np

def compute_machine_epsilon():
    """
    Computes the machine epsilon for the floating-point arithmetic used in Python.
    Machine epsilon is the smallest number such that 1.0 + epsilon > 1.0.
    
    Returns:
    - epsilon (float): The machine epsilon.
    """
    epsilon = 1.0
    while 1.0 + epsilon > 1.0:
        epsilon /= 2  # Halve epsilon until it no longer satisfies the condition
    return epsilon * 2  # Multiply by 2 to get the last significant value

if __name__ == "__main__":
    # Compute Python's floating-point epsilon
    python_epsilon = compute_machine_epsilon()
    print(f"Python's computed machine epsilon: {python_epsilon}")

    # Check the actual precision from NumPy (IEEE 754 double precision)
    numpy_epsilon = np.finfo(float).eps
    print(f"Machine epsilon from NumPy: {numpy_epsilon}")

    # Show the precision reported by the system (sys.float_info.epsilon)
    system_epsilon = sys.float_info.epsilon
    print(f"System-reported machine epsilon: {system_epsilon}")
