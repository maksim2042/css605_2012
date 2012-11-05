"""
This class implements a very stupid simple player for the RPS game
"""
import constants as c
import sm as sm
import random as random

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
		self.seq_0 = int(random.uniform(0,3))
		self.seq_1 = int(random.uniform(0,3))
		self.seq_2 = int(random.uniform(0,3))
		self.sequence =[self.seq_0, self.seq_1, self.seq_2]

	def go(self):
		remnant = len(self.move_history) % len(self.sequence)
		choice = self.sequence[remnant]
		return (c.CHOICES[choice])

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
								 	
class FSMPlayer(Player):
	def __init__(self, id='noID'):
		super(FSMPlayer, self).__init__(id)
		self.move = {'ROCK':0, 'PAPER':1, 'SCISSORS':2}
		self.current_state = None
		self.g = input('How many genomes do you want to generate?')
		self.genomes = [ self.make_genome(10) for x in range(self.g)]
		self.move_value = self.genomes[0]
		# self.opp_move_value = []

	def make_genome(self, length):
		return [random.randint(0,2) for x in range(length)]	

	def go(self):
		# move_value = ['0','2','1','2','1','0','0','0','1','2']
		# move_value = make_genome(10) 
		#	return move_value
		if len(self.move_value) > len(self.move_history):
			choice=self.move_value[len(self.move_history)]
			return (c.CHOICES[choice])

		else:
			residual = len(self.move_history) % len(self.move_value)
			choice = self.move_value[residual]
			return (c.CHOICES[choice])
			
		# self.fit()
		
		for a in self.move_value:
			if self.current_state == None:
				self.current_state = sm.START(a)
				
			else:
				self.current_state = self.current_state(a)

		if self.current_state == None:
			print " empty string"
		elif self.current_state in sm.F:
			print " accepted.  State:",current_state.__name__
		else:
			print " not accepted.  State:",current_state.__name__		

"""
	def fit(self):
		for m in self.move_history[1][0]:
			vec = [v for k, v in self.move.iteritems() if k == m ][0]
			self.opp_move_value.append(vec)
"""

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