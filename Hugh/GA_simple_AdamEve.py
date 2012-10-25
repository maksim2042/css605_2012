#new genetic algorithm

import random
import matplotlib.pyplot as plt
import numpy as np
import operator

NUM_GAMES = 100 #top level - complete games
NUM_LIFESPANS = 75 #how many generations to test
NUM_PLAYERS = 2 #adam and eve
LEN_STRAT = 20 #how many moves in a strategy
RULES = {}
RULES = {(0,0):[0,0],(0,1):[-1,1],(0,2):[1,-1],(1,1):[0,0],(1,0):[1,-1],(1,2):[-1,1],(2,2):[0,0],(2,1):[1,-1],(2,0):[-1,1]}
OPP_STRAT = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1] #this is a 20-move strategy

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
        self.fitness = [0] #the top score each round
        self.fitness2 = [0] #the time between a score improvement
    
    def collectScore(self,player):
        self.results.append([self.players[player].strategy,self.players[player].score])
    
    def pickTopGenes(self):
        self.ranked = []
        self.ranked = sorted(self.results, key=operator.itemgetter(1), reverse=True)
    
    def createChildren(self):
        split = random.randint(2,18)
        lefthalf = self.ranked[0][0][:split]
        righthalf = self.ranked[1][0][split:]
        self.players.append(player(lefthalf+righthalf))
        
        lefthalf = self.ranked[1][0][:split]
        righthalf = self.ranked[0][0][split:]
        self.players.append(player(lefthalf+righthalf))

    def resetLists(self):
        self.results = []
    
    def collectStats(self,round):
        #collect all the scores
        self.fitness.append(self.ranked[0][1])
        #if self.fitness[-1] < self.ranked[0][1]:
            #collect the times between improvements
         #   self.fitness2.append(round-self.fitness2[-1])

    def plotData(self):
        #subplot: numrows, numcols, fignum: 1 to numrows*numcols
        plt.figure(1)

        plt.subplot(2,1,1)
        plt.xlabel('Round',fontsize = 10, color = 'blue')
        plt.ylabel('Top Fitness',fontsize = 10, color = 'blue')
        plt.title('Fitness Improvements')    
        #plt.hist(outcomes,20)
        plt.plot(self.fitness)
        
        plt.subplot(2,1,2)
        plt.xlabel('Improvement',fontsize = 10, color = 'blue')
        plt.ylabel('Interval',fontsize = 10, color = 'blue')
        plt.title('Time Between Fitness Improvements')
        plt.plot(self.fitness2)
        
        #plt.show()

############# Main

for x in range(NUM_GAMES):
    a = game()
    p2 = opponent()
    for i in range(NUM_PLAYERS): #create adam and eve
        a.players.append(player(0))
        
    for j in range(NUM_LIFESPANS):
        for i in range(len(a.players)):
            a.players[i].play(p2)
            a.collectScore(i)
            a.players[i].resetPlayerScore()
            p2.resetOppScore()
        #print a.ranked
        #print a.fitness
        a.pickTopGenes() #ID the top 2 genes
        a.collectStats(j)
        a.createChildren() #creates new children from genes and adds to list
        a.resetLists()

    a.plotData()
plt.show()
    
        
            

