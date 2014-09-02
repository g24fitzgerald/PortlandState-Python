#copyright (c) Gina Fitzgerald
#create PRNG called randrange()

#define variables
s=12


#define randrange
def randrange(p1, p2=None):

    global s

    #analyze performance to set bounds
    if p2 == None:
        lower = 0
        upper = p1

    else:
        lower = p1
        upper = p2

    #compute result be normalizing bound
    r = s % (upper - lower) +lower

    #update seed

    s = (s * 55) % 251

    return r


 
   
