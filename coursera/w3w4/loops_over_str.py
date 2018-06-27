"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""
def collect_vowels(s):
    ''' (str) -> str

    Return the vowels from s.
    Don't treat the letter y as a vowel.

    >>>collect_vowels('Happy Anniversary!')
    'aAiea'
    >>>collect_vowels('xyz')
    ''
    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels
    
def count_vowels(s):
    '''(str) -> int

    Return the number of vowels in s.
    Don't treat the letter y as a vowel.

    >>>count_vowels('Happy Anniversary!')
    5
    >>>count_vowels('xyz')
    0
    '''
    num_vowels = 0
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels
