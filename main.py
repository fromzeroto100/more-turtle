from turtle import Turtle, Screen
import random

turtle = Turtle()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-70, -10, 40, 90, 140, 180]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)
        

# t2 = Turtle(shape="turtle")
# t2.color("blue")
# t2.penup()
# t2.goto(x=-230, y=-30)
# t2.pendown()
# t3 = Turtle(shape="turtle")
# t3.color("green")
# t3.penup()
# t3.goto(x=-230, y=20)
# t3.pendown()
# t4 = Turtle(shape="turtle")
# t4.color("orange")
# t4.penup()
# t4.goto(x=-230, y=90)
# t4.pendown()
# t5 = Turtle(shape="turtle")
# t5.color("yellow")
# t5.penup()
# t5.goto(x=-230, y=160)
# t5.pendown()

screen.exitonclick() 