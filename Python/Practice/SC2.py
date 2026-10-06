#Name : Patil Akshad Dhanaji
#Roll No : 53
import numpy as np

# Training data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target values (AND gate)
T = np.array([])

# Learning rate
eta = 0.1

# Initialize weights and bias
weights = np.zeros(2)
bias = 0

# Number of epochs
epochs = 100

# ADALINE training using Delta Rule
for epoch in range(epochs):

    total_error = 0

    for x, target in zip(X, T):

        # Calculate net input
        yin = np.dot(x, weights) + bias

        # Calculate error
        error = target - yin

        # Delta Rule weight update
        weights = weights + eta * error * x

        # Bias update
        bias = bias + eta * error

        # Sum squared error
        total_error += error ** 2

    print(f"Epoch {epoch + 1}: Error = {total_error:.4f}")

# Testing
print("\nADALINE Output:")

for x in X:

    yin = np.dot(x, weights) + bias

    # Threshold for final classification
    output = 1 if yin >= 0.5 else 0

    print(f"Input: {x} -> Output: {output}")