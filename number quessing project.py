import random
# random_number= random.randr(-5 , 10 )# here it generate number till 9 only but can't 10 is you want to generate it you have to write 11 on place of 10
top_of_range = input("Type a number :-)")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than zero.')
        quit()
else:
    print('please type a number next time.')  
    quit()  
random_number= random.randint(0, top_of_range)# this produce 11
guesses = 0 
while True:
    guesses += 1 
    user_guess = input("Make a Guess :-  ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
     print('please type a number next time.')  
     continue
    if user_guess == random_number:
        print("You got it !")
        break
    elif user_guess> random_number:
            print("You are above the number!")
    else :
            print("You are below the number!")    

print("You get it on ", guesses,"Guesses")        