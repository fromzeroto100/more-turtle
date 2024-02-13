from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
t1 = Turtle(shape="turtle")
t1.color("red")
t1.penup()
t1.goto(x=-230, y=-100)
t1.pendown

t2 = Turtle(shape="turtle")
t2.color("blue")
t2.penup()
t2.goto(x=-230, y=-30)
t2.pendown()
t3 = Turtle(shape="turtle")
t3.color("green")
t3.penup()
t3.goto(x=-230, y=20)
t3.pendown()
t4 = Turtle(shape="turtle")
t4.color("orange")
t4.penup()
t4.goto(x=-230, y=90)
t4.pendown()
t5 = Turtle(shape="turtle")
t5.color("yellow")
t5.penup()
t5.goto(x=-230, y=160)
t5.pendown()

screen.exitonclick() 