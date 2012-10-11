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
			print "I WON!!! ", self.myScore
		elif res[0]==0:
			print 'DRAW ', self.myScore
		else:
			self.myScore-=1
			print 'I LOST :((( ', self.myScore
		
class RandomPlayer(Player):

	def __init__(self, id="noID"):
		Player.__init__(self, id)
	
	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice])

class SequencePlayer(Player):

	def __init__(self, id="noID"):
		Player.__init__(self, id)
		self.counter = 0
		choice=int(random.uniform(0,3))  #Create a random move
		self.sequence = []
		self.sequencelength = 5          #Create a random sequence list of moves of a set length
		for i in range(self.sequencelength):
                        self.sequence.append(c.CHOICES[choice])
                        choice = int(random.uniform(0,3))      
                        
	def go(self):	
		if self.counter == self.sequencelength:
                        return self.sequence[self.counter]
                        self.counter = 0
		else:
                        return self.sequence[self.counter]
                        self.counter += 1

class HumanPlayer(Player):

        def __init__(self, id="noID"):
                Player.__init__(self, id)
                self.id = raw_input('Enter player name, and press return.')

        def go(self):

		move = raw_input('Enter your move, ROCK, PAPER or SCISSORS, and press return.')
		if move in c.CHOICES:
                        return move
                else:
                        move = raw_input('Bad entry, please enter ROCK, PAPER or SCISSORS and press return. ')
                        return move

class Tit4TatPlayer(Player):

        def __init__(self, id="noID"):
                Player.__init__(self, id)

        def go(self):
                choice = int(random.uniform(0,3)
                roundnumber = len(self.move_history)
                if roundnumber == 0:
                        return c.CHOICES[choice]
                else:
                    return self.move_history[roundnumber-1][1]

