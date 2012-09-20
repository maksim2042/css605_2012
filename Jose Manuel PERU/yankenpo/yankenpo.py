'''
Created on Sep 19, 2012
@author: josemagallanes
YANKENPO IS THE NAME OF THIS GAME IN PERU!!!!!!!

THE FIRST ONE WHO GETS 3 POINTS, WIN!!!
'''
import constants as c
import player as p

def yankenpoRound(p1, p2):
    move1=p1.go()
    move2=p2.go()
    choice=list(c.PAYOFFS[move1,move2])
    p1.result(choice,[move1,move2])
    choice.reverse()
    p2.result(choice,[move2,move1])

    

def yankenpo():
    r1=0
    r2=0
    while r1<3 and r2<3:
        print "YANKENPO!"
        yankenpoRound(p1,p2)
        r1=p1.myScore
        r2=p2.myScore
        print 'va p1 en',r1
        print 'va p2 en',r2
    if r1 == 3:
        print p1.name, 'es el ganador'
    else:
        print p2.name, 'es el ganador'
        
        
p1 = p.RandomPlayer('Player 1')
p2 = p.Player('Player 2')   

yankenpo()
