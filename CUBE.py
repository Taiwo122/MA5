import matplotlib.pyplot as plt
import numpy as np

# Define the range of numbers for the first 5 cubic numbers
x_small = np.arange(1, 6)
y_small = x_small ** 3

# Define the range of numbers for the first 5000 cubic numbers
x_large = np.arange(1, 5001)
y_large = x_large ** 3

# Create the first plot for the first 5 cubic numbers
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.scatter(x_small, y_small, c=y_small, cmap='viridis', label='First 5 Cubic Numbers')
plt.colorbar()
plt.title('Plot of the First 5 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.legend()

# Create the second plot for the first 5000 cubic numbers
plt.subplot(2, 1, 2)
plt.scatter(x_large, y_large, c=y_large, cmap='viridis', label='First 5000 Cubic Numbers')
plt.colorbar()
plt.title('Plot of the First 5000 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
