import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Generate x values
x = np.linspace(-2, 2, 400)
x_positive = np.linspace(0, 2, 400)

# Top-left: f(x) = x^3
axs[0, 0].plot(x, x ** 3, color='blue')
axs[0, 0].set_title('$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 0].grid(True)

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x, np.sin(x), color='green')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')
axs[0, 1].grid(True)

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x, np.exp(x), color='red')
axs[1, 0].set_title('$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')
axs[1, 0].grid(True)

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x_positive, np.log(x_positive + 1), color='purple')
axs[1, 1].set_title('f(x) = ln(x+1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')
axs[1, 1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
