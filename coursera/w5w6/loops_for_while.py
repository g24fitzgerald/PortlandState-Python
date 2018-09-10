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

### Parallel Lists and Loops

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

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return number of positions in s1 that contain
    the same character at the corresponding position of s2

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''

    matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            matches = matches + 1
    return matches
    
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
    return pairs

#### Nested Lists and Loops
def calculate_average(asn_grades):
    '''(list of lists of [str, number]) -> float

    Return the average of all the grades in asn_grades

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0.0
    for item in asn_grades:
        total = total + asn_grades[1]
    return total / len(asn_grades)

def averages(grades):
    '''(list of lists of number) -> list of float

    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position
    of grades

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    average_grades = []
    for grades_list in grades:
        #calculate the average of grades_list and append to averages
        total = 0
        for mark in grades_list:
            total = total + mark
        average_grades.append(total/len(grades_list))
    return average_grades
