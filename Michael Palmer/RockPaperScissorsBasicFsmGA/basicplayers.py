"""
Michael Palmer
CSS 605
Fall 2012
"""

import constants as c
import player as p
import random
import unittest

"""
MostLikelyPlayer - look at oponenets moves and choose oposite on a
probabilistic basis
"""
class MostLikelyPlayer(p.Player):
   counters = { c.ROCK:c.PAPER,c.PAPER:c.SCISSORS,c.SCISSORS:c.ROCK}
   def __init__(self,pid='noId',firstMove = c.PAPER):
      super(MostLikelyPlayer,self).__init__(pid)
      self.firstMove = firstMove
   def go(self):
      if self.move_history==[]:
         return self.firstMove
      selectedMove = random.choice(self.move_history)
      return self.counters[selectedMove[1]]

"""
SlightlyImprovedRandomPlayer - a slightly upgraded RandomPlayer implementation

Why the change from RandomPlayer? - Tests can be repeated by sending in the same seed.
"""
class SlightlyImprovedRandomPlayer(p.Player):
   def __init__(self,pid ='noId',seed=None):
       super(SlightlyImprovedRandomPlayer,self).__init__(pid)
       random.seed(seed)
   def go(self):
       choice=int(random.uniform(0,3))
       return(c.CHOICES[choice])

"""
HumanPlayer

Utilizes a name parameter to make it easier for two humans to play each other.
"""
class HumanPlayer(p.Player):
    def __init__(self,pid='noId'):
        super(HumanPlayer,self).__init__(pid)
        self.name = pid
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
    def __init__(self,pid='noId',moves=[c.ROCK,c.PAPER,c.SCISSORS]):
        super(SequencePlayer,self).__init__(pid)
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
   def __init__(self,pid='noId',firstmove=c.PAPER):
       super(TitForTatPlayer,self).__init__(pid)
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
   def __init__(self,pid='noId',move=c.SCISSORS):
       super(StupidPlayer,self).__init__(pid)
       assert(move in c.CHOICES)
       self.move =move

   def go(self):
       return self.move


class testplayers(unittest.TestCase):
     def getsuite(self):
        suite = unittest.TestSuite()
        suite.addTest(testplayers('test_buildStupidPlayer'))
        suite.addTest(testplayers('test_buildTitForTatPlayer'))
        suite.addTest(testplayers('test_buildSequencePlayer'))
        suite.addTest(testplayers('test_buildHumanPlayer'))
        return suite
      
     def runTest(self):
         runner = unittest.TextTestRunner(verbosity=2)
         suite = self.getsuite()
         result = runner.run(suite)

     def test_buildRandomPlayer(self):
        tt = SlightlyImprovedRandomPlayer('id',1)
        m = tt.go()
        self.assertEqual(c.ROCK,m)
        m = tt.go()
        self.assertEqual(c.SCISSORS,m)

     def test_buildStupidPlayer(self):
        for x in c.CHOICES:
           sp = StupidPlayer( x + 'Player',x)
           self.assertEqual(sp.move,x)
           self.assertEqual(sp.id,x+'Player')

     def test_buildTitForTatPlayer(self):
        tt = TitForTatPlayer()
        tt.move_history.append([c.ROCK,c.PAPER])
        move = tt.go()
        self.assertEqual(move,c.PAPER)
        tt.move_history.append([c.SCISSORS,c.ROCK])
        move = tt.go()
        self.assertEqual(move,c.ROCK)

     def test_buildSequencePlayer(self):
        tt = SequencePlayer('noName',[c.ROCK,c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.ROCK)
        move = tt.go()
        self.assertEqual(move,c.ROCK)
        move = tt.go()
        self.assertEqual(move,c.SCISSORS)
        move = tt.go()
        self.assertEqual(move,c.ROCK)

     def test_buildHumanPlayer(self):
        tt = HumanPlayer('Maurice')
        self.assertEqual(tt.id,'Maurice')
        self.assertEqual(tt.name,'Maurice')
