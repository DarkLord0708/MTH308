import numpy as np
from tabulate import tabulate
 
# Coefficients of the system
A = np.array([[5, -2, 3], 
              [-3, 9, 1], 
              [2, -1, -7]], dtype=float)
 
# Right-hand side
b = np.array([-1, 2, 3], dtype=float)
 
# Initial guess (zero vector)
x_jacobi = np.zeros(len(b))
x_gauss = np.zeros(len(b))
 
# Maximum iterations
max_iter = 8
 
# Jacobi Method
def jacobi(A, b, x0, max_iter):
    n = len(b)
    x_new = np.copy(x0)
    results = [['Iteration', 'x1', 'x2', 'xn']]
 
    for k in range(max_iter):
        x_old = np.copy(x_new)
        for i in range(n):
            sigma = sum(A[i, j] * x_old[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i, i]
        results.append([k+1, *x_new])
    
    return results
 
# Gauss-Seidel Method
def gauss_seidel(A, b, x0, max_iter):
    n = len(b)
    x_new = np.copy(x0)
    results = [['Iteration', 'x1', 'x2', 'xn']]
 
    for k in range(max_iter):
        for i in range(n):
            sigma = sum(A[i, j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i, i]
        results.append([k+1, *x_new])
    
    return results
 
# Solve using both methods
jacobi_results = jacobi(A, b, x_jacobi, max_iter)
gauss_seidel_results = gauss_seidel(A, b, x_gauss, max_iter)
 
# Print results using tabulate
print("Jacobi Method Results:")
print(tabulate(jacobi_results[1:], headers=jacobi_results[0], tablefmt="grid"))
 
print("\nGauss-Seidel Method Results:")
print(tabulate(gauss_seidel_results[1:], headers=gauss_seidel_results[0], tablefmt="grid"))