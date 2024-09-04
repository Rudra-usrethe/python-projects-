import turtle
import time
import random

WIDTH , HEIGHT = 500 , 500
COLORS = ['red', 'orange', 'yellow', 'black' , 'purple', 'pink', 'brown', 'blue','green','grey']
def get_number_of_racers():
    racers = 0
    while True:
        racers =  input("Enter the number of turtle betwwen (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not a numeric.. , Enter a valid Number: ")
            continue
        if 2<= racers <=10:
            return racers
        else:
            print("number is not in range!")
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance =  random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2-10:
                return colors[turtles.index(racer)]



def create_turtles(colors):
    turtles = [] 
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2 +20)# use to set a position of turtles    
        racer.pendown()
        turtles.append(racer)

    return turtles    

def init_turtle():
    screen =  turtle.Screen() # s always with S 
    screen.setup(WIDTH,HEIGHT)
    screen.title('Trutle Racing! ')
    



racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("game end !",winner)
time.sleep(5)