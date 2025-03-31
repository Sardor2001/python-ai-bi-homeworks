import numpy as np

# Create two 3x3 random matrices
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)

# Compute the dot product
result_matrix = np.dot(matrix_A, matrix_B)

print("Matrix A:")
print(matrix_A)
print("\nMatrix B:")
print(matrix_B)
print("\nDot Product Result:")
print(result_matrix)