import numpy as np

def lu_decomposition(A):
    """Performs LU decomposition using Doolittle’s method (L has 1s on the diagonal)."""
    n = len(A)
    L = np.eye(n)  # Initialize L as identity matrix
    U = np.zeros((n, n))  # Initialize U as zero matrix

    for i in range(n):
        # Compute U
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_
            print(U)

        # Compute L
        for k in range(i + 1, n):
            sum_ = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

# Define matrices for problems
matrices = {
    "Problem 1": np.array([[2, 3, 1], [4, 5, 2], [6, 7, 3]], dtype=float),
    "Problem 2": np.array([[1, 2, 1, 3], [2, 4, 1, 5], [3, 2, 1, 4], [4, 1, 1, 3]], dtype=float),
    "Problem 3": np.array([[5, 0, 0], [0, 7, 0], [0, 0, 9]], dtype=float),
    "Problem 4": np.array([[2, 0, 1], [4, 3, 2], [6, 0, 5]], dtype=float)
}

# Solve and print LU decomposition for each problem
for problem, A in matrices.items():
    if(problem=="Problem 1"):
        print(f"\n{problem}:")
        L, U = lu_decomposition(A)
        print("L matrix:\n", L)
        print("U matrix:\n", U)
