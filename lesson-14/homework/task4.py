import numpy as np

# Coefficient matrix
A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

# Right-hand side vector
B = np.array([12, -5, 15])

# Solving the system of equations
currents = np.linalg.solve(A, B)
print(currents)