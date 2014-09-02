#Display list for ASCII graphics

from ascii_graphics import *

class shape():
    def render(self):
        assert False
        
class point(shape):

    def __init__(self,p):
        self.p = p

    def render(self,screen):
        draw_point(screen, self.p)

class line(shape):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def render(screen, self.p1, self.p2)

class display_list():
    
    def __init__(self):
        self.display_list=[]

    #append to the display list
    def add(self, shape):
        self.display_list += [shape]

    #render a display list
    def render_display_list(display_list):  
        screen= make_screen()
        for d in self.display_list:
            d.render(screen)
        render_screen(screen)
