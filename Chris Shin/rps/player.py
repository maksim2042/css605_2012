"""
This class implements a very stupid simple player for the RPS game
"""
import constants as c
import random
from math import *

class Player(object):

	def __init__(self):
		self.myScore=0
		self.score_history=[]
		self.move_history=[]

	def go(self):
		return c.ROCK

	def result(self, res, moves):
		self.score_history.append(res)
		self.move_history.append(moves)
		if res[0]==1: 
			self.myScore+=1
			print "I WON!!! ", self.myScore
		elif res[0]==0:
			print 'DRAW ', self.myScore
		else:
			self.myScore-=1
			print 'I LOST :((( ', self.myScore

class StupidPlayer(Player):
	def __init__(self, stupid_move=None):
		Player.__init__(self)
		if stupid_move is None or stupid_move not in c.CHOICES:
			self.stupid_move = c.CHOICES[int(random.uniform(0,3))]

	def go(self):	
		return self.stupid_move

class RandomPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice])

class SeqPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def go(self):
		for i in range(0, 10000, 3):
			seq_move_0=int(random.uniform(0,3))
			return(c.CHOICES[seq_move_0])
		for i in range(1, 10000, 3):
			seq_move_1=int(random.uniform(0,3))
			return(c.CHOICES[seq_move_1])
		for i in range(2, 10000, 3):
			seq_move_2=int(random.uniform(0,3))
			return(c.CHOICES[seq_move_2])
		                               
class HumanPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def go(self, retries = 4, complaint = 'choose "ROCK", "PAPER", or "SCISSORS" please'):
		while True:
			move = raw_input('What is your move?')
			if move in ('r', 'rock', 'ROCK'):
				return 'ROCK'
			if move in ('p', 'paper', 'PAPER'):
				return 'PAPER'
			if move in ('s', 'scissors', 'SCISSORS'):
				return 'SCISSORS'	
			retries = retries - 1
			if retries < 0:
				raise IOError('refusenik use')
			print complaint	

class TfTPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def go(self):
		if (len(self.move_history) == 0):
			choice=int(random.uniform(0,3))
			return(c.CHOICES[choice])

		else:
			return self.move_history[len(self.move_history) - 1][1]

class MLPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def go(self):
		MLprob = {'ROCK': 1.0/3.0, 'PAPER': 1.0/3.0, 'SCISSORS': 1.0/3.0}
		m = max(MLprob.values())
		e = 0.0005
		key = [k for k, v in MLprob.iteritems() if v == m ][0]
 		if (len(self.move_history) == 0):
			choice=int(random.uniform(0,3))
			return(c.CHOICES[choice])

		else:
			if self.score_history[len(self.score_history) - 1][0] == - 1:
				if self.move_history[len(self.move_history) - 1][0] == 'ROCK':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 - e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 + (0.5 * e))
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 + (0.5 * e))
				elif self.move_history[len(self.move_history) - 1][0] == 'PAPER':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 + 0.5 * e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 - e)
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 + 0.5 * e)
				elif self.move_history[len(self.move_history) - 1][0] == 'SCISSORS':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 + 0.5 * e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 + 0.5 * e)
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 - e)
			elif self.score_history[len(self.score_history) - 1][0] == 1:
				if self.move_history[len(self.move_history) - 1][0] == 'ROCK':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 + e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 - 0.5 * e)
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 - 0.5 * e)
				elif self.move_history[len(self.move_history) - 1][0] == 'PAPER':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 - 0.5 * e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 + e)
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 - 0.5 * e)
				elif self.move_history[len(self.move_history) - 1][0] == 'SCISSORS':
					MLprob['ROCK'] = MLprob['ROCK'] * (1 - 0.5 * e)
					MLprob['PAPER'] = MLprob['PAPER'] * (1 - 0.5 * e)
					MLprob['SCISSORS'] = MLprob['SCISSORS'] * (1 + e)
			return key
