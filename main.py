from turtle import Turtle, Screen, colormode
import random
# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
# colour_palette = []
# for _ in colours:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     colour = (r, g, b)
#     colour_palette.append(colour)

colour_list = [(222, 152, 103), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
               (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102),
               (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119),
               (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

timmy_the_turtle = Turtle()
colormode(255)
timmy_the_turtle.speed("fastest")

timmy_the_turtle.ht()

timmy_the_turtle.pu()
timmy_the_turtle.setheading(225)
timmy_the_turtle.fd(300)
timmy_the_turtle.setheading(0)
timmy_the_turtle.pd()

for columns in range(10):
    for rows in range(10):
        timmy_the_turtle.color(random.choice(colour_list))
        timmy_the_turtle.begin_fill()
        timmy_the_turtle.circle(20)
        timmy_the_turtle.end_fill()
        timmy_the_turtle.pu()
        timmy_the_turtle.fd(50)
        timmy_the_turtle.pd()
    timmy_the_turtle.pu()
    timmy_the_turtle.goto(timmy_the_turtle.xcor() - 500, timmy_the_turtle.ycor() + 50)
    timmy_the_turtle.pd()

screen = Screen()
screen.exitonclick()
