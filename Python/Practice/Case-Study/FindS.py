import csv

# Read dataset
with open("/Users/akshad/GitHub/Workspace/Python/Practice/Case Study/Dataset/Find-SAlgo.csv", "r") as file:
    data = list(csv.reader(file))

header = data[0]
examples = data[1:]

# Initial hypothesis
hypothesis = ["Ø"] * (len(header) - 1)

# Find-S
for example in examples:
    attributes = example[:-1]
    target = example[-1]

    if target.lower() == "yes":
        for i in range(len(attributes)):
            if hypothesis[i] == "Ø":
                hypothesis[i] = attributes[i]
            elif hypothesis[i] != attributes[i]:
                hypothesis[i] = "?"

print("Final Hypothesis:")
print(hypothesis)