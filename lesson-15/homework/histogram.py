import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


# Generate 1000 random values from a normal distribution (mean=0, std=1)
np.random.seed(42)  # For reproducibility
data = np.random.normal(0, 1, 1000)

# Create the histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)

# Add title and axis labels
plt.title('Histogram of 1000 Random Values from a Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()