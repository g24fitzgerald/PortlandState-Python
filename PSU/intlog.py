#copyright 2014 
#in class assignment- Gina, Joel, Andrew, Naomie

def intlog(x):
   assert x >= 0
   count = 0
   while x > 0:
      print(format(x, 'b'))
      count += 1
      x >>= 1
   return count - 1

x = 25
print('intlog =', intlog(x))
print(x)




