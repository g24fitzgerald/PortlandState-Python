# Copyright (c) 2014 Gina Fitzgerald
# Coinwar Game-Portland State University - New Beginningsprogram - developed by Bart Massey
#You need not write your own tests for this game. Instead, I have supplied 10 tests that your program should pass elsewhere. Each test consists of an initial state and an expected game result. To run these tests, you will have to write your program so that it can optionally take a given initial state rather than randomly generating one itself, either from the test file or by typing it in by hand.
#Each team has 1 army of 5 coins flipped on each turn.
#Round of play: The players compare the first coins in their armies.

#H beats T, so if the coins mismatch, the player with H captures the coin of the player with T, and puts the T and H at the end of their Army in that order.

#In addition, the player with H then captures the Prisoners of the player with T—see below—and places the opposing Prisoners and then their own Prisoners in order at the end of their Army.

#If the coins are the same, each player puts the matched coin at the end of their Prisoners. Players with coins still in their Army then put the first remaining coin in their Army at the end of their sequence of Prisoners.

#Victory conditions: At any point, if either player has no Army, the game is immediately over.

#If only one player has an Army, that player wins. Otherwise, both players must have no Army.If one player has more H coins than the other in their Prisoners, that player wins.Otherwise, the game is a tie.


from random import choice
from tkinter import *

