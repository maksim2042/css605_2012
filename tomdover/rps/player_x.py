"""
TOM DOVER
CS 605
FALL 2012
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

class AltT4TPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
		else:
			a=self.move_history[-1]
			b=a[-1]
			i=c.CHOICES.index(b)
			self.choice=c.CHOICES[i]
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
		
class SimpleSeqPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.plays=['ROCK','PAPER','SCISSORS','SCISSORS','PAPER','PAPER','ROCK']
	
	def go(self):
		if len(self.plays)>len(self.move_history):
			self.choice=self.plays[len(self.move_history)]
		else:
			rem=len(self.move_history)% len(self.plays)
			self.choice=self.plays[rem]
		return (self.choice)
		
class GeneticPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.counter=0
		self.r=10
		self.n=10
		self.population=[]
		self.strategies=[]
		for x in range(self.n):
			self.genes()
		self.plays=self.population[random.randrange(0,self.n-1)]
		
	def genes(self):
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
		self.o_player=[]
		self.temp_op=[]
		self.op_r=0
		self.dbh_r=[]
		self.op_p=0
		self.dbh_p=[]
		self.op_s=0
		self.dbh_s=[]
		self.avg_r=0
		self_avg_p=0
		self.avg_s=0
		self.last_r=0
		self.last_p=0
		self.last_s=0
		self.dist_r=0
		self.dist_p=0
		self.dist_s=0
	
	def go(self):
		if len(self.move_history)==0:
			self.choice=random.choice(c.CHOICES)
			return (self.choice)
		else:
			self.cal_rock()
			self.cal_paper()
			self.cal_scissors()
			if (self.dist_r<=self.dist_p) and (self.dist_r<=self.dist_s):
				self.choice='PAPER'
			elif (self.dist_p<=self.dist_r) and (self.dist_p<=self.dist_s):
				self.choice='SCISSORS'
			else:
				self.choice='ROCK'
			return (self.choice)
		
	def cal_rock(self):
		a=self.move_history[-1]
		self.o_player.append(a[-1])
		self.op_r=self.o_player.count('ROCK')
		self.temp_op=self.o_player
		if self.o_player.count('ROCK')==0:
			self.dist_r=100
			return (self.dist_r)
		else:
			w=self.temp_op.index('ROCK')
			self.dbh_r.append(w+1)
			while w>0 or self.op_r>1:
				self.temp_op=self.temp_op[w+1:]
				try:
					w=self.temp_op.index('ROCK')
				except:
					break
				self.dbh_r.append(w+1)
				self.op_r=self.temp_op.count('ROCK')
				l=len(self.temp_op)
				self.last_r=l
		
			self.avg_r=math.fsum(self.dbh_r)/len(self.dbh_r)
			self.last_r=len(self.temp_op)
			if self.last_r-1<self.avg_r:
				self.dist_r=self.avg_r-(self.last_r-1)
			else:
				self.dist_r=100
			return self.dist_r
	
	def cal_paper(self):
		a=self.move_history[-1]
		self.o_player.append(a[-1])
		self.op_p=self.o_player.count('PAPER')
		self.temp_op=self.o_player
		if self.o_player.count('PAPER')==0:
			self.dist_p=100
			return (self.dist_p)
		else:
			w=self.temp_op.index('PAPER')
			self.dbh_p.append(w+1)
			while w>0 or self.op_p>1:
				self.temp_op=self.temp_op[w+1:]
				try:
					w=self.temp_op.index('PAPER')
				except:
					break
			self.dbh_p.append(w+1)
			self.op_p=self.temp_op.count('PAPER')
			l=len(self.temp_op)
			self.last_p=l
			
			self.avg_p=math.fsum(self.dbh_p)/len(self.dbh_p)
			self.last_p=len(self.temp_op)
			if self.last_r-1<self.avg_p:
				self.dist_p=self.avg_p-(self.last_p-1)
			else:
				self.dist_p=100
			return self.dist_p
		
	def cal_scissors(self):
		a=self.move_history[-1]
		self.o_player.append(a[-1])
		self.op_s=self.o_player.count('SCISSORS')
		self.temp_op=self.o_player
		if self.o_player.count('SCISSORS')==0:
			self.dist_s=100
			return (self.dist_s)
		else:
			w=self.temp_op.index('SCISSORS')
			self.dbh_s.append(w+1)
			while w>0 or self.op_s>1:
				self.temp_op=self.temp_op[w+1:]
				try:
					w=self.temp_op.index('SCISSORS')
				except:
					break
			self.dbh_s.append(w+1)
			self.op_s=self.temp_op.count('SCISSORS')
			l=len(self.temp_op)
			self.last_s=l
			
			self.avg_s=math.fsum(self.dbh_s)/len(self.dbh_s)
			self.last_s=len(self.temp_op)
			if self.last_r-1<self.avg_s:
				self.dist_s=self.avg_s-(self.last_s-1)
			else:
				self.dist_s=100
			return self.dist_s

			

		
	

