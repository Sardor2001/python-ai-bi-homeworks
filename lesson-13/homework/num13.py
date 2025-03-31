import numpy as np

# Create a 3x3 random matrix
matrix = np.random.rand(3, 3)

# Create a 3-element column vector
vector = np.random.rand(3, 1)  # Reshape to a column vector

# Compute the matrix-vector product
result = matrix @ vector  # Alternatively, use np.dot(matrix, vector)

print("3x3 Random Matrix:")
print(matrix)
print("\n3-Element Column Vector:")
print(vector)
print("\nMatrix-Vector Product:")
print(result)