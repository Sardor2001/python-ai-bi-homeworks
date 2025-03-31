import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


# Generate x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Compute the function f(x, y) = cos(x^2 + y^2)
z = np.cos(x**2 + y**2)

# Create the 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add a colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot of $f(x, y) = \\cos(x^2 + y^2)$')

# Show the plot
plt.show()