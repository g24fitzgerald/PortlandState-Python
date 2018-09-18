'''Learn to Program: Crafting Quality Code | University of Toranto Computer Science
2018 Gina Fitzgerald'''

def anagram_v1(s1, s2):
    ''' (str, str) -> bool

    Return True if and only if s1 is an anagram of s2
    list method

    >>> anagram_v1('silent, listen')
    True
    >>> anagram_v1("bear", "breach")
    False
    '''
    L1 = list(s1)
    L2 = list(s2)
    L1.sort()
    L2.sort()
    return L1 == L2
