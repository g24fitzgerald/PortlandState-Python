'''Learn to Program: Crafting Quality Code | University of Toranto Computer Science
2018 Gina Fitzgerald'''

#approaches/algorithms:
# 1 Reverse the string and check for equality

# 2 Split string in half, reverse second half, compare with original

# 3 compare str[0] to str[-1], str[1] to str[-2] until you reach the middle

def pallendrome_index(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> pallendrome_index('noon')
    True
    >>> pallendrome_index('truck')
    False
    '''
    return str == str[::-1]


def pallendrome_reverse(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> pallendrome_index('noon')
    True
    >>> pallendrome_index('truck')
    False
    '''
    return reverse(str)

def pallendrome_split(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> pallendrome_split('noon')
    True
    >>> pallendrome_split('racecar')
    True
    >>> pallendrome_split('truck')
    False
    '''
    #starting index of 2nd half of word ommitting middle letter of odd word
    second_index = len(str) // 2 + 1

    #slice strings to get first and second half of word ommitting middle letter
    first_half = str[:len(str) // 2]
    second_half = str[second_index:]

    return first_half == reverse(second_half)


def pallendrome_char_check(str):
    ''' (str) -> bool

    Returns whether or not a given string is a pallendrome

    >>> pallendrome_char_check('noon')
    True
    >>> pallendrome_char_check('truck')
    False
    '''
    # My initial Solution
    # for i in range(1, len(str)):
    #     if str[i] != str[len(str) -i -1]:
    #         return False
    # return True

    #Revised Solution
    i = 0
    j = len(str) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - i
    return j <= i 

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
