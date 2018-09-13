"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""
#file exclusively for functions

def read_grades(gradefile):
    ''' (file open for reading) -> list of float

    Read and Return a list of grades in the file

    Precondition: gradefile starts with a header that
    contains no blank lines, has 1 blank line, then
    lines containing student number and grade
    '''

    #Skip over header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    #Read the grades accumulating into list
    grades = [] #accumulator

    line = gradefile.readline()
    while line != '': #signifies that we haven't reached the end of the file
        #find last space in the line (the ' ' between student id and grade)
        #and take everything after that
        grade = line[line.rfind(' ') + 1:]
        grades.append(float(grade)) #converts that string to a float
        line = gradefile.readline() #string of info for single student
    return grades

def count_grade_ranges(grades):
    ''' (list of float) -> list of int

    Return a list of int where each index indicates how many
    grades were in these grade ranges:

    0-9:   index 0
    10-19: 1
       :
    90-99: 9
    100:   10
    >>> count_grade_ranges([32.0, 81.0, 90.9, 87.8, 74.8, 100.0])
    [0,0,0,1,0,0,0,1,2,1,1]
    '''

    range_counts = [0] * 11

    for grade in grades:
        which_range = int(grade // 10) #gives index into range count
        range_counts[which_range] =  range_counts[which_range] + 1 #increments that count at that particular range

    return range_counts

def write_histogram(range_counts, histfile):
    ''' (list of int, file open for writing) -> NoneType

    Writes a histogram of *'s based on the number of grades in each range

    The output format:
    0-9:   *
    10-19: *
        :
    90-99: ***
    100:   *

    '''
    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    # Write the 2-digit ranges
    for i in range(1, 10):
        low = i * 10
        high = i * 10 + 9
        histfile.write('*' * range_counts[0])
        histfile.write('\n')

    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')
