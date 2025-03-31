import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random points from a uniform distribution between 0 and 10
np.random.seed(42)  # For reproducibility
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', marker='o', edgecolor='black', alpha=0.7)

# Add title and axis labels
plt.title('Scatter Plot of 100 Random Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()