'''
Created on Sep 29, 2012

@author: josemagallanes
'''
import random
import constants as c

class Player(object):

    def __init__(self,name,payoff=0):
        self.name=name
        self.payoff=payoff

    def strategy (self):
        pass
    
    def record(self):
        pass

class PlayerRandom(Player):

    def __init__(self,name,payoff=0):
        Player.__init__(self,name,payoff)
        
    def strategy (self): 
        return(c.CHOICES[random.randint(0,2)])
    


class PlayerStupid(Player):

    def __init__(self,name,payoff=0):
        Player.__init__(self,name,payoff)
        
    def strategy (self):
        return c.ROCK
    
class PlayerHuman(Player):
    def __init__(self, name='YOU',pstrategy='Human Player'):
        Player.__init__(self,name,'Human Player')
       
    def strategy(self):
        choice=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while not choice.isdigit():
            print 'not a number...re enter, please!'
            choice=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        while int(choice) > 2:
            print 'wrong number!'
            choice=raw_input('Input 0 (ROCK), 1 (PAPER), 2 (SCISSORS):')
        return (c.CHOICES[int(choice)])