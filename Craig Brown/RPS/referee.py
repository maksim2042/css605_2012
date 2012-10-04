'''
Craig Brown
CSS 605
Fall 2012

Rock, Paper, Scissors
Referee Class
'''

import constants as c
import player as p

def playRound(p1,p2):
    move1=p1.go()
    move2=p2.go()
    result=list(c.PAYOFFS[move1,move2])
    p1.result(result,[move1,move2])
    result.reverse()
    p2.result(result,[move2,move1])
    
p1 = p.SequencePlayer()
p2 = p.RandomPlayer()  
    
def playGame():    
    for i in range(100):
        playRound(p1,p2)