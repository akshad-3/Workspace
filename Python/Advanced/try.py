try:
    with open("text1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("text2.txt","r") as f:   # <-- no indent
        print(f.read())
except Exception as e:
    print(e)
    
try:
    with open("text3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Code is executed")
