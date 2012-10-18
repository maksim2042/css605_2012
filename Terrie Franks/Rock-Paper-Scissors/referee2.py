'''
Terrie Franks
CSS 605, Fall 2012
This class will implement the genetic algorithm
for the sequence player in rock-paper-scissors.
This class is a revision of the first 'referee' file.
'''

import constants as c
#import player2 as p
import genetic4 as g

def playRound(p1, p2):
    move1 = p1.go()
    move2 = p2.go()
    result = list (c.PAYOFFS[move1, move2])
    p1.result(result,[move1, move2])
    result.reverse()
    p2.result(result,[move2,move1])

def playGame():
    for i in range(10):
        playRound(p1,p2)
    
if __name__ == "__main__":
    play1 = g.SequencePlayer()
    play2 = g.GAplayer()
    
print play1
print play2


    
    
    