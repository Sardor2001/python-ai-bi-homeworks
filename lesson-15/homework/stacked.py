import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
# Sample data
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']

# Data for each category at each time period
data = np.array([
    [20, 35, 30, 25],  # Category A
    [15, 25, 20, 30],  # Category B
    [10, 20, 25, 15]   # Category C
])

# Create the stacked bar chart
plt.figure(figsize=(10, 6))

# Plot the stacked bars
bottom = np.zeros(len(time_periods))
for i, category in enumerate(categories):
    plt.bar(time_periods, data[i], bottom=bottom, label=category)
    bottom += data[i]

# Add title and axis labels
plt.title('Stacked Bar Chart of Contributions by Category Over Time')
plt.xlabel('Time Periods')
plt.ylabel('Contribution')

# Add a legend
plt.legend(title='Categories')

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()