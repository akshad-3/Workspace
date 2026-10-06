import numpy as np

# XOR training data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

T = np.array([0, 1, 1, 0])

# Weights for hidden layer
# Neuron 1 learns OR
w1 = np.array([1.0, 1.0])
b1 = 0.0

# Neuron 2 learns AND
w2 = np.array([1.0, 1.0])
b2 = -1.5

# Output layer
# XOR = OR AND NOT(AND)
w_out = np.array([1.0, -2.0])
b_out = 0.0


def step(x):
    return 1 if x >= 0 else 0


print("X1 X2 | XOR Output")
print("------------------")

for x in X:

    # Hidden layer
    h1 = step(np.dot(x, w1) + b1)       # OR
    h2 = step(np.dot(x, w2) + b2)       # AND

    # Output layer
    output = step(h1 - h2)

    print(x[0], " ", x[1], " | ", output)