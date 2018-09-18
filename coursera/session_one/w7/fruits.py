"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""
#dictionary
fruit_to_color = {
    'banana': 'yellow',
    'cherry': 'red',
    'orange': 'orange',
    'peach': 'orange',
    'strawberry': 'red'}

#Invert fruit_to_color
color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]

    #If color is not alreadya key in the accumulator,
    #add color: [fruit] as entry
    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]

    #otherwise, append fruit to existing list
    else:
        color_to_fruit[color].append(fruit)
