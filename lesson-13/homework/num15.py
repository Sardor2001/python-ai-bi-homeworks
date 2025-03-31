import numpy as np

# Define a 5x5 matrix
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Compute row-wise sums
row_sums = np.sum(matrix, axis=1)

# Compute column-wise sums
col_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("\nRow-wise Sums:")
print(row_sums)
print("\nColumn-wise Sums:")
print(col_sums)