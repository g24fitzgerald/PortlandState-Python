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
