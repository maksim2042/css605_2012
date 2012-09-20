'''
Created on Sep 19, 2012
@author: josemagallanes
YANKENPO IS THE NAME OF THIS GAME IN PERU!!!!!!!

THE FIRST ONE WHO GETS 3 POINTS, WIN!!!
'''
import constants as c 
import player as p
import random

def yankenpoRound(p1, p2): #HERE WE DO ONE GAME
    move1=p1.go()   #WE GET THE CHOICE OF PLAYER ONE
    move2=p2.go()   #WE GET THE CHOICE OF PLAYER TWO
    choice=list(c.PAYOFFS[move1,move2]) #WE STORE THE CHOICES IN A LIST
    p1.result(choice,[move1,move2]) # WE PASS THE RESULT, PLAYER ONE WILL KNOW RESULT - IN [0] IS THE SCORE
    choice.reverse() # WE REVERSE THE ORDER OF THE LIST, SO ELEMENT [0] IS THE SCORE!!
    p2.result(choice,[move2,move1]) # WE PASS THE RESULT, PLAYER ONE WILL KNOW RESULT

def yankenpo():
    r1=0 #HERE WE STORE THE PARTIAL RESULTS OF PLAYER ONE
    r2=0 #HERE WE STORE THE PARTIAL RESULTS OF PLAYER TWO
    while r1<3 and r2<3: #WE FINISH THE GAME WHEN ONE GETS THREE POINTS!!
        print "YANKENPO!"#WE SAY THIS WORD IN PERU BEFORE OUR HANDS ARE SHOWN!!
        yankenpoRound(p1,p2)
        r1=p1.myScore
        r2=p2.myScore
    if r1 > r2:
        print p1.name, 'is the winner'
    else:
        print p2.name, 'is the winner'
        
#**************
oponents=int(random.uniform(0,2)) 
if oponents==0:   
    p1 = p.RandomPlayer('Player 1')
    print 'Player 1 is a Random Player'
    p2 = p.RandomPlayer('Player 2')   
    print 'Player 2 is an Random Player'
else :
    p1 = p.RandomPlayer('Player 1')
    print 'Player 1 is a Random Player'
    p2 = p.Player('Player 2')   
    print 'Player 2 is an Stupid Player'
    

yankenpo()
#**************