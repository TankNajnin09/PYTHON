import numpy as np
import matplotlib.pyplot as plt

# Create an array of x values from 0 to 4*pi
x = np.linspace(0, 4 * np.pi, 1000)

# Calculate the sine of each x value
y = np.sin(x)

# Plot the curve
plt.plot(x, y, label='sin(x)', color='blue')

# Add title and labels
plt.title('Plot of the Sine Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
