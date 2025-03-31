import numpy as np

matrix_A = np.random.rand(5, 3)
matrix_B = np.random.rand(3, 2)

result_Matrix = np.dot(matrix_A, matrix_B)

print("Matrix A (5x3):")
print(matrix_A)
print("\nMatrix B (3x2):")
print(matrix_B)
print("\nResulting Matrix (5x2):")
print(result_Matrix)