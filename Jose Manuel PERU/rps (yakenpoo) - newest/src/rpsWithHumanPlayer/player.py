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
        print '%s : %s' % (self.playerID,self.pstrategy)  

    def getplayerID(self):
        return self.playerID

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
            print "%s GOOD CHOICE (with %d points so far) " %(self.playerID, self.myScore)
        elif res[0]==0:
            print '%s DRAW (with %d points so far)' %(self.playerID, self.myScore)
        else:
            self.myScore-=1
            print '%s BAD CHOICE (with %d points so far)' %(self.playerID, self.myScore)

class RandomPlayer(Player):
    def __init__(self, playerID,pstrategy='Random Player'):
        Player.__init__(self,playerID,'Random Player')

    def strategy(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

c
class StupidPlayer(Player):
    def __init__(self, playerID,pstrategy='Stupid Player'):
        Player.__init__(self,playerID,'Stupid Player')
       
    def strategy(self):
        return c.ROCK

class HumanPlayer(Player):
    def __init__(self, playerID,pstrategy='Human Player'):
        Player.__init__(self,playerID,'Human Player')
       
    def strategy(self):
        try:
            choice=10
            while (choice)>2:
                choice=int(raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):'))
                if choice > 2:
                    print 'wrong number!'
            return (c.CHOICES[choice])
        except ValueError, e:
            print e # output: "integer division or modulo by zero"