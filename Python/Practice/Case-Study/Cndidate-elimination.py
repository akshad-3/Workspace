import csv

# Read dataset
with open("/Users/akshad/GitHub/Workspace/Python/Practice/Case-Study/Dataset/Find-SAlgo.csv", "r") as file:
    data = list(csv.reader(file))

header = data[0]
examples = data[1:]

num_attributes = len(header) - 1

# Most specific hypothesis
S = ["Ø"] * num_attributes

# Most general hypothesis
G = [["?"] * num_attributes]


def more_general(h1, h2):
    for a, b in zip(h1, h2):
        if a != "?" and a != b:
            return False
    return True


for example in examples:

    attributes = example[:-1]
    target = example[-1]

    if target == "Yes":

        # Generalize S
        for i in range(num_attributes):

            if S[i] == "Ø":
                S[i] = attributes[i]

            elif S[i] != attributes[i]:
                S[i] = "?"

        # Remove G hypotheses inconsistent with S
        G = [
            g for g in G
            if more_general(g, S)
        ]

    else:

        new_G = []

        for g in G:

            for i in range(num_attributes):

                if g[i] == "?":

                    if S[i] != "?" and S[i] != "Ø":

                        new_hypothesis = g.copy()
                        new_hypothesis[i] = S[i]

                        new_G.append(new_hypothesis)

        G = new_G

print("Specific Boundary (S):")
print(S)

print("\nGeneral Boundary (G):")
for g in G:
    print(g)