from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = [Turtle() for i in range(6)]

height = -140

for _ in range(6):
    turtles[_].pu()
    turtles[_].shape("turtle")
    turtles[_].color(colors[_])
    turtles[_].goto(-230, height)
    height += 60

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


screen.exitonclick()

