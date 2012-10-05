'''
referee.py

Took original referee and just added a scorecard and some functionality.

Usage: Type "PlayRPS()" to play Rock,Paper,Scissors

Brendon Fuhs 9-20-2012
updated 9-27-2012

Need to do something about the scorecard
'''

import constants as c
import player as p


# Referee keeps a scorecard, makes players play, and tells them their result
class Referee():
    
    def __init__(self):
        self.scorecard = {}
        self.lastResult = [0,0]
        
    def resetScore(self):
        self.scorecard = {}
        
    def playRound(self, p1, p2):
        move1=p1.go()
        # print p1.id, " plays ", move1 ############# CAN REMOVE THESE LINES
        move2=p2.go()
        # print p2.id, " plays ", move2 #############
        result=list(c.PAYOFFS[move1,move2])
        for j in range(2):
            self.lastResult[j] = self.lastResult[j] + result[j]
        p1.result(result,[move1,move2])
        self.scorecard[p1.id] = self.scorecard[p1.id] + result[0]
        result.reverse()
        p2.result(result,[move2,move1])
        self.scorecard[p2.id] = self.scorecard[p2.id] + result[0]
        
    def playGame(self, p1, p2, numRounds):
        self.lastResult = [0,0]
        for player in {p1.id,p2.id} - set(self.scorecard.keys()):
            self.scorecard[player]=0
        for i in range(numRounds):
            self.playRound(p1,p2)

        
Ref = Referee()

playerList = []
playerNameList = []

print "Type \"PlayRPS()\""


def PlayRPS():

    choice = 0

    mainMenu = ["Play Rock, Paper, Scissors",
                "View Scorecard",
                "Reset Scorecard",
                "View Players",
                "Create a Player",
                "Delete a Player",
                "Quit" ]
    
    # Game Loop!
    while True:
        print " "
        showMenu(mainMenu)
        print " "
        choice = requestChoice(7)
        if choice==1:
            setupAGame()
        elif choice==2:
            print Ref.scorecard
        elif choice==3:
            Ref.resetScore()
        elif choice==4:
            showMenu(playerNameList)
        elif choice==5:
            createPlayer()
        elif choice==6:
            deletePlayer()
        elif choice==7:
            break

# Main Menu Option 1
def setupAGame():
    if len(playerList) <= 1:
        print " "
        print "You need to have created two players before you can play!"
        print " "
        return
    print " "
    print "It's showtime."
    print " "
    showMenu(playerNameList)
    print " "
    print "Enter player one... "
    player1Choice = requestChoice(len(playerNameList))
    print " "
    print "Enter player two... "
    player2Choice = requestChoice(len(playerNameList))
    print " "
    if player2Choice == player1Choice:
        print "I'm sorry, but I cannot comprehend the sound of one hand clapping."
        print " "
        return
    print "Enter the number of rounds the game should last: (max 1000000)"
    gameLength = requestChoice(1000000)
    print " "
    print "You have chosen ", playerNameList[player1Choice-1], " and ", playerNameList[player2Choice-1]
    print " "
    Ref.playGame(playerList[player1Choice-1],playerList[player2Choice-1],gameLength)
    print "The final scores for ", playerNameList[player1Choice-1], " and ", playerNameList[player2Choice-1], " are... "
    print Ref.lastResult
    print " "
    

# Main Menu Option 5
def createPlayer():
    
    playerTypeMenu = ["Random Player",
                      "Stupid Player",
                      "Sequence Player",
                      "Tit4Tat Player",
                      "Human Player",
                      "MLPlayer Player",
                      "Markov Player",
                      "SleeperCell"]
    print " "
    id = raw_input("Enter a name for your player... ")
    print " "
    showMenu(playerTypeMenu+["Go back"])
    print " "
    print "Choose which player type you would like your player to be."
    print " "
    choice = requestChoice(len(playerTypeMenu)+1)
    print " "
    
    if choice == 9: # Escape hatch before I add an id to the name list
        return
    
    playerNameList.insert(0, id)
    
    if choice == 1:
        playerList.insert(0, p.RandomPlayer(id))
    elif choice == 2:
        playerList.insert(0, p.StupidPlayer(id))
    elif choice == 3:
        playerList.insert(0, p.SequencePlayer(id))
    elif choice == 4:
        playerList.insert(0, p.Tit4TatPlayer(id))
    elif choice == 5:
        playerList.insert(0, p.HumanPlayer(id))
    elif choice == 6:
        playerList.insert(0, p.MLPlayer(id))
    elif choice == 7:
        playerList.insert(0, p.MarkovPlayer(id))
    elif choice == 8:
        playerList.insert(0, p.SleeperCell(id))
    print " "


# Main Menu Option 6
def deletePlayer():
    if len(playerList) == 0:
        print " "
        print "You have no players to delete!"
        print " "
        return
    print " "
    showMenu(playerNameList+["Go back"])
    print " "
    print "Choose which player to delete."
    print " "
    choice = requestChoice(len(playerNameList)+1)
    if choice == len(playerNameList)+1:
        pass
    else:
        try: del Ref.scorecard[playerNameList[choice-1]]
        except: pass
        del playerList[choice-1]
        del playerNameList[choice-1]

# prints a list with numbers to the left
def showMenu(menu):
    print " "
    for i in range(len(menu)):
        print str(i+1) + ": " + menu[i]
    print " "

# gets a choice
def requestChoice(numOptions):
    while True:
        choice = raw_input("Enter your choice here... ")
        try: int(choice)
        except: continue
        if int(choice) in range(1,numOptions+1):
            print " "
            return int(choice)


