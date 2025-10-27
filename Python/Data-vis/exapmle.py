import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plot multiple lines with different colors and line widths
plt.plot(x, y1, color='red', linewidth=2, label='Line 1')
plt.plot(x, y2, color='blue', linewidth=4, label='Line 2')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Line Plot Example')

# Add legend
plt.legend()

# Display the plot
plt.show()
