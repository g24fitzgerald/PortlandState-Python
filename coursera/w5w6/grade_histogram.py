"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""
# A Read Grades Into a List
# B Count the grades per range
# C Write histogram to file

#this file is the main program, it holds constants and imports functions

import tkinter.filedialog
import grade
#1. define varables to where we read from and where we save to
a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename,'r')

a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename,'w')

# A Read Grades Into a List
grades = grade.read_grades(a1_file)

# B Count the grades per range
range_counts = grade.count_grade_ranges(grades)

#print(range_counts) #test

# C Write the histogram to the file
grade.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_histfile.close()
