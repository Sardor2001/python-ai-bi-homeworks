import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(0, 2 * np.pi, 500)

# Calculate sine and cosine values
sin_values = np.sin(x_values)
cos_values = np.cos(x_values)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot sine function
plt.plot(x_values, sin_values, label=r"sin(x)", color='blue', linestyle='-', marker='o', markevery=50)

# Plot cosine function
plt.plot(x_values, cos_values, label=r"cos(x)", color='red', linestyle='--', marker='s', markevery=50)

# Add labels, title, and legend
plt.title("Sine and Cosine Functions", fontsize=14)
plt.xlabel("x (radians)", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add horizontal line at y=0
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Add vertical line at x=0
plt.grid(alpha=0.5)
plt.legend(fontsize=12)

# Show the plot
plt.show()
