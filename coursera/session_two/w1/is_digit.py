"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def is_digit(s):
    ''' (str) -> str

    Returns the char in str that are digits

    >>> is_digit('12abf')
    12
    '''
    digits = ""
    for ch in s:
        if ch.isdigit():
            digits = digits + ch
    return digits

def is_digit_v2(s):
    ''' (str) -> str

    Returns the char in str that are digits

    >>> is_digit_v2('12abf')
    12
    '''
    digits = ""
    for ch in s:
        if ch in '0123456789':
            digits = digits + ch
    return digits

def is_digit_v3(s):
    ''' (str) -> str

    Returns the char in str that are digits

    >>> is_digit_v3('12abf')
    12
    '''
    digits = ""
    for i in range (len(s)):
        if s[i].isdigit():
            digits = digits + s[i]
    return digits
    
def is_digit_v4(s):
    ''' (str) -> str

    Returns the char in str that are digits

    >>> is_digit_v4('12abf')
    12
    '''
    indices = []
    digits = ""

    for i in range (len(s)):
        if s[i].isdigit():
            indices.append(i)
    for index in indices:
        digits = digits + s[index]
    return digits
