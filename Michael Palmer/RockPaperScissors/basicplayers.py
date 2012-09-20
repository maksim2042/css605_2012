"""
Michael Palmer
CSS 605
Fall 2012
"""

import constants as c
import player as p
import random

"""
SlightlyImprovedRandomPlayer - a slightly upgraded RandomPlayer implementation

Why the change from RandomPlayer? - Tests can be repeated by sending in the same seed.
"""
class SlightlyImprovedRandomPlayer(Player):
   def __init__(self,seed=None):
       Player.__init__(self)
       random.seed(seed)
   def go(self):
       choice=int(random.uniform(0,3))
       return(c.CHOICES[choice])

"""
HumanPlayer

Utilizes a name parameter to make it easier for two humans to play each other.
"""
class HumanPlayer(p.Player):
    def __init__(self,name):
        super(HumanPlayer,self).__init__()
        self.name = name
    def go(self):
        noMove = True
        while noMove:
            maybemove = raw_input(self.name + "-->")
            if maybemove.upper() in c.CHOICES: return maybemove.upper()

"""
SequncePlayer

Takes an input sequence and produces moves by repeating the sequence.
""" 
class SequencePlayer(p.Player):
    def __init__(self,moves):
        super(SequencePlayer,self).__init__()
        assert(len(moves)>0)
        self.movesequence = moves
        self.counter = 0
        
    def go(self):
        move = self.movesequence[self.counter]
        self.counter += 1
        if (self.counter > len(self.movesequence) -1) :
            self.counter = 0
        return move

"""
TitForTatPlayer

Uses an initial first move and then repeats what the other player did.
"""        
class TitForTatPlayer(p.Player):
   def __init__(self,firstmove):
       super(TitForTatPlayer,self).__init__()
       assert(firstmove in c.CHOICES)
       self.firstmove = firstmove
   def go(self):
       if (len(self.move_history)==0):
           return self.firstmove
       return self.move_history[len(self.move_history) -1][1]

"""
StupidPlayer

Play the move the was sent in with the object initialization.
"""
class StupidPlayer(p.Player):
   def __init__(self,move):
       super(StupidPlayer,self).__init__()
       assert(move in c.CHOICES)
       self.move =move

   def go(self):
       return self.move
