import random
import time
print("**WELCOME TO 'ROCK-PAPER-SCISSORS' GAME**")
print("*YOU VS COMPUTER* - The One To Reach 3 Points First Wins!")
print("Rock - 'R'\nPaper - 'P'\nScissors - 'S'")
print()
time.sleep(2)
player = 0
comp = 0
def show_points():
    print("YOU = ",player,"Points")
    print("Computer =",comp,"Points")
while(player!=3 and comp!=3):
    rand = random.choice(["Rock","Paper","Scissors"])
    print("Rock...")
    time.sleep(0.8)
    print("Paper...")
    time.sleep(0.8)
    print("Scissors..")
    val = input("Waiting For Your Pick.. (R/P/S) : ")
    print()
    if(val == "R"):
        player_ch = "Rock"
    elif(val == "P"):
        player_ch = "Paper"
    elif(val == "S"):
        player_ch = "Scissors"
    else:
        print("**Error Occured**")
        break
    print("<",player_ch,"VS",rand,">")
    if(player_ch==rand):
        print("*****DRAW*****")
    elif((player_ch == "Rock" and rand == "Scissors") or (player_ch == "Paper" and rand == "Rock") or (player_ch == "Scissors" and rand == "Paper")):
        print("*YOU EARNED A POINT*")
        player+=1
    else:
        print("*COMPUTER EARNED A POINT*")
        comp+=1
    show_points()
    print()
    time.sleep(0.5)
if(player == 3):
    print("**YOU WON! CONGRATS**")
elif(comp == 3):
    print("**YOU LOST, TRY AGAIN**")
print()
print("-----GAME OVER-----")
input("Press Enter To Exit...")
    
    
    