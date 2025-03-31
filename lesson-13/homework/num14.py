import numpy as np


def solve_linear_system(A, b):
    """Solves Ax = b safely, even if A is singular."""
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Check if A is singular
    if np.linalg.det(A) == 0:
        print("Matrix A is singular. Finding least-squares solution...")
        x = np.linalg.pinv(A) @ b  # Use pseudo-inverse for a best-fit solution
    else:
        x = np.linalg.solve(A, b)  # Direct solution

    return x


# Example usage
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

x = solve_linear_system(A, b)
print("Solution:", x)
