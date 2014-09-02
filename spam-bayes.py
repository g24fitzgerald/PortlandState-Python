#copyright (c) 2014 Gina Fitzgerald
#spam-bayes.py

#categories 
ham=0
spam=0

#with indicators
ham_i=0
spam_i=0
indicators= (ham_i + spam_i)

#without indicators
ham_ni=0
spam_ni=0
no_indicators= (ham_ni + spam_ni)

def read_data(filename):

    # Reads integer data in space delimited format 

    filedata = csv.reader(open(filename), delimiter=' ')

    data = []

    for line in filedata:

        row = [int(line[0]), int(line[1])]

        data.append(row)

    #returns list of lists of integers 

    return data

read_data(filename)

#update counters 
if row in data == [0,0]:
    ham += 1
    ham_ni +=1
    
if row in data == [0,1]:
    ham +=1
    ham_i +=1

if row in data == [1,0]:
    spam += 1
    spam_ni +=1

if row in data == [1,1]:
    spam += 1
    spam_i += 1

#probability of indicators
Pr(E)= indicators // (spam+ham)
Pr(S)= spam // (spam+ham)
Pr(E|S)= |E isect S|/|H|
Pr(S|E)= Pr(E|S) * Pr(s) / Pr(E)

#display table

print("probability of evidence given the message is Spam:", Pr(E|S))
print("Probability the message is spam given evidence:", Pr(S|E))


