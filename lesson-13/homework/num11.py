import numpy as np

# Create a 3x3 random matrix
matrix = np.random.rand(3, 3)

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

print("Matrix:")
print(matrix)
print("\nDeterminant:")
print(determinant)