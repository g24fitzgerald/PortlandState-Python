"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def up_to_vowels(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s

    >>> up_to_vowels('hello')
    'h'
    >>> up_to_vowels('bcvir')
    'bcvir'
    >>> up_to_vowels('FYH')
    'FYH'
    '''

    # before_vowel contains all characters found in s[0:i]
    before_vowel = ''
    i = 0

    # Accumulate the non-voewls at beginning of the string
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1
    return before_vowel

def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask user for a 'yes' or 'no'
    answer and continue asking until the user gives
    a valid response. Return the answer

    '''

    answer = input(prompt)
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)
    return answer

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurances of a characters and
    adjacent character being the same

    >>> count_adjacent_repeats('abccdeffggh')
    3
    >>> count_adjacent_repeats('noob')
    1
    >>> count_adjacent_repeats('help')
    0
    '''

    repeated_characters = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeated_characters = repeated_characters + 1
    return repeated_characters

def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position

    Precondition: len(L) >=1
    '''

    first_item = L[0]
    for i in range(1, len(L)):
        #shift each element to the left
        L[i - 1] = L[i]

    #shift last element to value of first
    L[-1] = first_item

def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the corresponding
    position of list1 and list2

    Precondition: len(list1) == len(list2)

    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 3]
    '''
    summed_list = []
    for i in range(len(list1)):
        summed_list.append(list1[i] + list2[i])
    return summed_list
