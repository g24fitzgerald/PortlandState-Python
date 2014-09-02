#Copyright (c) 2014 Gina Fitzgerald
#selection sort array a of n elements: read a file of integers
#and impliment selection sort

#create definitions 
def read_data(filename):

    # Reads integer data in space delimited format 

    filedata = csv.reader(open(filename), delimiter=' ')
    
    #defines the data variable 
    data = []

    for line in filedata:

        row = [int(line)]

        data.append(row)

    #returns list of lists of integers 

    return data

def exchange(a,i,j):

    #save value in tmp so that nothing needs to be overwritten 
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp


#MAIN
#call read_data function to open file
read_data(filename)

#sort
 a = data
for i in data.range(1, n):
    for j in data.range(i+1, n):
        if a[j] < a[i]:
            exchange(a, i, j)
        return
    
    return a


