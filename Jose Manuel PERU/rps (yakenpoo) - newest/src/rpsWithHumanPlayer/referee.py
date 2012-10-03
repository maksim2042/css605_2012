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
    move1=p1.strategy()   #WE GET THE CHOICE OF PLAYER ONE
    move2=p2.strategy()   #WE GET THE CHOICE OF PLAYER TWO
    choice=list(c.PAYOFFS[move1,move2]) #WE STORE THE CHOICES IN A LIST
    p1.result(choice,[move1,move2]) # WE PASS THE RESULT, PLAYER ONE WILL KNOW RESULT - IN choice[0] IS THE SCORE
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
        print p1.playerID, 'WON THE GAME!!'
    else:
        print p2.playerID, 'WON THE GAME!!'
        
#**************
oponents= int(random.uniform(0,4)) 
if oponents==0:   
    p1 = p.RandomPlayer('Tom')   
    p2 = p.RandomPlayer('Mary')
elif oponents==1:
    p1 = p.HumanPlayer('YOU')   
    p2 = p.RandomPlayer('Mary')
elif oponents==2:
    p1 = p.HumanPlayer('YOU')   
    p2 = p.StupidPlayer('Mary')
else :
    p1 = p.RandomPlayer('Jim')    
    p2 = p.StupidPlayer('Lidia')      
    

yankenpo()
#**************