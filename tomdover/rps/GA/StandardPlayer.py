"""
TOM DOVER
CS 605
FALL 2012
Ths is the standard player
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

	def reset(self):
		self.myScore=0
		self.score_history=[]
		self.move_history=[]
			
	def result(self, res, moves):
		self.score_history.append(res)
		self.move_history.append(moves)
		if res[0]==1:
			self.myScore+=1
			#print self.id,"throws",self.choice,"and says: I WON!!! ", self.myScore
		elif res[0]==0:
			pass
			#print self.id,"throws",self.choice,"and says: IT'S A DRAW ", self.myScore
		else:
			self.myScore-=1
			#print self.id,"throws",self.choice,"and says: I LOST :((( ", self.myScore
			
