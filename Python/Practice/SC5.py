import numpy as np
characters = {
    'A': [
        0,1,1,1,0,
        1,0,0,0,1,
        1,1,1,1,1,
        1,0,0,0,1,
        1,0,0,0,1
    ],

    'B': [
        1,1,1,1,0,
        1,0,0,0,1,
        1,1,1,1,0,
        1,0,0,0,1,
        1,1,1,1,0
    ],

    'C': [
        0,1,1,1,1,
        1,0,0,0,0,
        1,0,0,0,0,
        1,0,0,0,0,
        0,1,1,1,1
    ],

    'D': [
        1,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        1,0,0,0,1,
        1,1,1,1,0
    ],
    'Z': [
            1,1,1,1,1,
            0,0,0,1,0,
            0,0,1,0,0,
            0,1,0,0,0,
            1,1,1,1,1
        ]
}

X = np.array(list(characters.values()), dtype=float)
labels = list(characters.keys())
rows = 2
cols = 2
input_size = 25

learning_rate = 0.5
epochs = 100
np.random.seed(42)
weights = np.random.rand(rows, cols, input_size)
def find_bmu(sample):

    distances = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            distances[i, j] = np.linalg.norm(
                sample - weights[i, j]
            )

    bmu = np.unravel_index(
        np.argmin(distances),
        distances.shape
    )

    return bmu
for epoch in range(epochs):
    current_lr = learning_rate * (1 - epoch / epochs)

    for sample in X:
        bmu = find_bmu(sample)
        for i in range(rows):
            for j in range(cols): 
                grid_distance = np.sqrt(
                    (i - bmu[0]) ** 2 +
                    (j - bmu[1]) ** 2
                )
                neighborhood = np.exp(
                    -(grid_distance ** 2) / 2
                )
                weights[i, j] += (
                    current_lr *
                    neighborhood *
                    (sample - weights[i, j]))

neuron_labels = {}

for index, sample in enumerate(X):

    bmu = find_bmu(sample)

    neuron_labels[bmu] = labels[index]
def recognize_character(pattern):
    pattern = np.array(pattern, dtype=float)
    bmu = find_bmu(pattern)
    if bmu in neuron_labels:
        return neuron_labels[bmu], bmu
    distances = []

    for sample in X:
        distances.append(
            np.linalg.norm(pattern - sample)
        )

    closest = np.argmin(distances)

    return labels[closest], bmu
test_character = [
    1,1,1,1,1,
    0,0,0,1,0,
    0,0,1,0,0,
    0,1,0,0,0,
    1,1,1,1,1
]
result, neuron = recognize_character(test_character)

print("Input Character: Z")
print("Recognized Character:", result)
print("Winning Neuron:", neuron)