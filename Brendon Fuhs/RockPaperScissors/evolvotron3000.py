
'''
evolvotron3000.py

Brendon Fuhs
10-5-12

This is an interface and referee for running
Rock, Paper, Scissors games and evolving players.


'''


import random as r
import constants as c
import player as p
import playermachine as pm
import copy


def evolveAgainst(opponentList):

    # maybe opponentList should have been a set?
    for i in range(len(opponentList)):
        if str(type(opponentList[i]))=="<type 'classobj'>":  # I couldn't make boolean with type work
            opponentList[i] = opponentList[i]("testPlayer") # Instantiates an opponent if it's a player type
    MACHINENUM = 100 # EVEN number of competing machines at any given time.
    MACHINESIZE = 100 ### Not sure if this is initial or if it will change
    ROUNDSPERGAME = 100
    GAMENUM = 100 ### Later on, change this to legit stopping criteria

    print   "Creating ", MACHINENUM, " random machines with ", MACHINESIZE, " nodes apiece."
    #### Not sure if "nodeNum=" should be in here
    machineList = [pm.FSM(nodeNum=MACHINESIZE)]*MACHINENUM
    print " "
    gameCount = 0
    while True:
        opponent = r.choice(opponentList)
        gameCount += 1
        print  "Commencing Game number ", gameCount
        print  "Letting each machine play ", ROUNDSPERGAME, " rounds against ", opponent.getID()
        
        ##### Do I want Deep or Shallow copy?
        map( playGame,
             machineList,
             [copy.deepcopy(opponent)]*MACHINENUM,
             [ROUNDSPERGAME]*MACHINENUM )
        
        fitnessList = [machine.myScore for machine in machineList]
        fitnessList = [x+1+min(fitnessList) for x in fitnessList]

        if gameCount == GAMENUM:
            return machineList[fitnessList.index(max(fitnessList))]
        
        ############# This is printing out weird stuff
        print   " Adjusted fitness stats: Best = ", max(fitnessList), ". Worst = ", min(fitnessList),"." 
        print   "Average = ", ( sum(fitnessList)/MACHINENUM ), ". Median = ", sorted(fitnessList)[MACHINENUM/2],"." 
        print "Recombining, mutating, etc..."
        machineList = recombineMutateEtc(machineList,fitnessList)
        print " "

def recombineMutateEtc(machineList,fitnessList ): # fitnessList probably isn't necessary

    totalFitness = float(sum(fitnessList))
    reproductionList = []
    # This may not be the most efficient way of doing this.
    r.shuffle(machineList)
    while True:
        for machine in machineList:
            if r.random() < machine.myScore/totalFitness:
                reproductionList.append(machine)
        if len(reproductionList) >= len(machineList):
            break

    childList = []
    r.shuffle(reproductionList)
    for i in range(len(machineList)):
        childList += reproductionList[i*2].mateWith(reproductionList[i*2+1])
    return childList
    

def playGame(p1, p2, numRounds):
    for i in range(numRounds):
        playRound(p1,p2)
        
def playRound(p1, p2):
    move1=p1.go()
    move2=p2.go()
    result=list(c.PAYOFFS[move1,move2])
    p1.result(result,[move1,move2])
    result.reverse()
    p2.result(result,[move2,move1])


class Menu():

    def __init__(self, displayList=None, actionList=None):
        self.displayList=displayList
        self.actionList=actionList
        self.menuLength=len(actionList)
        self.actionDict = dict(zip( range(1, self.menuLength+1), actionList ))
        
    def getSelection(self):
        self.displayMenu()

        while True:
            choice = raw_input("Enter your choice here... ")
            try: choice = int(choice)
            except: continue
            if choice in self.actionDict.keys():
                return self.actionDict[choice] # Not sure yet if I want to return
                                        # or just do stuff to what it's pointing at

    def displayMenu(self):
        print " "
        for i in range(self.menuLength):
            try: print str(i+1) + ": " + self.displayList[i]
            except: print str(i+1) + ": none of the above."
        print " "
        

