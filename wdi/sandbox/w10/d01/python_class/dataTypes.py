#Exploring data types

# myList = [1,2,3,4,5,6]
# print myList[0]
#
# myList[0] = 'new value'
# print myList[0]  #['new value',2,3,4,5,6]
#
# myList.append(99)
# print myList #['new value',2,3,4,5,6,99]
#
# firstItem = myList.pop(0)
# print firstItem # 'new value'
# print myList #[2,3,4,5,6,99]
#
# lastItem = myList.pop()
# print lastItem # 99
# print myList # [2,3,4,5,6]
#
# myList.insert(0,33)
# print myList # [33,2,3,4,5,6]

# alphaList = ['a', 'booboo', 'baa']
#
# alphaList.sort()
# print alphaList #['a', 'baa','booboo']
#
# alphaList.reverse()
# print alphaList  #['booboo', 'baa', 'a']
#
# alphaList.remove('a')
# print alphaList  #['booboo', 'baa']
#
# print len(alphaList) #3

# TUPLES: an immutable indexed collection of data. More performant than lists
# myTuple = (1,2,3,4,5,5,5,'hello','tuples',True)
# # print myTuple[0] #1
#
# #myTuple[0] = 'change the value of the first item'  #object does not support item assignment
#
# print myTuple.count(5) #3
#
# print myTuple.index('hello') #7
#
# print myTuple.index(5) #4 prints the first instance of 5
#
# print len(myTuple)

# STRINGS an immutable indexed collection of data

# myString = 'hello python!'

# print myString[0]
#
# myString[0] = 'B' #object does not support item assignment

#print myString.find('python') #6 returns index where the word python starts

# print myString.title() # Hello Python!  capitalizes the first letter of each word

# print myString.replace('python', 'anaconda') #hello anaconda! returns a new string, but did't modify the original

#print myString.count('python') #1 (the one instance of python)

# wood = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('wood')
# chuck = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?'.count('chuck')
# print wood == chuck  #True (each word appears  4 times in the sentence, it counts the wood and chuck in woodchuck)
