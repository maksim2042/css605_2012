'''
playermachine.py

10-6-12
updated 10-10-12

Brendon Fuhs

'''

import constants as c
import random as r
# import Queue as q
# import itertools as it


# CSS 605 class standard (minus the chatter) for an RPS Player
# Maybe I could have just imported this
class Player(object):
    
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


class FSMPlayer(Player):
    def __init__(self, id="noID", nodeNum=None, nodeList=None):
        Player.__init__(self, id="noID")
        self.id=id
        self._nodeNum_ = nodeNum
        self.nodeList = nodeList
        if self._nodeNum_==None:
            self._nodeNum_ = len(nodeList)
        else:
            self.nodeList = [{}]*self._nodeNum_
            self.nodeList = map(self.randomizeNode,self.nodeList)
        # This might break if both or none of nodeNum and nodeList are supplied
        
        # Nodes are a dict of dicts.
        # RPS input keys for dicts with keys "output" and "nextNode" 

        self.currentNode = self.nodeList[0] # Set start to node zero

    # Randomizes the contents of a state / node
    def randomizeNode(self,node): # Do I need to feed this nodeNum?
        for opponentMove in c.CHOICES:
            node[opponentMove] = { "output" :  c.CHOICES[r.randint(0,2)],
                                    "nextNode" : self.nodeList[r.randint(0,self._nodeNum_-1)] }
        return node

    # responds to a move and iterates the machine forward
    def respondTo(self,opponentMove):
        ourResponse = self.currentNode[opponentMove]
        self.currentNode = ourResponse["nextNode"]
        return ourResponse["output"]

    # Gets a subTree
    def getSubTree(self, startNodeIndex, treeNodeNum):
        startNode = self.nodeList[startNodeIndex]
        subTree = []

        # recursive depth search to get subTree
        def depthSearch(thisNode, searchLength):

            if searchLength <= 0:
                return
            if thisNode in subTree:    #####vvv Why would this be empty? If nodeNum=1
                nextNode = r.choice([node for node in self.nodeList if node not in subTree])
                depthSearch(nextNode, searchLength)
            
            subTree.append(thisNode)
            searchLength -= 1
            
            for inputMove in sorted(c.CHOICES, key=lambda x: r.random()):
                nextNode = thisNode[inputMove]["nextNode"]
                depthSearch(nextNode, searchLength)
                
        # recursive breadth search to get subTree
        def breadthSearch(thisNode, searchLength, firstTime = True): 

            # Need to start out with this node
            if firstTime==True:
                subTree.append(thisNode)
                searchLength -= 1

            nextNodesList = []
                             
            for inputMove in sorted(c.CHOICES, key=lambda x: r.random()):
                if searchLength <= 0:
                    return
                nextNode = thisNode[inputMove]["nextNode"]
                if nextNode in subTree:
                    continue
                nextNodesList.append(nextNode)
                subTreeIndices.append(nextNode)
                searchLength -= 1

            for nextNode in nextNodesList:
                breadthSearch(nextNode, searchLength, firstTime = False)

            nextNode = r.choice([node for node in self.nodeList if node not in subTree])
            breadthSearch(nextNode, searchLength)

        # Choose randomly from the two search types and return result
        r.choice((depthSearch,breadthSearch))(nodeList, startNode, treeNodeNum)
        return subTree

    def go(self):
        if len(self.move_history)==0:
            return c.CHOICES[r.randint(0,2)]
        else:
            return self.respondTo(self.move_history[-1][1])

'''
class FSMPlayer(Player): # Woo multiple inheritance. I have no idea what I'm doing.
    #def __init__(self, id="noID", nodeNum=None, nodeList=None):
    #    Player.__init__(self, id=id)
    #    FSM.__init__(self, nodeNum=nodeNum, nodeList=nodeList)
        ################ Do I need more?
    def __init__(self, id="noID", nodeNum=None, nodeList=None):
        super(FSMPlayer, self).__init__(id="noID", nodeNum=None, nodeList=None)

    
    def go(self):
        if len(self.move_history)==0:
            return c.CHOICES[r.randint(0,2)]
        else:
            return respondTo(self.move_history[-1][1])



# Finite State Machine Player
# 
class FSM(Player):

    ######## Seems like multiple optional inputs could confuse things.
    def __init__(self, id="noID", nodeNum=2, nodeList=None):
        Player.__init__(self, id="noID")
        self.SWAPAMOUNT = 0.1 # Size of cross-over portion; should make this vary between .01 and .5 randomly?
        self.MUTATIONRATE = 0.05 # Mutation probability for a node. 
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
'''
