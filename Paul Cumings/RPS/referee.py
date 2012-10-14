"""
Defines a simple Referee class so that players have someone to play with
"""

import constants as c
import player as p
import genetic as g

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])
	
def playGame():
	p1 = p.RandomPlayer(id="Max")
	p2 = g.GeneticPlayer() 
	for i in range(1000):
	  playRound(p1,p2)
		

playGame()