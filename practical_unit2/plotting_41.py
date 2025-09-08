import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = np.array([2, 3, 5, 7, 11])
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]
sizes = [15, 30, 45, 10]
hist_data = np.random.randn(1000)
scatter_x = np.random.rand(50)
scatter_y = np.random.rand(50)

# Set figure size
plt.figure(figsize=(15, 10))

# 1. Line Plot (1st subplot)
plt.subplot(2, 3, 1)  # (rows, columns, index)
plt.plot(x, y, marker='o', color='blue')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# 2. Bar Chart (2nd subplot)
plt.subplot(2, 3, 2)
plt.bar(categories, values, color='orange')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 3. Pie Chart (3rd subplot)
plt.subplot(2, 3, 3)
plt.pie(sizes, labels=['Apple', 'Banana', 'Cherry', 'Date'], autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.axis('equal')

# 4. Histogram (4th subplot)
plt.subplot(2, 3, 4)
plt.hist(hist_data, bins=25, color='green', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')

# 5. Scatter Plot (5th subplot)
plt.subplot(2, 3, 5)
plt.scatter(scatter_x, scatter_y, color='red', alpha=0.6)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Leave the 6th subplot blank (optional)
plt.subplot(2, 3, 6)
plt.axis('off')

# Adjust layout
plt.tight_layout()
plt.suptitle("All Plots in One Figure Using Subplot", fontsize=16, y=1.02)

# Show all plots in one window
plt.show()
