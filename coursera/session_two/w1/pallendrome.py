'''Learn to Program: Crafting Quality Code | University of Toranto Computer Science
2018 Gina Fitzgerald'''

#approaches/algorithms:
# 1 Reverse the string and check for equality

# 2 Split string in half, reverse second half, compare with original

# 3 compare str[0] to str[-1], str[1] to str[-2] until you reach the middle

def pallendrome_full(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> pallendrome_full('noon')
    True
    >>> pallendrome_full('truck')
    False
    '''
    return str == str[::-1]

def pallendrome_split(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> 'noon'
    True
    >>> 'truck'
    False
    '''

def pallendrome_char_check(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> 'noon'
    True
    >>> 'truck'
    False
    '''
    for i in range(1, len(str)):
        if str[i] != str[len(str) -i -1]:
            return False
    return True

def reverse(s):
    ''' (str) -> str

    Return a reversed version of the string

    >>> reverse('hello')
    'olleh'
    >>> reverse('h')
    'h'
    '''
    rev = ''

    # add each char from string to the beginning of rev
    for ch in s:
        rev = ch + rev
    return rev
