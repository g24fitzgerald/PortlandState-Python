                                                
# Number of participants
m = int(input("Number of people? "))

# Team size
n = int(input("Number of people per team? "))


# Set up random
import random

# Given a list of participants, return
# teams as a list of lists of participants

def make_teams(participants):
    # Set up counts and accumulator
    teams = []
    l = len(participants)
    residue = l % n

    # Loop over teams
    for _ in range(len(participants) // n):
        # Set up accumulator
        members = []
        # Check for an extra person that needs a team
        team_size = n
        if residue > 0:
            team_size += 1
            residue -= 1
        # Loop over team members
        for _ in range(team_size):
            i = random.randrange(len(participants))
            members += [participants[i]]
            del participants[i]

        # Remember the new team
        teams += [members]

    return teams

# Produce and print the teams
teams = make_teams(list(range(m)))
for t in teams:
    print(*t)
