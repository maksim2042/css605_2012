"""
This class implements a very stupid simple player for the RPS game
"""
import constants as c
import random
from math import *
import sm as sm

class Player(object):
	def __init__(self, id='noID'):
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

class StupidPlayer(Player):
	def __init__(self, stupid_move=None, id='noID'):
		super(StupidPlayer, self).__init__(id)
		if stupid_move is None or stupid_move not in c.CHOICES:
			self.stupid_move = c.CHOICES[int(random.uniform(0,3))]
	def go(self):	
		return self.stupid_move

class RandomPlayer(Player):
	def __init__(self, id='noID'):
		super(RandomPlayer, self).__init__(id)
	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice])	

class SeqPlayer(Player):
	def __init__(self, id='noID'):
		super(SeqPlayer, self).__init__(id)
	def go(self):
		for i in range(0, 10000, 3):
			seq_0=int(random.uniform(0,3))
			return(c.CHOICES[seq_0])
		for i in range(1, 10000, 3):
			seq_1=int(random.uniform(0,3))
			return(c.CHOICES[seq_1])
		for i in range(2, 10000, 3):
			seq_2=int(random.uniform(0,3))
			return(c.CHOICES[seq_2])
		                               
class HumanPlayer(Player):
	def __init__(self, id='noID'):
		super(HumanPlayer, self).__init__(id)
	def go(self, retries = 4, complaint = 'choose "ROCK", "PAPER", or "SCISSORS" please'):
		while True:
			Strategy = raw_input('What is your move?')
			if Strategy in ('r', 'rock', 'ROCK'):
				return 'ROCK'
			if Strategy in ('p', 'paper', 'PAPER'):
				return 'PAPER'
			if Strategy in ('s', 'scissors', 'SCISSORS'):
				return 'SCISSORS'	
			retries = retries - 1
			if retries < 0:
				raise IOError('refusenik use')
			print complaint	

class TfTPlayer(Player):
	def __init__(self, id='noID'):
		super(TfTPlayer, self).__init__(id)
	def go(self):
		if (len(self.move_history) == 0):
			choice=int(random.uniform(0,3))
			return(c.CHOICES[choice])
		else:
			return self.move_history[len(self.move_history) - 1][1]

class MLPlayer(Player):
	def __init__(self, id='noID'):
		super(MLPlayer, self).__init__(id)
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

class MarkovPlayer(Player):
	def __init__(self, id='noID'):
		super(MarkovPlayer, self).__init__(id)
	def go(self):
		Mar_list = ['ROCK', 'PAPER', 'SCISSORS']
		Mar_counter={}
		if len(self.move_history) == 0 :
			choice=int(random.uniform(0,3))
			return(c.CHOICES[choice])
		else:
			if self.score_history[len(self.score_history) - 1][0] == + 1:
				Mar_list.append(self.move_history[len(self.move_history) - 1][0])
				for strat in Mar_list:
					if strat in Mar_counter:
						Mar_counter[strat] += 1
					else:
						Mar_counter[strat] = 1
				Mar = sorted(Mar_counter, key = Mar_counter.get, reverse = True)
				return Mar[:1].pop()
			else:
				for strat in Mar_list:
					if strat in Mar_counter:
						Mar_counter[strat] += 1
					else:
						Mar_counter[strat] = 1
				Mar = sorted(Mar_counter, key = Mar_counter.get, reverse = True)
				return Mar[:1].pop()
								 		
"""
FSM debugging
"""

class FSMPlayer(Player):
	def __init__(self, id='noID'):
		super(FSMPlayer, self).__init__(id)

	def make_genome(length):
		return [randint(0,3) for x in range(length)]

	def go(self):
		move = {'ROCK':0, 'PAPER':1, 'SCISSORS':2}
		move_value = make_genome(10)
		for a in move_value:
		if current_state == None:
			choice=int(random.uniform(0,3))
			current_state = sm.START(choice)
			return(c.CHOICES[choice])
		else:
			current_state = current_state(a)
			move = {'ROCK':0, 'PAPER':1, 'SCISSORS':2}
			key = [ k for k, v in move.iteritems() if v == a ][0]
			return key


"""

		if (len(self.move_history) == 0) and state == startState:
			choice=int(random.uniform(0,3))
			return (c.CHOICES[choice])
		elif (len(self.move_history) > 0) and state != startState:
			OppMove = self.move_history[len(self.move_history) - 1][1]
			self.currentState = state
			vec = [v for k, v in self.stateList.iteritems() if k == state ][0]
			self.state_his.append(vec)
			return (OppMove, getNextValues)			
	def getNextValues(self, inp):
			OppMove = inp
			if OppMove == 'ROCK':
				nextState = 'ROCK'
			elif OppMove =='PAPER':
				nextState = 'PAPER'
			elif OppMove=='SCISSORS':
				nextState='SCISSORS'
			return (nextState, self.go(nextState))			
"""				