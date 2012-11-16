"""
TOM DOVER
CS 605
FALL 2012
Ths is the Genetic player to be used in the Referee_test
"""
import constants as c
import random
import math
import StandardPlayer as sp

class GeneticPlayer(sp.Player):
	def __init__(self):
		sp.Player.__init__(self)
		self.counter=0
		#self.r=input("How many genes are in one genome? (between 5-30)..") # r = the number of genes in a single genome
		#self.r=random.randrange(5,10,1)
		#self.r=40
		self.n=input('How many different genomes? (recommend between 100-1000)..')  # n = the population of genomes
		self.population=[]
		self.strategies=[]
		for x in range(self.n):
			self.genes()
		self.plays=self.population[0]
	
	def genes(self):
		self.r=random.randrange(5,10,1)
		for i in range(self.r):
			self.strategies.append(random.choice(c.CHOICES))
		self.population.append(self.strategies)
		self.strategies=[]	
	
	def go(self):
		
		if len(self.plays)>len(self.move_history):
			self.choice=self.plays[len(self.move_history)]
		else:
			rem=len(self.move_history)% len(self.plays)
			self.choice=self.plays[rem]
		self.counter=self.counter+1
		return (self.choice)
		self.test()
				
	def test(self):
		self.altmoves=[]
		self.altmoves=[e[-1] for e in self.population]
		self.opphistory=self.move_history[-1][-1]
		o=self.opphistory
		self.scores=[]
		self.scorelist=[]
		for x in self.altmoves:
			if x == 'ROCK' and o == 'PAPER': self.scorelist.append(-1)
			elif x == 'ROCK' and o == 'SCISSORS': self.scorelist.append(1)
			elif x == 'PAPER' and o == 'SCISSORS': self.scorelist.append(-1)
			elif x == 'PAPER' and o == 'ROCK': self.scorelist.append(1)
			elif x == 'SCISSORS' and o == 'ROCK': self.scorelist.append(-1)
			elif x == 'SCISSORS' and o == 'PAPER': self.scorelist.append(1)
			else: self.scores.append(0)
		self.scorelist.append(self.scores)
		self.scores=[]
				
