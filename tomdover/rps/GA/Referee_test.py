"""
Defines a simple Referee class so that players have someone to play with
"""

import constants as c
import Opponent as o
import Genetic as g
import random as r
import math as m
import itertools

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])
	
def playGame():
        p1Fitness=[]
        geneMean=0
        genomeId=0
        while geneMean<5:
                for x in p1.population:
                        p1.reset()
                        p2.reset()
                        p1.plays=x
                        for i in range(p1.r):
                                playRound(p1,p2)
                                print '--------------------'
                        print 'player 1:', p1.id
                        print 'player 2:', p2.id
                        print '--------------------'
                        print '--------------------'
                        if p1.myScore>0:
                                p1Fitness.append([p1.myScore,genomeId])
                                genomeId=genomeId+1
                        else:
                                genomeId=genomeId+1

                geneMean=sum([x[0] for x in p1Fitness])/float(len(p1Fitness))
                print 'generation mean score:',geneMean
                print '--------------------'
                print '--------------------'
                selection()
                newpopulation()
                selTable=[]
                
                

def selection():
        for x in p1Fitness:
                for i in range(x[0]):
                        selTable.append(x[1])
        
						
def mutation(genome1,genome2):
	p = mutation_prob
	for i in range(len(genome1)):
		if r.random()<p:
			genome1[i] = r.choice(c.CHOICES)
	for i in range(len(genome2)):
		if r.random()<p:
			genome2[i] = r.choice(c.CHOICES)
       
def newpopulation():
        newPopulation=[]
        for i in range(p1.n/2):
                mom=p1.population[r.choice(selTable)]
                dad=p1.population[r.choice(selTable)]
                split = r.randint(0,p1.r)
                child1=list(mom[:split])+list(dad[split:])				
                child2=list(dad[:split])+list(mom[split:])
                mutation(child1,child2)
                newPopulation.append(child1)
                newPopulation.append(child2)
        #print newPopulation
        #print '--------------------'
        #print '--------------------'
        print p1.population
        #print '--------------------'
        #print '--------------------'
        p1.population=newPopulation
        
        
        #print p1.population
                
mutation_prob=0.05
newPopulation=[]               
selTable=[]                
p1Fitness=[]
weights=[]
p1=g.GeneticPlayer()
p1.id = 'Genetic Algorithm'
p2=o.SimpleSeqPlayer()
p2.id = 'Opponent'
