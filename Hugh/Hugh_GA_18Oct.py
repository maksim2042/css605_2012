#new genetic algorithm

import random
import matplotlib.pyplot as plt
import numpy as np
import operator

NUM_LIFESPANS = 100
NUM_PLAYERS = 10
LEN_STRAT = 20
RULES = {}
RULES = {(0,0):[0,0],(0,1):[-1,1],(0,2):[1,-1],(1,1):[0,0],(1,0):[1,-1],(1,2):[-1,1],(2,2):[0,0],(2,1):[1,-1],(2,0):[-1,1]}
OPP_STRAT = [0,0,1,1,2,2,1,1,0,0,0,0,1,1,2,2,1,1,0,0]

class player(object):
    def __init__(self,strategy):
        if strategy == 0:
            self.strategy = [random.randint(0,2) for i in range(LEN_STRAT)]
        else:
            self.strategy = strategy
        self.score = 0
    
    def play(self,opp):
        for i in range(LEN_STRAT):
            myplay = self.strategy[i]
            oppplay = opp.strategy[i]
            
            self.score += RULES[myplay,oppplay][0]
            opp.score += RULES[myplay,oppplay][1]
    
    def resetPlayerScore(self):
        self.score = 0

class opponent(object):
    def __init__(self):
        self.strategy = OPP_STRAT
        self.score = 0
    
    def resetOppScore(self):
        self.score = 0

class game(object):
    def __init__(self):
        self.players = []
        self.children = []
        self.results = []
        self.ranked = []
        self.newGenes = []
    
    def collectScore(self,player):
        self.results.append([self.players[player].strategy,self.players[player].score])
    
    def pickTopGenes(self):
        self.ranked = sorted(self.results, key=operator.itemgetter(1), reverse=True)
    
    def createChildren(self):
        split = random.randint(2,5)
        lefthalf = self.ranked[0][0][:split]
        righthalf = self.ranked[1][0][split:]
        self.children.append(lefthalf + righthalf)
        
        lefthalf = self.ranked[1][0][:split]
        righthalf = self.ranked[0][0][split:]
        self.children.append(lefthalf + righthalf)

    def resetLists(self):
        self.players = []
        self.results = []
        self.ranked = []
    
    def newBatch(self):
        self.newGenes = []
        self.newGenes.append(self.ranked[0][0])
        self.newGenes.append(self.ranked[1][0])
        self.newGenes.append(self.children[0])
        self.newGenes.append(self.children[1])


############# Main
a = game()
p2 = opponent()

for j in range(NUM_LIFESPANS):
    for i in range(NUM_PLAYERS):
        if i<len(a.newGenes):
            a.players.append(player(a.newGenes[i]))
        else:
            a.players.append(player(0))
        
    for i in range(NUM_PLAYERS):
        a.players[i].play(p2)
        a.collectScore(i)
        p2.resetOppScore()
    
    a.pickTopGenes()
    print a.ranked[0]
    a.createChildren()
    a.newBatch()
    a.resetLists()
    
        
            

