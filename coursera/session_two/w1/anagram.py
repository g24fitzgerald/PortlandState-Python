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

#unrelated to prev function 
def make_dictionary(s):
    ''' (str) -> dict of {str : int}

    Return a dictionary of keys str and
    values int of the number of ocurrances of letter in str

    >>> make_dictionary('noodle'):
    {n:1, o:2, d:1, l:1, e:1}
    '''
    d = {}
    for i in s:
        #if char not in accumulator
        #add s[i] as entry
        if not (s[i] in d):
            d[s[i]] == 1
        #otherwise increment value of char key
        else:
            d[s[i]] == d[s[i]] + 1
    return d
