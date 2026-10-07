import csv

# Read dataset
with open("/Users/akshad/GitHub/Workspace/Python/case study/data.csv", "r") as file:
    data = list(csv.reader(file))

# Remove header
header = data[0]
examples = data[1:]

# Start with most specific hypothesis
hypothesis = ["Ø"] * (len(header) - 1)

# Find-S algorithm
for example in examples:

    attributes = example[:-1]
    target = example[-1]

    # Consider only positive examples
    if target == "Yes":

        for i in range(len(attributes)):

            if hypothesis[i] == "Ø":
                hypothesis[i] = attributes[i]

            elif hypothesis[i] != attributes[i]:
                hypothesis[i] = "?"

print("Attributes:")
print(header[:-1])

print("\nFinal Hypothesis:")
print(hypothesis)