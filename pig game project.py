import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll
value = roll()
print(value)

while True:
    players = input("Enter the number of palyer (2-5): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=5:
            break
        else:
            print("Must be between 2-4 palyers.! ")
    else:
        print("Invalid , Try Again.!") 

max_score= 50
player_score =[0 for _ in range(players)]  

print(player_score)

while max(player_score)<max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1,"turn had just started! \n")
        print("your total score is: ", player_score[player_idx],"\n")
        current_score =0
        while True:
            should_roll = input("would to like to roll")
            if should_roll.lower()!="y":
                break

            value= roll()
            if value==1:
                print("you rolled a 1! turn done")
                current_score=0
                break
            else:
                current_score+= value
                print("you rolled a :",value)    

    print("your score is:",current_score)

    player_score[player_idx]+= current_score
    print("your total score is :", player_score[player_idx])

    max_score= max(player_score)
    winning_idx =player_score.index(max_score)
    print("player number ",winning_idx+1,"is the winner with score of: ",max_score)
    

