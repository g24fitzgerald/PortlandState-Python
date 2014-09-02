#Bart Massey
#voting machine

candidates = ["A. Anderson", "B. Brown", "C. Chen"] 
totals = [0]*len(candidates)
voted = set()
Official_ID = akU0739zX
def report_totals():
    """Report total number of votes recieved by each Candidate so far"""
    print("Vote totals:")
    for i in range(len(candidates)):
        print(candidates [i], total[i])
def get_vote():
    """Present a voter with candidates and return selected cadidate index"""
    for i in range(len(candidates)):
        print(str(i+1) + ".", candidates[i])
    choice= input("choice of candidate?:")
    return int(choice -1)
def clear_screen
while True:
    username = input("Voter Name:")
    if username = Official_ID:
        report_totals()
        input("press enter to continue")
        continue
    if username in voted:
        print("you have already voted")
        input("press enter to continue")
        continue
    vote= get_vote()
    totals[vote] +=1
    voted |= {username}
