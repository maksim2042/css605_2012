'''
Created on Oct 18, 2012

@author: josemagallanes
'''

import random
import constants as c
from random import *

class Player(object):
    '''super class'''
    def __init__(self, playerID,pstrategy):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        self.playerID=playerID
        self.pstrategy=pstrategy
        print '%s : %s' % (self.playerID,self.pstrategy)  

    def getplayerID(self):
        return self.playerID

    def updatePlayersHistory(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        self.myScore+=res

class RandomPlayer(Player):
    def __init__(self, playerID,pstrategy='Random Player'):
        Player.__init__(self,playerID,'Random Player')

    def strategy(self):
        val=random.randint(0,2)
        return(c.CHOICES[val])


class StupidPlayer(Player):
    def __init__(self, playerID,pstrategy='Stupid Player'):
        Player.__init__(self,playerID,'Stupid Player')
       
    def strategy(self):
        return c.ROCK

class HumanPlayer(Player):
    def __init__(self, playerID,pstrategy='Human Player'):
        Player.__init__(self,playerID,'Human Player')
       
    def strategy(self):
        move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while not move.isdigit():
            print 'not a number...re enter, please!'
            move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while int(move) > 2:
            print 'wrong number!'
            move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        return (c.CHOICES[int(move)])
    
class tftPlayer(Player):
    def __init__(self, playerID,pstrategy='Automaton Player'):
        Player.__init__(self,playerID,'Automaton Player')
        self.start=0
    
    def strategy(self):
        if self.start==0:
            nextOwnMove=c.ROCK
            self.start+=1
        else:
            ownMove,rivalMove=self.move_history[-1]
            nextOwnMove=c.STATES[ownMove,rivalMove]
        return nextOwnMove

class SequencePlayer(Player):
    def __init__(self, playerID,pstrategy='Sequential Player'):
        Player.__init__(self,playerID,'Sequential Player')
        self.sequencePosition=0
    
    def strategy(self):
        nextOwnMove = c.SEQUENCE[self.sequencePosition]
        self.sequencePosition+=1
        if self.sequencePosition==len(c.SEQUENCE):
            self.sequencePosition=0
        return nextOwnMove

class GAPlayer(Player):
    def __init__(self, playerID,pstrategy='Adaptive Player (GA)'):
        Player.__init__(self,playerID,'Adaptive Player (GA)')
        self.sequencePosition=0
        self.GASEQUENCE=c.SEQUENCE
        self.GApopulation=[]
        self.scoreinSequence=0

    def strategy(self):
        nextOwnMove = self.GASEQUENCE[self.sequencePosition]
        self.sequencePosition+=1
        if (self.sequencePosition==len(self.GASEQUENCE)):
            self.GASEQUENCE = generateGASequence(self.GASEQUENCE,self.scoreinSequence,self.score_history)
            self.sequencePosition=0  
            self.scoreinSequence=0   
        elif len(self.score_history)>0:
            self.scoreinSequence+=self.score_history[-1]   
        return nextOwnMove
    
    def generateGASequence(lastGASequence,fitnesslastGASequence,history):
        self.GApopulation.append((fitnesslastGASequence, lastGASequence))
        if len(history)<5*len(lastGASequence):
            return [randint(0,2) for chromosome in range(len(lastGASequence))]
        else:
            cutoff = int(len(self.GApopulation)/2)
            generators = sorted(self.GApopulation)[:cutoff]
            father,mother=getParents(generators,lastGASequence)
            child1, child2 = crossover(father,mother)
            child1=mutation(child1)
            child2=mutation(child2)
            children=list(child1,child2)
            return children[randint(0,1)]
    
    def getParents(generators,sequence):
        father,mother=[],[]
        while father==mother:
            father=generators[randint(0,len(generators)-1)][1] 
            mother=generators[randint(0,len(generators)-1)][1]
        return father, mother
    
    def crossover(father,mother):
        split=randint(0,min(len(father),len(mother)))
        child1=list(father[:split]) + list(mother[split:])
        child2=list(mother[:split]) + list(father[split:])
        return child1, child2

    def mutation(child):
        mutation_prob=rand()
        for i in range(len(child)):
            if random()<mutation_prob: child[i]=randint(0,2)
