#Copyright (c) 2014 Bart Massey
#Class exercise generate permutations and try something with each


#pick each element in turn, generate and stick to end of partial permutation
def try_perms(source_set, eval_function):

    #pass partial permutations down as argument 
    def complete_perm(current_elements, partial_permutation):
        if len(current_element) == 0:
            eval_function(partial_permutation)
            return
        for e in cirrent_elements:
            complete_perm(current_elements.difference({e}),\
                          partial permutation + [e])
            
    #start with empty permutation, in recursive call tac each
    #additional element
    complete_perm(source_set, [])

class Found(Exception):
    def __init__(self, result):
        self.result = result

def three_second(p):            #Looking for specific perm
    if p[1] == 3:               #if program finds that 2nd element of permutation=3 
        raise Found(p)          #raises Found(exception) for that permutation 