def playRPS():

    players = []
    playerNameList = []

    def setupAGame():
        if len(players) <= 1:
            print " "
            print "You need to have created two players before you can play!"
            print " "
            return
        print " "
        print "CHOOSE PLAYER 1"
        print " "
        p1 = playerMenu.getSelection()
        print " "
        print "CHOOSE PLAYER 2"
        print " "
        p2 = playerMenu.getSelection()
        print " "
        if p1==p2 or p1==None or p2==None:
            print "A Player can't player against itself."
            print " "
            return
        print ""
        numRounds = 1
        while True:
            choice = raw_input("Enter the number of rounds the game should last: (max 1000000)")
            try: choice = int(choice)
            except: continue
            if int(choice) in range(1,1000001):
                numRounds = choice
                break
        p1OldScore = p1.myScore
        p2OldScore = p2.myScore
        playGame(p1,p2,numRounds)
        print "The final scores are "
        print p1.getID(), ": ", p1.myScore-p1OldScore
        print p2.getID(), ": ", p2.myScore-p2OldScore

    def createPlayer():
        print " "
        print "Choose a Player Type to create"
        print " "
        newPlayer = playerTypeMenuWithEvolve.getSelection()()
        # newPlayer = newPlayer()############ DELETE THIS LINE
        if newPlayer==None:
            return
        print " "
        newName = raw_input("Enter a name for this player... ")
        print " "
        newPlayer.id = newName
        players.append(newPlayer)
        playerNameList.append(newName)

    def evolvePlayer():
        playersAndTypesMenu = Menu( playerTypeList + playerNameList,
                                    playerTypes + players + [None] )
        opponentList = []
        while True:
            print " "
            print "Choose Players to evolve against"
            opponent = playersAndTypesMenu.getSelection()
            if opponent==None:
                if len(opponentList)==0:
                    return None
                break
            opponentList.append(opponent)
            
        return evolveAgainst(opponentList)
        

    def deletePlayer():
        if len(players) == 0:
            print " "
            print "You have no players to delete!"
            print " "
            return
        print " "
        print " "
        print "Choose which player to delete."
        print " "
        obsoletePlayer = playerMenu.getSelection()
        try:
            obsPlayerIndex = players.index(obsoletePlayer)
            del playerNameList[obsPlayerIndex]
            del players[obsPlayerIndex]
        except:
            pass

    def exitRPS():
        print " " ##################### quit or exit?
        print "NO YOU CAN NEVER LEAVE"
        print "LET US PLAY FOREVER AND EVER!!"
        print " "
        

    playerTypeList = ["Random Player",
                      "Stupid Player",
                      "Sequence Player",
                      "Tit4Tat Player",
                      "Human Player",
                      "MLPlayer Player",
                      "Markov Player", ]

    # These ones will actually need to be executed because they take IDs
    playerTypes = [ p.RandomPlayer,
                    p.StupidPlayer,
                    p.SequencePlayer,
                    p.Tit4TatPlayer,
                    p.HumanPlayer,
                    p.MLPlayer,
                    p.MarkovPlayer ]


    # maybe redo these inside the functions
    playerMenu = Menu(playerNameList, players + [None])
    playerTypeMenu = Menu(playerTypeList, playerTypes)
    playerTypeMenuWithEvolve = Menu(playerTypeList + ["Evolved Player"],
                                    playerTypes + [evolvePlayer] + [None])
    
    mainMenuList = ["Play Rock, Paper, Scissors",
                    "View Players",
                    "Create or evolve a Player",
                    "Delete a Player",
                    "Quit" ]

    mainMenuActions = [ setupAGame,
                        playerMenu.displayMenu,  ###########NOT WORKING
                        createPlayer,
                        deletePlayer,
                        exitRPS ] # Make sure this works.
    
    mainMenu = Menu(mainMenuList, mainMenuActions)
    
    # Game Loop!
    while True:
        mainMenu.getSelection()()
        playerMenu = Menu(playerNameList, players + [None]) # Not 100% sure I need to do this.
          
print "Type \"playRPS()\""

###########
playRPS()
###########


