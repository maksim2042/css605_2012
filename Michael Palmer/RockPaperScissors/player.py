"""
This class implements a very stupid simple player for the RPS game
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
		elif res[0]==0:
                        pass
		else:
			self.myScore-=1
		
class RandomPlayer(Player):
	def __init__(self):
		Player.__init__(self)
	
	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice])
