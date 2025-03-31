import numpy as np

# Coefficient Matrix
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

# Right-hand side vector
B = np.array([7, 4, 5])

# Solving the system of linear equations
solution = np.linalg.solve(A, B)

print(solution)