class CoinWar(Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.grid()

       
        # Intro
        self.title = Label(self, text = "Ready to play Coin War?")
        self.title.grid(column = 1)
        Label(self, text = "").grid(row = 1, column = 0)
        self.select = Label(self, text = "Select your method to create teams")
        self.select.grid(row = 2, column = 0)
        
        # User team generation options
        self.random = Button(self, text ="Random", command = self.do_random)
        self.random.grid(row = 3, column = 0)

        self.text = Button(self, text = "Text File", command = self.do_text)
        self.text.grid(row = 4, column = 0)
        Label(self, text ="File name:").grid(row = 4, column = 1, sticky = E)
        self.text_box = Entry(self, width = 7)
        self.text_box.grid(row = 4, column = 2)

        self.usr_input = Button(self, text = "Manual", command = self.do_input)
        self.usr_input.grid(row = 5, column = 0)
        Label(self, text = "Player 1:").grid(row = 6, column = 1, sticky = W)
        Label(self, text = "Player 2:").grid(row = 6, column = 2, sticky = W)

        self.one_box = Entry(self, width = 7)
        self.one_box.grid(row = 5, column = 1, sticky = W)
        self.two_box = Entry(self, width = 7)
        self.two_box.grid(row = 5, column = 2, sticky = W)

        # The Display
        Label(self, text = "").grid(row = 6, column = 0)

        Label(self, text = "Player 1 -").grid(row = 7, column = 0, sticky = E)
        Label(self, text = "Player 2 -").grid(row = 8, column = 0, sticky = E)

        self.army1 = Label(self, text = "Army:")
        self.army1.grid(row = 7, column = 1, sticky = W)
        self.army2 = Label(self, text = "Army:")
        self.army2.grid(row = 8, column = 1, sticky = W)

        Label(self, text = "Prisoners:").grid(row = 7, column = 2, sticky = W)
        self.prison1 = Label(self)
        self.prison1.grid(row = 7, column = 3, sticky = W)

        Label(self, text = "Prisoners:").grid(row = 8, column = 2, sticky = W)
        self.prison2 = Label(self)
        self.prison2.grid(row = 8, column = 3, sticky = W)
 
        # Next Button and winner
        Label(self, text = "").grid(row = 9, column = 0)
        self.next_turn = Button(self, text = "Next Flip", command = self.do_next_turn)
        self.next_turn.grid(row = 10, column = 1)

        Label(self, text = "").grid(row = 11, column = 0)
        self.winner = Label(self)
        self.winner.grid(row = 12, column = 1, columnspan = 2)
        

    def random_team(self):
        # Select random team
        team = []
        coin = ["H", "T"]
        for _ in range(5):
            i = choice(coin)
            team.append(i)
        return team

    def do_random(self):
        # Make global variables
        global army1
        global army2
        global prison1
        global prison2
        
        # Generate teams
        army1 = self.random_team()
        army2 = self.random_team()
        prison1 = []
        prison2 = []
        
        # Print and reset original values
        self.army1["text"] = "Army: " + "".join(army1)
        self.army2["text"] = "Army: " + "".join(army2)
        self.prison1["text"] = ""
        self.prison2["text"] = ""
        self.winner["text"] = ""
        self.next_turn["text"] = "Next Turn"

    def do_input(self):
        # Make global variables
        global army1
        global army2
        global prison1
        global prison2
        
        army1 = self.one_box.get()
        army2 = self.two_box.get()
        prison1 = []
        prison2 = []

        good = True
        
        # Get correct input
        if len(army1) == 5 and len(army2) == 5:
            for i in army1:
                if i not in ["H", "T"]:
                   good = False
                   self.winner["text"] = "Entry must be in the form 'H' or 'T'"
                
            
            for i in army2:
                if i not in ["H", "T"]:
                    good = False
                    self.winner["text"] = "Entry must be in the form 'H' or 'T'"

        else:
            good = False
            self.winner["text"] = "You must use 5 letters"


        if good:
            
            army1 = "".join(army1)
            army2 = "".join(army2)

            # Print and reset original values
            self.army1["text"] = "Army: " + "".join(army1)
            self.army2["text"] = "Army: " + "".join(army2)
            self.prison1["text"] = ""
            self.prison2["text"] = ""
            self.winner["text"] = ""
            self.next_turn["text"] = "Next Turn"                           


        # Put back into a list
        army1 = list(army1)
        army2 = list(army2)

        # Clear entry boxes
        self.one_box.delete(0, END)
        self.two_box.delete(0, END)


    # get army assignments from file

    def do_text(self):

        # Make global values to be used with other methods
        global army1
        global army2
        global prison1
        global prison2

        # Pull info from file
        file_name = self.text_box.get()
        txt_file = open(file_name, "r")
        
        # Read lines to make armies
        army1 = list(txt_file.readline().rstrip())
        army2 = list(txt_file.readline().rstrip()) 
        
        
        
        prison1 = []
        prison2 = []

        # Print and reset original values
        self.army1["text"] = "Army: " + "".join(army1)
        self.army2["text"] = "Army: " + "".join(army2)
        self.prison1["text"] = ""
        self.prison2["text"] = ""
        self.winner["text"] = ""
        self.next_turn["text"] = "Next Turn"


        # Clear entry text box
        self.text_box.delete(0, END)
        
    def do_next_turn(self):
        
        # Game loop:1 round 
        if len(army1) > 0 and len(army2) > 0:
            if army1[0] == "H" and army2[0] == "T":
                army1.extend(["T", "H"])
                army1.extend(prison2)
                army1.extend(prison1)        
                del army1[0], army2[0], prison1[:], prison2[:]

            elif army1[0] == "T" and army2[0] == "H":
                army2.extend(["T", "H"])
                army2.extend(prison1)
                army2.extend(prison2)        
                del army1[0], army2[0], prison1[:], prison2[:]
            else:
                prison1.append(army1[0])
                prison2.append(army2[0])
                del army1[0], army2[0]
                if army1 and army2:
                    prison1.append(army1[0])
                    prison2.append(army2[0])
                    del army1[0], army2[0]

            # Print results after each turn
            self.army1["text"] = "Army: " + "".join(army1)
            self.army2["text"] = "Army: " + "".join(army2)
            self.prison1["text"] = "".join(prison1)
            self.prison2["text"] = "".join(prison2)



        # Display Winner 
        if len(army1) == 0 or len(army2) == 0:
            if len(army2) > len(army1):
                self.winner["text"] = "Player 2 is the winner!"
            elif len(army1) > len(army2):
                self.winner["text"] = "Player 1 wins!"
            elif prison1.count("H") > prison2.count("H"):
                self.winner["text"] = "Player 1 is the winner"
            elif prison2.count("H") > prison1.count("H"):
                self.winner["text"] = "Player 2 is the winner"
            else:
                self.winner["text"] = "We have a Tie!"
            
            self.next_turn["text"] = "Game Over"

# Start the app
root = Tk()
root.title("Coin War")
root.geometry("600x350")

app = CoinWar(root)
root.mainloop()
