"""
Defines a simple Referee class so that players have someone to play with
"""
import constants as c
import player as p
import random as random
from math import *

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])

def playGame():
	for i in range(10):
		playRound(p1, p2)

def GG():
	for i in range(10):
		playGame()


"""
Trying
"""

def playGame():
	for i in range(10):
		playRound(p1, p2)
	oppmove = [e[0] for e in p2.move_history]	



		
