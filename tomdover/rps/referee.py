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
        for i in range(100):
                playRound(p1,p2)
                print '--------------------'
        print 'player 1:', p1
        print 'player 2:', p2

players = (p.RandomPlayer(),p.StupidPlayer(),p.T4TPlayer(),p.SeqPlayer(),p.MLPlayer(),p.MyPlayer())
p1 = random.choice(players)
p1.id = 'TEST'
p2 = random.choice(players)
p2.id = 'COMPUTER'

def shuffle():
        p1 = random.choice(players)
        p2 = random.choice(players)
        p1.score_history=[]
        p2.score_history=[]
        p1.move_history=[]
        p2.move_history=[]
        print 'player 1:', p1
        print 'player 2:', p2
        
