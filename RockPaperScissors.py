import random
print("**WELCOME TO 'ROCK-PAPER-SCISSORS' GAME**")
print("*YOU VS COMPUTER* - The One To Reach 3 Points First Wins!")
print("Rock - 'R'\nPaper - 'P'\nScissors - 'S'")
print()
player = 0
comp = 0
def show_points():
    print("YOU = ",player,"Points")
    print("Computer =",comp,"Points")
while(player!=3 and comp!=3):
    rand = random.choice(["Rock","Paper","Scissors"])
    val = input("Enter Your Pick.. (R/P/S) : ")
    print()
    if(val == "R"):
        str = "Rock"
    elif(val == "P"):
        str = "Paper"
    elif(val == "S"):
        str = "Scissors"
    else:
        print("**Error Occured**")
        break
    print("<",str,"VS",rand,">")
    if(str==rand):
        print("*****DRAW*****")
    elif((str == "Rock" and rand == "Scissors") or (str == "Paper" and rand == "Rock") or (str == "Scissors" and rand == "Paper")):
        print("*YOU EARNED A POINT*")
        player+=1
    else:
        print("*COMPUTER EARNED A POINT*")
        comp+=1
    show_points()
    print()
if(player == 3):
    print("**YOU WON! CONGRATS**")
elif(comp == 3):
    print("**YOU LOST, TRY AGAIN**")
print()
print("-----GAME OVER-----")
input("Press Enter To Exit...")
    
    
    