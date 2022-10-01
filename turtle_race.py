from turtle import Turtle,Screen, exitonclick
import random,time
screen=Screen()
screen.setup(width=500,height=500)
winner=False
turtle_winner=""
user_bet=""
colors=['red','green','blue','black','cyan','purple']
def create_turtles():
    turtles=[]
    for x in range(6):
        turtle=Turtle()
        turtles.append(turtle)
    return turtles
def turtle_color(turtles):
    for turtle in turtles:
        col=random.choice(colors)
        turtle.color(col)
        colors.remove(col)
def change_shape(turtles):
    for turtle in turtles:
        turtle.shape('turtle')
def turtle_position(turtles):
    x=-200
    y=-200
    for turtle in turtles:
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y)
        y+=50
def define_speed():
    speeds=[10,20,30,40,50]
    speed=random.choice(speeds)
    return speed
def move_forward(turtles):
    for turtle in turtles:
        turtle.forward(define_speed())
def check_win(turtles):
    global winner,turtle_winner
    for turtle in turtles:
        if turtle.xcor()>=200:
            winner=True
            turtle_winner=turtle.pencolor()
def check_bet():
    global turtle_winner,user_bet
    if turtle_winner==user_bet:
        print(f"you bet was {user_bet}")
        print("you got it right")
    else:
        print(f"your bet was {user_bet}")
        print(f"the winner is {turtle_winner} , good luck next time")
def create_finalLine():
    screen.tracer(0)
    t=Turtle()
    t.penup()
    t.setpos(x=200,y=-230)
    t.pendown()
    t.left(90)
    t.forward(350)
    t.hideturtle()
    screen.update()
def get_user_bet():
    user_bet=screen.textinput(title="make a bet", prompt="which turtle gonna win ?(choose your turle base on the color)")
    while user_bet not in colors:
        user_bet=screen.textinput(title="make a bet", prompt="which turtle gonna win ?(choose your turle base on the color)")
    return user_bet
def start_game():
    user_bet=get_user_bet()
    turtles=create_turtles()
    create_finalLine()
    change_shape(turtles)
    turtle_color(turtles)
    turtle_position(turtles)
    screen.update()
    while winner==False:
        move_forward(turtles)
        check_win(turtles)
        screen.update()
        time.sleep(1)
    check_bet()
start_game()
exitonclick()

