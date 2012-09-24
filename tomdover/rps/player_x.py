"""
This class implements a very stupid simple player for the RPS game
"""
import constants as c
import random
import math

class Player(object):

	def __init__(self,id='noID'):
		self.myScore=0
		self.score_history=[]
		self.move_history=[]
		self.id = id
						
	def getID():
		return self.id	
	
	def go(self):
		self.choice="NA"
		return(self.choice)
			
	def result(self, res, moves):
		self.score_history.append(res)
		self.move_history.append(moves)
		if res[0]==1:
			self.myScore+=1
			print self.id,"throws",self.choice,"and says: I WON!!! ", self.myScore
		elif res[0]==0:
			print self.id,"throws",self.choice,"and says: IT'S A DRAW ", self.myScore
		else:
			self.myScore-=1
			print self.id,"throws",self.choice,"and says: I LOST :((( ", self.myScore
			
class RandomPlayer(Player):
	
	def __init__(self):
		Player.__init__(self)
				
	def go(self):
		self.choice=random.choice(c.CHOICES)
		return(self.choice)
				
class StupidPlayer(Player):
	
	def __init__(self):
		Player.__init__(self)
				
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
		else:
			self.choice=self.choice
		return(self.choice)

class ManualPlayer(Player):
	
	def __init___(self):
		Player.__init__(self)
	
	def go(self):
		self.choice = raw_input('What would you like to throw?')
		while self.choice != "ROCK" and self.choice != "PAPER" and self.choice != "SCISSORS":
			self.choice = raw_input ("Oops!  Your answer needs to be 'ROCK' or 'PAPER' or 'SCISSORS':")
		return(self.choice)
		
class T4TPlayer(Player):
	
	def __init__(self):
		Player.__init__(self)
		self.CHOICES=('PAPER', 'SCISSORS', 'ROCK')
		
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
		else:
			a=self.move_history[-1]
			b=a[-1]
			i=c.CHOICES.index(b)
			self.choice=self.CHOICES[i]
		return (self.choice)
		
class SeqPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.plays=[]
		self.r=random.randrange(10,500,1)
		for i in range(self.r):
			self.plays.append(random.choice(c.CHOICES))
				
	def go(self):
		if len(self.plays)>len(self.move_history):
			self.choice=self.plays[len(self.move_history)]
		else:
			rem=len(self.move_history)% len(self.plays)
			self.choice=self.plays[rem]
		return (self.choice)

class MLPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.CHOICES=('PAPER', 'SCISSORS', 'ROCK')
		self.other_player=[]
		self.op_rock=0
		self.op_paper=0
		self.op_scissors=0
				
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
		else:
			a=self.move_history[-1]
			self.other_player.append(a[-1])
			self.op_rock=self.other_player.count('ROCK')
			self.op_paper=self.other_player.count('PAPER')
			self.op_scissors=self.other_player.count('SCISSORS')
			op=[self.op_rock,self.op_paper,self.op_scissors]
			i=op.index(max(op))
			self.choice=self.CHOICES[i]
		return (self.choice)
		
class MyPlayer(Player):

	def __init__(self):
		Player.__init__(self)
		self.CHOICES=('PAPER','SCISSORS','ROCK')
		self.other_player=[]
		self.temp_other_player=[]
		self.op_rock=0
		self.dbh_rock=[]
		self.op_paper=0
		self.dbh_paper=[]
		self.op_scissors=0
		self.dbh_scissors=[]
	
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
		else:
			cal_rock()
			cal_paper()
			cal_scissors()
		
	def cal_rock():
		a=self.move_history[-1]
		self.other_player.append(a[-1])
		self.op_rock=self.other_player.count('ROCK')
		self.temp_other_player=self.other_player
		w=self.temp_other_player.index('ROCK')
		self.dbh_rock.append(w+1)
			
		while w>0 or self.op_rock>1:
			self.temp_other_player=self.temp_other_player[w+1:]
			w=self.temp_other_player.index('ROCK')
			self.dbh_rock.append(w+1)
			self.op_rock=self.temp_other_player.count('ROCK')
		
		avg_rock=math.fsum(self.dbh_rock)/len(self.dbh_rock)
		return avg_rock
	
	def cal_paper():
		a=self.move_history[-1]
		self.other_player.append(a[-1])
		self.op_paper=self.other_player.count('PAPER')
		self.temp_other_player=self.other_player
		w=self.temp_other_player.index('PAPER')
		self.dbh_paper.append(w+1)
			
		while w>0 or self.op_paper>1:
			self.temp_other_player=self.temp_other_player[w+1:]
			w=self.temp_other_player.index('PAPER')
			self.dbh_paper.append(w+1)
			self.op_paper=self.temp_other_player.count('PAPER')
		
		avg_paper=math.fsum(self.dbh_paper)/len(self.dbh_paper)
		return avg_paper
		
	def cal_scissors():
		a=self.move_history[-1]
		self.other_player.append(a[-1])
		self.op_scissors=self.other_player.count('SCISSORS')
		self.temp_other_player=self.other_player
		w=self.temp_other_player.index('SCISSORS')
		self.dbh_scissors.append(w+1)
			
		while w>0 or self.op_scissors>1:
			self.temp_other_player=self.temp_other_player[w+1:]
			w=self.temp_other_player.index('SCISSORS')
			self.dbh_scissors.append(w+1)
			self.op_scissors=self.temp_other_player.count('SCISSORS')
		
		avg_scissors=math.fsum(self.dbh_scissors)/len(self.dbh_scissors)
		return avg_scissors
