"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotides = 0
    for char in dna:
        if nucleotide in char:
            num_nucleotides = num_nucleotides + 1
    return num_nucleotides

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """(str)->bool
    Return True if a string of dna contains only valid nucleotides (A,T,C or G).
    Only uppercase are valid
    >>>is_valid_sequence('AATCG')
    True
    >>>is_valid_sequence('PXIOATP')
    False
    """
    is_dna = True
    for char in dna:
        if char not in 'AGCT':
            is_dna = False
    return is_dna

def insert_sequence(dna1, dna2, index):
    """(str,str,int)->str

    Return the dna sequence given by inserting dna2 into dna1 at the given index.
    >>>insert_sequence('ACCAG', 'CCC', -1)
    'ACCACCCG'
​    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """
    return (dna1[ : index] + dna2 + dna1[index : ])

def get_complement(nucleotide):
    """(str) -> str

    Return the complement nucleotide of a nucleotide given
    A bonds with T, and G bonds with C

    >>>get_complement('A')
    'T'
    >>>get_complement('G')
    'C'
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'not a nucleotide'

def get_complementary_sequence(dna):
    """(str) -> str
    Return the dna sequence with complementary nucleotides of the dna sequence given
    A to T and G to C.

    >>> get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('GAC')
    'CTG'
    """
    complement_dna = ''
    for char in dna:
        complement_dna = complement_dna + get_complement(char)
    return complement_dna
