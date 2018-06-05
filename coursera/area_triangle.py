
'''Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald'''


'''1. header'''
def area_triangle(base, height):
'''2. Type Contract'''
    '''(num, num) -> num

   3. Description
        Return the area of a triangle with dimentions base and height.
'''
'''4. Examples
   >>> area_triangle(10, 5)
   25.0
   >>> area_triangle(2.5, 3)
   3.75

   5. Body '''
    return base * height / 2
