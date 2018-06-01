#import lets us connect to different module. sys is a module that comes with python and flags errors
import sys #sys leets you look at the system

#argv takes the arguments
ProgramName = sys.argv[0] #argv[0] gives the program name afternoon.py

if len(sys.argv) < 2:
    print "Usage python " + ProgramName + "[List of Names]"
else:
    for Interation in range(10): #Iteration gets the value
        for Name in sys.argv[1:]:
            if Name.lower() == 'stop':
                break
            if Name.lower() == 'ignore':
                continue
            print 'hello ' + Name
        print "Number of iteration is %i" %(Interation + 1 )
