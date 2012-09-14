"""
Defines a simple Referee class so that players have someone to play with
"""

import constants as c
import player as p

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])
	
p1 = p.RandomPlayer()
p2 = p.RandomPlayer()  

def playGame():
	for i in range(10):
		playRound(p1,p2)
		
