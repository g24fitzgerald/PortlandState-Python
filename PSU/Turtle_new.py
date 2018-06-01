#copyright (c) 2014 Gina Fitzgerald
#in class turtle exercise

from turtle import *

def leg():
    forward(50)
    backward(100)
    forward(50)

setheading(45) #start pointed at 45 degrees (North is 90 degrees in standard mode, 0 in logo mode)

leg()           #execute leg method

left(90)        #move 90 degrees to left

leg()           #execute leg method

done() 
