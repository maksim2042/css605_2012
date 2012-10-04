"""
Annetta's set of players for the RPS game
"""
import constants as c
import random

class Player(object):
	
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
			print "I WON!!! ", self.myScore
		elif res[0]==0:
			print 'DRAW ', self.myScore
		else:
			self.myScore-=1
			print 'I LOST :((( ', self.myScore
		
class RandomPlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self)
	
	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice])
	
class Tit4TatPlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self)
		
	def go(self):
		choice=int(random.uniform(0,3))
		if move1 == c.ROCK:
			return c.ROCK
		elif move1 == c.PAPER:
			return c.PAPER
		elif move1 == c.SCISSORS:
			return c.SCISSORS
		else:
			return(c.CHOICES[choice])
		
class HumanPlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self)
	
	def go(self):
		move = raw_input('Enter your move; ROCK, PAPER or SCISSORS.')
		return move
	
class SequencePlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self)
		
	def go(self):	
		movesequence = [ROCK, SCISSORS, SCISSORS, ROCK, PAPER]
		x = random.choice([1,2,3,4,5])
		basemove = movesequence[x]
		if basemove == PAPER:
			return movesequence[1]
		else:
			return movesequence[x+1]
		
	