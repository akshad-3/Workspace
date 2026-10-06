#Name : Patil akshad Dhanaji
#Roll no : 53

def mp_neuron(input, weights, threshold):
    weighted_sum = 0

    for x, w in zip(input, weights):
        weighted_sum += x * w

    if weighted_sum >= threshold:
        return 1
    else:
        return 0

input = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("AND GATE:")
print("X1 X2 Output")

for x in input:
    output = mp_neuron(x, weights=[1, 1], threshold=2)
    print(x[0], x[1], output)

print("\nOR GATE:")
print("X1 X2 Output")

for x in input:
    output = mp_neuron(x, weights=[1, 1], threshold=1)
    print(x[0], x[1], output)

print("\nNOT GATE:")
print("X Output")

for x in [0, 1]:
    output = mp_neuron([x], weights=[-1], threshold=0)
    print(x, "->", output)