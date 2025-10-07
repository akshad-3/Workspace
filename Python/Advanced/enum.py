l = [13,14,15,16,17,28,18,19,20,21]

# index=0
# for i in l:
#     print(f"At index {index} the value is {i}")
#     index+=1
#-->insted of doing this waht we can do is...<--

for index,i in enumerate(l):
    print(f"At index {index} the value is {i}")