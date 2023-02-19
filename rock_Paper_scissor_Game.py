import random

def swg(computer,player):
    if(computer == player):
        return None
    if(computer=='r' and player=='p'):
        return True
    elif(computer=='s' and player=='r'):
        return True
    elif(computer=='p' and player=='s'):
        return True
    else:
        return False

playersum = 0
computersum = 0
matchdrawn = 0
choice2 =('r','p','s')

print("\n!!!!!....._______________WELCOME_TO_ROCK_PAPER_SCISSOR_GAME_______________.....!!!!!")
for i in range(0,10):
    player = input("\nChoose your choice ('Rock - r','Paper - p','Scissor -s') -:")
    i += 1
    print("______________________________________________________________________________")

    computer = random.randint(0,2)
    computer = choice2[computer]
    
    win = swg(computer,player)
    print(f"You choose {player} and the computer choose {computer}")
    if win is None :
        print("Match Drawn.....")
        matchdrawn += 1
    elif win:
        print(f"You won this round {i} :).....")
        playersum += 1
    else:
        print(f"You loose this round {i} :(.....")
        computersum += 1

if(playersum > computersum):
    print(f"\nyou won total {playersum} rounds")
    print(f"\nyou loose total {computersum} rounds")
    print(f"\nyour total matchdrawn are {matchdrawn}") 
    print("\n:) .......... YOU WON THE MATCH .......... :)")
elif(playersum == computersum):
    print(f"\nyou won total {playersum} rounds")
    print(f"\nyou loose total {computersum} rounds")
    print(f"\nyour total matchdrawn are {matchdrawn}") 
    print("\n:) .......... MATCH IS DRAWN .......... :)")
else:
    print(f"\nyou won total {playersum} rounds")
    print(f"\nyou loose total {computersum} rounds")
    print(f"\nyour total matchdrawn are {matchdrawn}") 
    print("\n:( .......... YOU LOOSE THE MATCH .......... :(")