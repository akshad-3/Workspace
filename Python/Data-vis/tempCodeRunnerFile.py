import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plot lines
plt.plot(x, y1, color='blue', linewidth=2, label='Line 1')
plt.plot(x, y2, color='red', linewidth=3, label='Line 2')

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Line Plot")

# Show legend
plt.legend()

# Display graph
plt.show()
