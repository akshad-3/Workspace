word=input("Enter the word you want to search :")

with open("file_2.txt","r") as f:
    content = f.read()

if(word in content):
    print(f"The word {word} is present in file")
else:
    print(f"The word {word} is NOT present in file")