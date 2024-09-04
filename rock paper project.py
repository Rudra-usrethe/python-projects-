import random 

user_wins =0
computer_wins =0

option =["rock","paper","scissors"]

while True :
    user_input =input("Type Rock / Paper / scissors |or| Q to Quit.  ").lower()
    if user_input == "q":
        break
    if user_input not in  option:
        continue
    random_number = random.randint(0,2)
    computer_pick = option[random_number]
    print("Computer Picked ", computer_pick+".")

    if user_input == "rock"and computer_pick=="scissors":
        print("You wins! |and| Computer lost ")
        user_wins+=1

    
    elif user_input == "paper"and computer_pick=="rock":
        print("You wins! |and| Computer lost ")
        user_wins+=1
    
    elif user_input == "scissors"and computer_pick=="paper":
        print("You wins! |and| Computer lost ")
        user_wins+=1
    else :
        print("Computer Wins |and| You lost ")
        computer_wins += 1

print("You Won !", user_wins,"Computer lost.")
print("The computer Won ",computer_wins,"Times")
print("Meet you in next game :-)")       