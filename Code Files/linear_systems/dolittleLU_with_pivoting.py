import numpy as np

def doolittle_lu_factorization_with_pivoting(A):
    """
    Performs LU decomposition of a square matrix A using Doolittle's method
    with partial pivoting. That is, we find P, L, U such that P*A = L*U.
    However, here we directly swap rows in A and L (instead of explicitly
    creating a permutation matrix P).

    Parameters:
    A (2D list or np.ndarray): The square matrix to decompose.

    Returns:
    L, U (np.ndarray, np.ndarray): Matrices L and U such that (some row-swapped version of) A = L * U.
    """
    A = np.array(A, dtype=float)  # Ensure a float array
    n = A.shape[0]

    # Initialize L and U as zero matrices
    L = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)

    for k in range(n):
        # --- Partial Pivoting: Find the pivot row ---
        # 1) Find the index of the largest absolute value in column k from row k downward
        pivot_row = k + np.argmax(np.abs(A[k:, k]))

        # 2) If pivot_row != k, swap row k with pivot_row in A and the relevant part of L
        if pivot_row != k:
            # Swap rows in A
            A[[k, pivot_row], :] = A[[pivot_row, k], :]

            # Swap the rows in L only up to column k (already computed columns)
            # because columns >= k are not yet finalized in L
            L[[k, pivot_row], :k] = L[[pivot_row, k], :k]

        # 3) Set the diagonal of L to 1
        L[k, k] = 1.0

        # --- Compute U[k, k] ---
        t = 0.0
        for p in range(k):
            t += L[k, p] * U[p, k]
        U[k, k] = A[k, k] - t

        # --- Compute the remaining elements of U in row k ---
        for j in range(k + 1, n):
            t = 0.0
            for p in range(k):
                t += L[k, p] * U[p, j]
            U[k, j] = A[k, j] - t

        # --- Compute the remaining elements of L in column k ---
        for i in range(k + 1, n):
            t = 0.0
            for p in range(k):
                t += L[i, p] * U[p, k]
            L[i, k] = (A[i, k] - t) / U[k, k]

    return L, U

# ------------------ Example Usage ------------------
if __name__ == "__main__":
    # A = [
    #     [1, 2, 1, 3],
    #     [2, 4, 1, 5],
    #     [3, 2, 1, 4],
    #     [4, 1, 1, 3]
    # ]
    A = [
        [2,0,1],
        [4,3,2],
        [6,0,5]
    ]

    L, U = doolittle_lu_factorization_with_pivoting(A)

    print("Original Matrix A (after potential row swaps internally):")
    print(np.array(A))
    print("\nL (Unit Lower Triangular):")
    print(L)
    print("\nU (Upper Triangular):")
    print(U)

    # Check that L @ U is equal to the row-swapped A
    # Because we do not explicitly track a permutation matrix P, A has been
    # partially pivoted in-place. Let's call that A' (A prime).
    A_prime = np.array(A, dtype=float)
    A_reconstructed = L @ U
    print("\nReconstructed A' from L*U (should match the pivoted A):")
    print(A_reconstructed)

    print("\nDifference (A' - L*U):")
    print(A_prime - A_reconstructed)
