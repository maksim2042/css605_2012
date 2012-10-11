
'''
evolvotron3000.py

Brendon Fuhs
10-5-12
updated 10-11-12

This is an interface and referee for running
Rock, Paper, Scissors games and evolving players.


Semi-problem: I'm copying the same already-instantiated opponents when evolving a player.
This is fixable.
'''


import random as r
import constants as c
import player as p
import playermachine as pm
import copy
import math as m

# Do I have a random seed problem?

# This returns gene material for the next round.
def recombineMutateEtc( machineList, fitnessList, meanXoverSize, xoverAltSiteProb, mutateProb ):
    MACHINENUM = len(fitnessList)
    print "Recombining, mutating, etc..."
    print " "
    reproductionList = []
    
    fitnessDict = dict(zip(machineList,fitnessList))
    # This may not be the most efficient way of doing this.
    r.shuffle(machineList)

    def fitnessSelected(machines, fitnesses): # Generator, not sure if optimally-written. Maybe should be function.
        machinesYielded = 0
        r.shuffle(machines)
        while True:
            for machine in machines:
                if r.random() < fitnesses[machine]/MACHINENUM:
                    yield machine
                machinesYielded += 1
                if machinesYielded == MACHINENUM:
                    StopIteration

    reproductionList = [machine for machine in fitnessSelected(machineList, fitnessDict)]

    newGenesList = []
    r.shuffle(reproductionList)

    ##### MAKE THIS BETTER
    for machine1,machine2 in it.izip( ifilter(lambda x: x%2, range(MACHINENUM)) ,ifilterfalse(lambda x: x%2, range(MACHINENUM) )):
        ############ NEED TO DECIDE HOW I WANT TO DO THIS
        startNodeIndex1 = r.choice(range(MACHINENUM))
        if r.random() < xoverAltSiteProb:
            startNodeIndex2 = r.choice(range(MACHINENUM))
        else:
            startNodeIndex2 = startNodeIndex1

        # Size of subtree is based on meanXoverSize
        treeNodeNum = int(min(0,max(r.gauss(meanXoverSize, MACHINENUM/6.0),MACHINENUM/2)))
        
        subTree1 = machine1.getSubTree(startNodeIndex1, treeNodeNum)
        subTree2 = machine2.getSubTree(startNodeIndex2, treeNodeNum)

        def subTreeReplace(machine,subTree,replacementSubTree): # Generator replaces subtrees by node.
            i=0
            for node in machine:
                if node==subTree[i]:
                    i+=1
                    newNode = replacementSubTree[i]
                else:
                    newNode = node
                if r.random() <= mutateProb:
                    newNode = machine.randomizeNode(newNode)
                yield newNode
        
        childGenes1=[ node for node in subTreeReplace( machine1, subTree1, subTree2 ) ]
        childGenes2=[ node for node in subTreeReplace( machine2, subTree2, subTree1 ) ]
        newGenesList.append(childGenes1)
        newGenesList.append(childGenes2)

    #### I have no idea is these garbage-collection-ish lines are necessary
    newGenesList = copy.deepcopy(newGenesList)
    del machineList
    
    return newGenesList


# This method creates a machine player that was evolved against a list of opponent types
def evolveAgainst(opponentList):
    MACHINENUM = 100 # EVEN number of competing machines at any given time.
    MACHINESIZE = 100 ### Not sure if this is initial or if it will change
    ROUNDSPERGAME = 100
    GAMENUM = 100 ### Later on, change this to legit stopping criteria
    MEANXOVERSIZE = int(0.15*MACHINENUM)
    XOVERALTSITEPROB = 0.05
    MUTATEPROB = 0.05
    
    # Generator of instantiated players from list of both player types and players
    def playersCreatedFrom(opponentList): 
        for opponent in opponentList:
            if str(type(opponent))=="<type 'type'>": #### FIGURE OUT A BETTER WAY TO CHECK THIS
                yield opponent("testPlayer") # Instantiates an opponent if it's a player type
            else:
                yield opponent
    
    opponentList = [opponent for opponent in playersCreatedFrom(opponentList)]
    # Now opponentList has playable opponents.

    print "Creating ", MACHINENUM, " random machines with ", MACHINESIZE, " nodes apiece."
    #### "nodeNum="
    machineList = [pm.FSMPlayer(nodeNum=MACHINESIZE) for i in range(MACHINENUM)] # Creates random machine players for the first time
    print " "
    gameCount = 0
    while True:
        opponent = r.choice(opponentList)
        print " "
        print "Game ", gameCount
        print "Letting each machine play ", ROUNDSPERGAME, " rounds against a copy of ", opponent.getID(), opponent
        
        ##### Do I want Deep or Shallow copy?
        map( playGame,
             machineList,
             [copy.deepcopy(opponent)]*MACHINENUM,
             [ROUNDSPERGAME]*MACHINENUM )
        
        fitnessList = [machine.myScore for machine in machineList]

        gameCount += 1
        if gameCount >= GAMENUM: # Wrap things up if that was the final set of games.
            winnerMachine = machineList[fitnessList.index(max(fitnessList))]
            print "The winning machine has a score of ", winnerMachine.myScore
            return winnerMachine
        
        maxFit = max(fitnessList)
        minFit = min(fitnessList)
        print "Fitness stats: Best = ", maxFit, ". Worst = ", minFit,"." 
        print "Average = ", ( sum(fitnessList)/MACHINENUM ), ". Median = ", sorted(fitnessList)[MACHINENUM/2],"." 
        print " "
        print "Normalizing fitness stats..."
        print " "
        ############# WILL BREAK IF maxFit==minFit
        try: fitnessList = [(x-minFit)/float(maxFit-minFit) for x in fitnessList]
        except: fitnessList = [.5]*len(fitnessList)
        assert(len(fitnessList)==len(machineList))
        assert(max(fitnessList)<=1)
        assert(min(fitnessList)>=0)
  
        newGenesList = recombineMutateEtc(machineList,fitnessList, MEANXOVERSIZE, XOVERALTSITEPROB, MUTATEPROB)
        machineList = [ FSMPlayer(nodeList=machineGene) for machineGene in newGenesList]

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


