import numpy as np

# Create matrix A (3x4)
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# Create matrix B (4x3)
B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

# Compute the matrix product A * B
result = np.dot(A, B)  # Alternatively, you can use: result = A @ B

print("Matrix A (3x4):")
print(A)
print("\nMatrix B (4x3):")
print(B)
print("\nMatrix Product A * B (3x3):")
print(result)