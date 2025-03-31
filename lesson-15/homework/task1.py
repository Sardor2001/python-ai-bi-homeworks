import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 4 * x + 4


x_values = np.linspace(-10, 10, 500)

y_values = f(x_values)

plt.figure(figsize=(8, 6))

plt.plot(x_values, y_values, label=r"f(x)=x^2-4x+4", color='blue', linewidth=2)

plt.title("PLot of f(x)=x^2 - 4x +4", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=14)

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(alpha=0.5)

plt.legend(fontsize=12)

plt.show()
