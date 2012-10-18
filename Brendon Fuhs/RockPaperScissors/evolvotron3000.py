
'''
evolvotron3000.py

Brendon Fuhs
10-5-12
updated 10-18-12

This is an interface and referee for running
Rock, Paper, Scissors games and evolving players.


Semi-problem: I'm copying the same already-instantiated opponents when evolving a player.
This is fixable.
'''

import itertools as it
import random as r
import constants as c
import player as p
import playermachine as pm
import copy
import math as m




# This returns gene material for the next round.
def recombineMutateEtc( machineList, fitnessList, meanXoverFraction, xOverAltSiteProb, mutateProb ):
    MACHINENUM = len(fitnessList)
    assert(MACHINENUM > 0)
    assert(MACHINENUM == len(machineList))
    assert(0 <= mutateProb <= 1)
    assert(0 <= xOverAltSiteProb <= 1)
    assert(0 <= meanXoverFraction <= 1)
    print "Recombining, mutating, etc..."
    print " "

    reproductionList = []
    while len(reproductionList) < MACHINENUM:
        i = r.choice(range(MACHINENUM))
        if r.random() < fitnessList[i]:
            reproductionList.append(machineList[i])
    r.shuffle(reproductionList)

    newGenesList = [] ############
    
    mommies, daddies = reproductionList[:MACHINENUM/2], reproductionList[MACHINENUM/2:]
    assert(len(mommies)==len(daddies)) ### Hoping there was an even number of machines

    for [mom,dad] in zip(mommies,daddies):

        startNodeIndexDad = startNodeIndexMom = r.choice(range(MACHINENUM))
        if r.random() < xOverAltSiteProb:
            startNodeIndexDad = r.choice(range(MACHINENUM))

        # Size of subtree is based on meanXoverSize
        treeNodeNum = int(max(1,min(r.gauss(meanXoverFraction*MACHINENUM, MACHINENUM/10.0),MACHINENUM/2))) ####Is this right?
### THIS STUFF DOESN'T WORK YET
#        xOverGenesFromMom = r.choice((mom.depthSearch,mom.breadthSearch))(startNodeIndexMom, treeNodeNum)
#        xOverGenesFromDad = r.choice((dad.depthSearch,dad.breadthSearch))(startNodeIndexDad, treeNodeNum)
#        def swapIndicesFor(genes,subtree): # an inefficient generator
#            for node in subtree:
#                for i in range(len(genes)):
#                    if node is genes[i]:
#                        yield i
#        swapIndicesMom = [indices for indices in swapIndicesFor(mom.nodeList, xOverGenesFromMom)]
#        swapIndicesDad = [indices for indices in swapIndicesFor(dad.nodeList, xOverGenesFromDad)]
#        for [swapIndexMom, swapIndexDad] in zip(swapIndicesMom,swapIndicesDad):
#            mom[swapIndexMom], dad[swapIndexDad] = dad[swapIndexDad], mom[swapIndexMom]
###
        mom.mutate(mutateProb)
        dad.mutate(mutateProb)
    newGenesList = [copy.deepcopy(mom.nodeList) for mom in mommies] + [copy.deepcopy(dad.nodeList) for dad in daddies]
    del machineList
    return newGenesList


# This method creates a machine player that was evolved against a list of opponent types
def evolveAgainst(opponentList):
    MACHINENUM = 100 # EVEN number of competing machines at any given time.
    MACHINESIZE = 100 ### Not sure if this is initial or if it will change
    ROUNDSPERGAME = 100
    GAMENUM = 50 ### Later on, change this to legit stopping criteria
    MEANXOVERFRACTION = 0.15
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

    machineList = [pm.FSMPlayer() for i in range(MACHINENUM)] # Creates random machine players for the first time
    for machine in machineList:
        machine.randomizeNodeList(MACHINESIZE)
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
        print "Fitness stats: Best = ", maxFit, ". Worst = ", minFit,", Total = ", sum(fitnessList) 
        print "Average = ", ( sum(fitnessList)/MACHINENUM ), ". Median = ", sorted(fitnessList)[MACHINENUM/2],"." 
        print " "
        print "Normalizing fitness stats..."
        print " "
        try: fitnessList = [(x-minFit)/float(maxFit-minFit) for x in fitnessList] # Will break if maxFit==minFit
        except: fitnessList = [.5]*len(fitnessList)
        assert(len(fitnessList)==len(machineList))
        assert(max(fitnessList)<=1)
        assert(min(fitnessList)>=0)
        newGenesList = recombineMutateEtc(machineList,fitnessList, MEANXOVERFRACTION, XOVERALTSITEPROB, MUTATEPROB)
        #machineList = [ pm.FSMPlayer(nodeList=machineGene) for machineGene in newGenesList]
        machineList = [pm.FSMPlayer() for i in range(MACHINENUM)] # Creates random machine players for the first time
        for [machine,newNodeList] in zip(machineList,newGenesList):
            machine.nodeList = newNodeList
            machine.currentNode = machine.nodeList[0] #### What's going wrong here?

        

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
        try:
            newPlayer = playerTypeMenuWithEvolve.getSelection()()
        except:
            return # This is to catch the none-of-the-above option
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
        print " " 
        print "NO YOU CAN NEVER LEAVE"
        print "LET US PLAY FOREVER AND EVER!!"
        print " "
        a = 1/0 ##################### LOLOLOLOLOLOL!!!!
        # import sys
        # sys.exit
        

    playerTypeList = ["Random Player",
                      "Stupid Player",
                      "Sequence Player",
                      "Tit4Tat Player",
                      "Human Player",
                      "MLPlayer Player",
                      "Markov Player (SLOW)", ]

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
                    "View Players (BROKEN)",
                    "Create or evolve a Player",
                    "Delete a Player",
                    "Quit (SORTA BROKEN)" ]

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


