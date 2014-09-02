#copyright (c) 2014 Gina Fitzgerald
#gen-email.py


#define user input

n = int(input("Number of lines?"))

ham = int(input("Number of ham messages"))
ham_indicator = int(input("number of ham messages with indicator"))
ham_ni= (ham-ham_indicator)

spam = (n-ham)
print("there are", spam, "spam messages")
spam_indicator = int(input("how many spam messages have the indicator?"))
spam_ni= (spam-spam_indicator) 

def gen_email(result):
    Tuples = (A,B)

    for _ in n:
        tuple_lists = [Tuples]
    #compile list
        for _ in ham_indicator:
            tuple_lists += (0,1)
    
        for _ in ham_ni:
            tuple_lists += (0,0)
    
        
        for _ in spam_indicator:
            tuple_lists += (1,1)

        for _ in spam_ni:
            tuple_lists += (1,0)
            
    #set of tuples 
    result += [tuple_lists]

result_final = gen_email(result)
print(result_final)
