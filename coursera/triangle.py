
'''Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald'''


'''1. header'''
def area_triangle(base, height):
    '''
    2. Type Contract
     (num, num) -> num

    3. Description
         Return the area of a triangle with dimentions base and height.

    4. Examples
    >>> area_triangle(10, 5)
    25.0
    >>> area_triangle(2.5, 3)
    3.75

    5. Body
    '''
    return base * height / 2


def perimeter(side1, side2, side3):
    '''
    (number, number, number) -> number
    Returns the perimeter of a triangle given 3 side lengths

    >>>(3,4,5)
    12
    >>>(3.3, 10, 3.8)
    17.1
    '''
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''
    (number, number, number) -> float
    returns one half the value of the perimeter of a triangle based on 3 side legths

    >>>semiperimeter(3,4,5)
    6.0
    >>>semiperimeter(10.5, 6, 9.5)
    12.9
    '''
    return perimeter(side1, side2, side3) / 2
