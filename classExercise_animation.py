#Copyright 2014 Gina Fitzgerald 
#Bart Massey's in class exercise

from time import sleep

width = 20

def clear():
    print(end="\r")
    print(" " * width, end ="\r")
    
def display_animation(figure, positions):

    #print number of spaces with arrow, and return 
    def display_frame(i):
        print(" "* i + figure, end = "\r")

    for i in positions:
        sleep(0.1)
        clear()
        display_frame(i)

def animation_move_right(figure):
    display_animation(figure, range(width - len(figure) +1))

def animation_move_left(figure):
    display_animation(figure, range(width - len(figure), -1, -1))
   



animation_move_right('->')
animation_move_left('<-')
animation_move_right('==>')
animation_move_left('<==')
print()

    

