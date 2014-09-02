#snowflake curve with turtle

from turtle import *

#number of fractal levels deep to draw
dim = 5

def snowflake(n):
    global canvas_width, canvas_height, dim
    if n == 0:
        forward(canvas_width * 2 // 3**dim)    #0th order curve
        return

    snowflake(n - 1)
    left(60)
    snowflake(n-1)
    right(120)
    snowflake(n-1)
    left(60)
    snowflake(n-1)

(canvas_width, canvas_height) = screensize()
speed(10)
penup()
setx(-canvas_width)
setheading(90)
pendown()
snowflake(dim) 
    
