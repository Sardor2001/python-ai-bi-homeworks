import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])

# Add title and axis labels
plt.title('Sales Data for Five Different Products')
plt.xlabel('Products')
plt.ylabel('Sales')

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()