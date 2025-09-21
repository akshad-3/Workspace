words=["idiot","silly","bad"]

with open("file_1.txt","r") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word,"#"*len(word))

with open("file_1.txt","w") as f:
    f.write(content)
    