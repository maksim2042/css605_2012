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

    def updatePlayersHistory(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        self.myScore+=res

class RandomPlayer(Player):
    def __init__(self, playerID,pstrategy='Random Player'):
        Player.__init__(self,playerID,'Random Player')

    def strategy(self):
        val=random.randint(0,2)
        return(c.CHOICES[val])


class StupidPlayer(Player):
    def __init__(self, playerID,pstrategy='Stupid Player'):
        Player.__init__(self,playerID,'Stupid Player')
       
    def strategy(self):
        return c.ROCK

class HumanPlayer(Player):
    def __init__(self, playerID,pstrategy='Human Player'):
        Player.__init__(self,playerID,'Human Player')
       
    def strategy(self):
        move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while not move.isdigit():
            print 'not a number...re enter, please!'
            move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while int(move) > 2:
            print 'wrong number!'
            move=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        return (c.CHOICES[int(move)])
    
class tftPlayer(Player):
    def __init__(self, playerID,pstrategy='Automaton Player'):
        Player.__init__(self,playerID,'Automaton Player')
        self.start=0
    
    def strategy(self):
        if self.start==0:
            newoM=c.ROCK
            self.start+=1
        else:
            oM,rM=self.move_history[-1]
            newoM=c.STATES[oM,rM]
        return newoM
    