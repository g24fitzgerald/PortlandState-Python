#copyright (c) Gina Fitzgerald 2014
#Exchange values i and j of array a

def exchange(a,i,j):

    #save value in tmp so that nothing needs to be overwritten 
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

