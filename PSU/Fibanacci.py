#Copyright 2014 Fitzgerald 
#Fibanacci 


def F(n):
    if n<2:
        return 1
    return (F(n-1) +F(n-2))

print(F(5))      

       
