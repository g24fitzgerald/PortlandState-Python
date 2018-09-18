"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def count_startswith(L, ch):
    ''' (list of str, str) -> int

    Precondition: the length of each item in L is >=1, and len(ch) == 1

    Return number of strings in L that begin with ch

    >>> count_startswith(['payday', 'lorem', 'price'], 'p')
    2
    '''
    #use list accumulator
    ch_strings = []

    #for each item in L if the item begins with ch add to accumulator
    for item in L:
        if item[0] == ch:
            ch_strings.append(item)
    #return length of accumulator
    return len(ch_strings)

def count_startswith_v2(L, ch):
    ''' (list of str, str) -> int

    Precondition: the length of each item in L is >=1, and len(ch) == 1

    Return number of strings in L that begin with ch

    >>> count_startswith_v2(['payday', 'lorem', 'price'], 'p')
    2
    '''
    #make a copy of L to hold values that start with ch
    startswith= L[:]

    #for each item in L if it doesnt start with ch, remove from startswith
    for item in L:
        if not item.startswith(ch):
            startswith.remove(item)
    #return length of startswith
    return len(startswith)

def count_startswith_v3(L, ch):
    ''' (list of str, str) -> int

    Precondition: the length of each item in L is >=1, and len(ch) == 1

    Return number of strings in L that begin with ch

    >>> count_startswith_v3(['payday', 'lorem', 'price'], 'p')
    2
    '''
    #make a copy of L to hold values that don't start with ch
    dontstartwith= L[:]

    #for each item in L if it starts with ch, remove from startswith
    for item in L:
        if item.startswith(ch):
            dontstartwith.remove(item)
    #return length of original - length of list startswith
    return len(L) - len(dontstartwith)
