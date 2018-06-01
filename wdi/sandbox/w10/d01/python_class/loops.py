aList = ['apples', 'oranges', 'pineapples']

#what does the range function do?
whatIsRange = range(1,10)
whatIsRangeAgain = range(20,30)

print whatIsRange #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print whatIsRangeAgain #[20, 21, 22, 23, 24, 25, 26, 27, 28, 29] prints the values including and up to specified

#count up to ten basic for loop. could replace range with a touple or list 
for i in range(0,10):
    print i
'''
0
1
2
3
4
5
6
7
8
9'''

#Looping through a list
for i in range(len(aList)):
    print 'value is %s' % aList[i]

'''value is apples
value is oranges
value is pineapples'''

#Looping through a list another way
for index, value in enumerate(aList):
    print 'the index is %d' % index
    print 'the value is %s' % value
'''the index is 0
the value is apples
the index is 1
the value is oranges
the index is 2
the value is pineapples '''

#While loops, basic
number = 0
while number < 10:
    print number
    number += 1
'''0
1
2
3
4
5
6
7
8
9 '''

#using while loops to loop through array
anotherNumber = 0
aList = ['apples', 'bananas', 'oranges']
while anotherNumber < len(aList):
    print aList[anotherNumber]
    anotherNumber += 1
''' apples
bananas
oranges'''
