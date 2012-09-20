'''
Created on Sep 19, 2012
@author: josemagallanes

YANKENPO IS THE NAME OF THIS GAME IN PERU!!!!!!!
'''
import constants as c
import player as p



def yankenpoRound(p1, p2):
    move1=p1.go()
    move2=p2.go()
    choice=list(c.PAYOFFS[move1,move2])
    #print 'Player 1:',move1, result[0], ', Player 2:', move2, result[1]
    p1.result(choice,[move1,move2])
    print choice
    choice.reverse()
    print choice
    #print [move2,move1]
    p2.result(choice,[move2,move1])

def yankenpo():
    for c in range(3):
        print "YANKENPO!"
        yankenpoRound(p1,p2)
        p1.history()
        p2.history()
        

p1 = p.RandomPlayer('Player 1')
p2 = p.Player('Player 2')   

yankenpo()
