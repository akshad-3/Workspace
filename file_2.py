word=input("Enter the word you want to search :")

with open("file_2.txt","r") as f:
    content = f.readlines()
lineno=1
for line in content:
    if word in line:
        print(f"The word {word} is present in file| on line NO. {lineno}")
        break
    lineno+=1
else:
    print(f"The word {word} is NOT present in file")