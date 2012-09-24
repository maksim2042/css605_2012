"""
Defines a simple Referee class so that players have someone to play with
"""

import constants as c
import player_x as p
import random

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])
	
def playGame():
        for i in range(1000):
                playRound(p1,p2)
                print '--------------------'
        		
p1 = p.MLPlayer()
p1.id = 'TEST'
players = (p.RandomPlayer(),p.StupidPlayer(),p.T4TPlayer(),p.SeqPlayer())
p2 = random.choice(players)
p2 = p.SeqPlayer()
p2.id = 'COMPUTER'

def shuffle():
       p2 = random.choice(players)
       print p2
