def read_grades(gradefile):
    ''' (file open for reading) -> dict of {float: list of str}

    Read and Return a dictionary where
    each key is a grade and each value is the list
    of ids of students who earned that grade

    Precondition: gradefile starts with a header that
    contains no blank lines, has 1 blank line, then
    lines containing student number and grade
    '''

    # Skip Over Header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # Read Grades, accumulate in dictionary
    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':
        student_id = line[:4] #string containing 4 digits of student id
        grade = float(line[4:].strip()) #strip removes whitespace

        # Case where key is not in dict
        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id] #add student id string as a list item
        # Case where key is already in dict
        else:
            grade_to_ids[grade].append(student_id)

        line = gradefile.readline()
    return grade_to_ids
