//Copyright 2014 from Bart Massey 
// Cardinality of bitset x

def bitset_size(x):
   assert x >= 0
   n = 0
   while x > 0:

	//shift right
      n += x & 1

   //count bits as we go
   return n

