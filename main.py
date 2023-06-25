from turtle import Turtle, Screen
import random


s = Screen()
s.setup(500, 400)
bet = s.textinput("Make you bet", "Which turtle do you want to bet on? Pick you color:")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y = [-90, -60, -30, 00, 30, 60]
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-230, y[turtle_index])
    all_turtles.append(t)
is_on = True
while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_turtle = turtle.pencolor()
            if bet == winning_turtle:
                print(f"You've won! The winner is {winning_turtle}")
            else:
                print(f"You've lost! The winner is {winning_turtle}")
    
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)   




s.exitonclick()