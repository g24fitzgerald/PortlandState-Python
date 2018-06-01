myList = [1,2,3,4]
myTouple = [1,2,3,4]

#If, Else IF, and Else
if not(True):
    print 'Does If print?'
elif True:
    print 'Does else-if print?' #this one prints because True is true
else:
    print 'Does else print'

if 1 in myList:
    print 'Do I print???'  #yes it prints because 1 is in myList

if 4 in myTouple:
    print 'Does this one print too?' #yes it prints because 4 is in myTouple

#not in
if 5 not in myTouple:
    print 'Does this one print?' #yes this prints because 5 is not in myTouple
