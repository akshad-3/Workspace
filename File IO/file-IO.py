import random

def game():
    print("Starting the Game...")
    score = random.randint(1,100)
    with open("file.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
            
    print(f"you Score is :{score}")
    print(f"you High Score is :{hiscore}")

    if(score>hiscore):
        with open("file.txt","w") as f:
            f.write(str(score))

game()
        
        
