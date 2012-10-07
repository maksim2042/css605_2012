'''
playermachine.py

10-6-12

Brendon Fuhs

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

    def getID(self):
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
# 
class FSM(Player):

    ######## Seems like multiple optional inputs could confuse things.
    def __init__(self, id="noID", nodeNum=2, nodeList=None):
        Player.__init__(self, id="noID")
        self.SWAPAMOUNT = 0.1 # Size of cross-over portion, I have no idea if this is good
                                # Maybe I should make this vary between .01 and .5 randomly?
        self.MUTATIONRATE = 0.05 # I have not idea what this should be.
                                # Maybe it should start higher and decrease with time?
        self.id=id
        self.nodeList = nodeList # This will be a list of nodes in the machine

        self.nodeNum = nodeNum
        ##########
        print self.nodeNum # WHY IS ONLY ONE OF THESE PRINTING????
        ######
        
        if self.nodeList==None: # Populate a random machine if none supplied
            self.nodeList = [{}]*self.nodeNum
            self.nodeList = map(self.randomizeNode,self.nodeList)
            
        self.nodeNum = len(self.nodeList) # number of states in machine
        self.currentNode = self.nodeList[0] # Zero is start

    # Randomizes the contents of a state / node
    def randomizeNode(self,node): # Do I need to feed this nodeNum?
        for possibleOpponentMove in c.CHOICES:
            node[possibleOpponentMove] = { "output" :  c.CHOICES[r.randint(0,2)],
                                           "nextNode" : self.nodeList[r.randint(0,self.nodeNum-1)] }
        return node

    # This returns the machine's move and iterates it to the next state
    def go(self):
        if len(self.move_history)==0:
            return c.CHOICES[r.randint(0,2)]
        opponentMoved = self.move_history[-1][1]
        ourResponse = self.currentNode[opponentMoved]
        self.currentNode = ourResponse["nextNode"]
        return ourResponse["output"]

    # This reaches into another player, mixes genetic material with it,
    # applies mutation, and returns nodeLists for (ONE OR TWO???) children
    def mateWith(self,otherFSM):

        # Maybe change indices to swap to an anonymous list of two lists
        indicesToSwap = map( self.getSubTree,
                             [self.nodeList, otherFSM.nodeList],
                             [r.choice(range(self.nodeNum)), r.choice(range(otherFSM.nodeNum))],
                             [int(self.SWAPAMOUNT * min(self.nodeNum,otherFSM.nodeNum))]*2 )

        child1 = copy.deepcopy(self.nodeList) ### Do I need to deep copy these so they don't leek or get deleted??
        child2 = copy.deepcopy(otherFSM.nodeList) # Or should I shallow copy just to make the next thing work?

        for i in self.nodeNum:
            if i in indicesToSwap[0]:
                child1[i] = otherFSM.nodeList[indicesToSwap[1][i]]
            if r.random() < self.MUTATIONRATE:
                child1[i] = randomizeNode(child1[i])

        for i in otherFSM.nodeNum:
            if i in indicesToSwap[1]:
                child2[i] = self.nodeList[indicesToSwap[0][i]]
            if r.random() < self.MUTATIONRATE:
                child2[i] = randomizeNode(child2[i])
        ### I should probably be implementing mutation below the node level.
                    
        return (child1, child2)
 

    def getSubTree(self, nodeList, startNodeIndex, treeNodeNum):
        
        subTreeIndices = [] # Maybe these should be a set?

        # uses recursion to populate a list of subTreeIndices
        def depthSearch(nodeList, thisNodeIndex, searchLength):

            if searchLength <= 0:
                return
            if thisNodeIndex in subTreeIndices:    #####vvv Why would this be empty? If nodeNum=1
                nextNodeIndex = r.choice(list( set(range(self.nodeNum)) - set(subTreeIndices) ))
                depthSearch(nodeList, nextNodeIndex, searchLength)
            
            subTreeIndices.append(thisNodeIndex)
            searchLength -= 1
            
            for inputMove in sorted(c.CHOICES, key=lambda x: r.random()): # straight from Stackoverflow!
                nextNodeIndex = nodeList.index(nodeList[thisNodeIndex][inputMove]["nextNode"])
                depthSearch(nodeList, nextNodeIndex, searchLength)
                
        # uses recursion to populate a list of subTreeIndices
        def breadthSearch(nodeList, thisNodeIndex, searchLength, firstTime = True): 

            # Need to start out with this node
            if firstTime==True:
                subTreeIndices.append(thisNodeIndex)
                searchLength -= 1

            nextNodeIndices = []
                             
            for inputMove in sorted(c.CHOICES, key=lambda x: r.random()): # straight from Stackoverflow!
                if searchLength <= 0:
                    return
                nextNodeIndex = nodeList.index(nodeList[thisNodeIndex][inputMove]["nextNode"])
                if nextNodeIndex in subTreeIndices:
                    continue
                subTreeIndices.append(nextNodeIndex)
                searchLength -= 1
            
            for index in nextNodeIndices:
                breadthSearch(nodeList, nextNodeIndex, searchLength, firstTime = False)

            nextNodeIndex = r.choice(list( set(range(self.nodeNum)) - set(subTreeIndices) ))
            breadthSearch(nodeList, nextNodeIndex, searchLength)

        # Choose randomly from the two search types and return result
        r.choice((depthSearch,breadthSearch))(nodeList, startNodeIndex, treeNodeNum)
        
        return subTreeIndices
        

    
    

    
