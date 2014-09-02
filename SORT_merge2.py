#copyright (c) 2014 Gina Fitzgerald 
#mergesort: 
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

def merge(l1, l2):
    r = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            r += [l1[0]]
            l1 = l1[1:]
        else:
            r += [l2[0]]
            l2 = l2[1:]
        return r + l1 + l2

def mergesort(l):
    if len(l) <2:
        return 1
    j = len(l) // 2
    l1 = mergesort(l[:j])  
    l2 = mergesort(l[j:])
    return merge(l1, l2)

#tests
def test():
    a = []
    for _ in range(randrange(20)):
        a.append(randrange(100))
    assert mergesort(a) == sorted(a)   #if the result of our mergesortfunction
                                        #is equivalent to python's sorted function
                                        #we pass and exception not raised
    #random tests
    print("running tests") 
    for _ in range(1000):
        test() 
