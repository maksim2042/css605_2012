'''
playermachine.py

10-6-12
updated 10-18-12

Brendon Fuhs

'''

import constants as c
import random as r
import Queue as q

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
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.nodeList = [{}]
        self.currentNode = self.nodeList[0]

    # Randomizes the states/nodes
    def randomizeNodeList(self, nodeNum):
        self.nodeList = [{}]*nodeNum
        self.nodeList = map(self.randomizeNode,self.nodeList)
        self.currentNode = self.nodeList[0]

    # Randomizes the contents of a state / node
    def randomizeNode(self, node):
        nodeNum = len(self.nodeList)
        for opponentMove in c.CHOICES:
            node[opponentMove] = { "output" :  c.CHOICES[r.randint(0,2)],
                                   "nextNode" : self.nodeList[r.randint(0,nodeNum-1)] }
        return node

    # Responds a move and iterates the machine forward to the next state/node
    def respondTo(self,opponentMove):
        ourResponse = self.currentNode[opponentMove]
        self.currentNode = ourResponse["nextNode"]
        return ourResponse["output"]

    # Replaces Player's "go" method to get the FSMPlayer's move
    def go(self): 
        if len(self.move_history)==0:
            return c.CHOICES[r.randint(0,2)]
        else:
            return self.respondTo(self.move_history[-1][1])

    # checks to see if the object itself is in a collection
    # There is probably a slicker way of doing this
    def isIn(self, a, collection):
        for b in collection:
            if a is b:
                return True
        return False

    ### UNUSED
    # generates an iterator for objects that are actually in a collection
    def thingThatIsIn(self, a, collection):
        for b in collection:
            if a is b:
                yield a

    # Gets a subtree using depth search. Probably not the most efficient way of doing this.
    def getDepthTree(self, thisNodeIndex,treeNodeNum):
        nodeStack = [] 
        subTree = []
        nodeNum = len(self.nodeList)
        thisNode=self.nodeList[thisNodeIndex]
        nodeStack.append(thisNode)
        while True:
            thisNode = nodeStack[-1]
            subTree.append(thisNode)
            if len(subTree)==treeNodeNum:
                return subTree
            adjacentNodes = [ thisNode[inputMove]["output"] for inputMove in c.CHOICES ]
            r.shuffle(adjacentNodes)
            
            didWeStack = False
            for node in adjacentNodes:
                if not self.isIn(connectedNode, subTree):
                    nodeStack.append(thisNode)
                    didWeStack = True
                    break
            if didWeStack==FALSE:
                nodeStack.pop()
            if len(nodeStack)==0:
                nextNode = r.choice([node for node in self.nodeList if not self.isIn(node,subTree)])
                nodeStack.append(nextNode) ###### Slightly nervous about above line        
            
    def getBreadthTree(self, thisNodeIndex,treeNodeNum):
        nodeQueue=q.Queue()
        subTree = []
        nodeNum = len(self.nodeList)
        thisNode=self.nodeList[thisNodeIndex]
            
        while True:
            subTree.append(thisNode)
            nodeQueue.put(thisNode)
            adjacentNodes = [ thisNode[inputMove]["output"] for inputMove in c.CHOICES ]
            for node in adjaacentNodes:
                if (node in self.nodeList and not self.isIn(node,subTree)):
                    subTree.append(node)
                    if len(subTree)==treeNodeNum:
                        return subTree
                    nodeQueue.put(node)
            if nodeQueue.empty():
                thisNode = r.choice([node for node in self.nodeList if not self.isIn(node,subTree)])
            else: ######
                thisNode = nodeQueue.pop()

    def mutate(self, prob):
        assert(0<=prob<=1)
        for node in self.nodeList:
            for inputMove in node:
                if r.random < prob:
                    node[inputMove]["output"] = c.CHOICES[r.randint(0,2)]
                if r.random < prob:
                    node[inputMove]["nextNode"] = self.nodeList[r.randint(0,nodeNum-1)]

