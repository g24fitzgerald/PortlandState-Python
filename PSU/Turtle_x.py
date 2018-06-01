#Copyright (c) 2014 Gina Fitzgerald
#Draw random "x"s with the turtle

from turtle import *


def random_x():
    global canvas_width, canvas_height

    def randcoord(d):
        return randrange(2 * d) - d

    #go to random coordinate within canvas height and width 
    goto(randcoord(canvas_width), randcoord(canvas_height))

    #give heading 
    setheading(randrange(360))

    #draw the x
    draw_x()

(canvas_width, canvas_height) = screensize()
speed(10)
for _ in range(40):
    random_x()
hideturtle()
done()
