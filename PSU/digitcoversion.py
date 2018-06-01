#Copyright 2014 Gina Fitzgerald
#in class exercise print thehex value of the set of vowels

n = 0
for c in ('a', 'e', 'i', 'o', 'u'):
   b =  2 **(ord(c) - ord('a'))
   n += b

print(format(n, 'x'))

