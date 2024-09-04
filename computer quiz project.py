print("Welcome to my computeer quiz! \n")
playing = input("Do you want to play! \n")
if playing.lower() != "yes":
    quit()
print("okay! lets play the game :)")
score =0 
answer= input("what does CPU stands for ? \n")
if answer.lower()=="central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer= input("what does GPU stands for ? \n")
if answer.lower()=="graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer= input("what does RAM stands for ? \n")
if answer.lower()=="random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer= input("what does PUS stands for ? \n")
if answer.lower()=="power supply":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " Question correct :)")
print("You got "+ str((score/4)*100)+"%")