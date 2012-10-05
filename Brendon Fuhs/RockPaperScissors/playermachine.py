'''
playermachine.py

10-5-12

'''

import constants as c
import random as r


# CSS 605 class standard (minus the chatter) for an RPS Player
# Maybe I could have just import this
class Player():
    
    def __init__(self, id="noID"):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        self.id=id

    def getID():
        return self.id
        
    def go(self):
        return c.ROCK

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
        elif res[0]==0:
            pass
        else:
            self.myScore-=1


# Finite State Machine Player
class FSM(Player):

    ######## Seems like multiple optional inputs could confuse things.
    def __init__(self, id="noID", nodeNum=1, genome=None):
        self.id=id
        self.nodeNum = nodeNum # number of states in machine
        self.nodeList = [{}]*nodeNum # This will be a list of nodes in the machine
        self.genome = genome

        if genome==None: # Randomize the machine if no genome is supplied
            self.nodeList = map(randomizeNode,self.nodeList)
        else:
            buildMachine(genome)

        self.currentNode = self.nodeList[0] # Start at 0

    def go(self):
        opponentMoved = self.move_history[-1][1]
        return respondTo(opponentMoved)

    # Randomizes the contents of a state / node
    def randomizeNode(node): # Do I need to feed this nodeNum?
        for possibleOpponentMove in node.keys():
            node[possibleOpponentMove] = { "output" =  c.CHOICES[r.randint(0,2)],
                                           "nextNode" = nodeList[r.randint(0,nodeNum)] }
        return node

    # This gets the machine's move and iterates the machine to the next state
    def respondTo(opponentMove):
        ourResponse = self.currentNode[opponentMove]
        self.currentNode = ourResponse["nextNode"]
        return ourResponse["output"]

    def buildMachine(genome):
        pass ############# Build machine based on a genome

    def getGenome():
        pass ############# I might only need to extract a genome once if I don't mutate in-house
                            # Or the randomization can happen before the building and I don't
                            # need to even worry about it.
    def mutate():
        pass ############# Do I want a mutate method?
    
    

    
