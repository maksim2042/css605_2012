'''
Created on Sep 22, 2012

@author: josemagallanes
'''

"""
We implement a SUPER CLASS PLAYER and then define subclasses according to the type of player playing strategy
"""
import random
import constants as c

class Player(object):
    '''super class'''
    def __init__(self, playerID,pstrategy):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        self.playerID=playerID
        self.pstrategy=pstrategy
        print '%s is a %s' % (self.playerID,self.pstrategy)  

    def getplayerID(self):
        return self.playerID

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
            print "I WON!!! ", self.myScore
        elif res[0]==0:
            print 'DRAW ', self.myScore
        else:
            self.myScore-=1
            print 'I LOST :((( ', self.myScore

class RandomPlayer(Player):
    def __init__(self, playerID,pstrategy='Random Player'):
        Player.__init__(self,playerID,'Random Player')

    def strategy(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

c
class StupidPlayer(Player):
    def __init__(self, playerID,pstrategy='StupidPlayer'):
        Player.__init__(self,playerID,'StupidPlayer')
       
    def strategy(self):
        return c.ROCK
