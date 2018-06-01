#copyright (c) Gina Fitzgerald 
#NB HW
#find earliest modal element of a sequence 

#Pseudocode: 
#d <- empty dictionary
#        m <- 0
#        for k in S
#            if k is a key in d
#                increment d[k]
#            else
#                d[k] <- 1
#            if d[k] > m
#                m <- d[k]
#        for k in S
#            if d[k] = m
#                return k

#Python Code 
def first_modal(sequence):
   assert sequence
   sequence_dictionary = {}
   max_index = 0

   for key in sequence_dictionary:
      if key in sequence:
         sequence_dictionary[key] += 1
      else:
         sequence_dictionary[key] = 1

      if seqence_dictionary[key] > max_index:
         max_index = sequence_dictionary[key]

   for key in sequence:
      if max_index == sequence_dictionary[key]:
         return key 

print(2 == first_modal([1, 2, 2, 4, 5]))
print(5 == first_modal([1, 5, 7, 7, 5]))
print(1 == first_modal([2, 2, 1, 4, 1]))




