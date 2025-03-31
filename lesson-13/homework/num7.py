import numpy as np
from sklearn.preprocessing import MinMaxScaler


def normalize_matrix(matrix):
    """Safely normalizes a matrix using MinMaxScaler."""
    if np.max(matrix) == np.min(matrix):
        print("All elements in the matrix are the same. Returning a zero matrix.")
        return np.zeros_like(matrix)  # Avoid division by zero

    scaler = MinMaxScaler()
    return scaler.fit_transform(matrix)


# Generate a random 5x5 matrix
matrix = np.random.rand(5, 5)
normalized_matrix = normalize_matrix(matrix)

print("Original matrix:\n", matrix)
print("Normalized matrix:\n", normalized_matrix)
