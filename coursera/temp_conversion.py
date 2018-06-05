'''Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald'''

def convert_to_celsius(fahrenheight):
    '''(number) -> float

    Returns number of degrees celsius from its equivalent in fahrenheight

    >>>f_to_c(32)
    0.0
    >>>f_to_c(212)
    100.0
    '''
    return (fahrenheight - 32) * 5 / 9
