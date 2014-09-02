#copyright 2014 Gina Fitzgerald
#prime number checker 

from math import sqrt

def prime_check(n):
    
    #2 is prime
    if n==2:
        return True
    
    #removes all even numbers which are composite 
    if n % 2==0:
        return False

    #walks odd numbers that are possible factors of n
    #looking for a hit 
    for d in range (3, floor(sqrt(n)+1), 2):
        
        #longest portion of code, has to perform division and find remainders against every number up to the candidate
        if n % d ==0:
            return False
    #no factors found, so n is prime
    return True


candidate= int(input("candidate prime?"))
if prime_check(candidate):
    print("prime")
else:
    print("composite")

