"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def is_one_to_one(d):
    ''' (dict) -> bool

    Return True if and only if no two d's keys map to the same value

    >>> is_one_to_one({'a': 1, 'b': 2, 'c':3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c':1})
    False
    >>> is_one_to_one({})
    True
    '''
    values_seen = []
    for key in d:
        #if we've already seen the value in another key, false
        if d[key] in values_seen:
            return False
        else:
            values_seen.append(d[key])
    return True

def is_one_to_one_v2(d):
    ''' (dict) -> bool

    Return True if and only if no two d's keys map to the same value

    >>> is_one_to_one_v2({'a': 1, 'b': 2, 'c':3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c':1})
    False
    >>> is_one_to_one_v2({})
    True
    '''
    L1 = list(d.values())
    L2 = L1[:]

    L2 = remove_duplicate(L2)
    return len(L1) == len(L2)

# Python code to remove duplicate elements
def remove_duplicate(L):
    final_list = []
    for char in L:
        if char not in final_list:
            final_list.append(char)
    return final_list
