
"""
Michael Palmer
CSS605
Fall2012
FiniteStateMachine - RockPaperScissors

fsm.py represents a suggested implementation for a finite state machine Rock Paper Scissors player.

"""

import random as r
import player as p
import constants as c
import unittest

"""
START_NODE     : fsm node to use as initial state
FSMNAME        : name of the node in the fsm dictionary
FSMVALUE       : move returned from being at this node in the fsm dictionary
FSMTRANSITIONS : name of the transitions dictionary in the fsm dict record
ANYMOVE        : a special transition token that matches any move
RANDOMMOVE     : a special value token that will generate a legal random move
"""
START_NODE     = "START"
FSMNAME        = 'Name'
FSMVALUE       = 'Value'
FSMTRANSITIONS = 'Transitions'
ANYMOVE        = 'ANY'
RANDOMMOVE     = 'RND'


"""
   finitestatemachinev1
   Stores the data and current state for a finite state machine
"""
class finitestatemachinev1(object):
    NODENAME        = 0
    NODEVALUE       = 1
    NODETRANSITIONS = 2
    """
      __init__
      legalmoves = a list of leagal moves for this FSM
    """
    def __init__(self,legalmoves = c.CHOICES):
        self.currentNode = None
        self.startNode   = None
        self.stateDict   = {}
        self.legalmoves  = c.CHOICES
    """
      getValue
      return the move associated with being at the current node
      process a RANDOMMOVE token to return a selected legal move
    """
    def getValue(self):
        if self.currentNode == None: self.currentNode = self.startNode
        nodeValue = self.stateDict[self.currentNode][FSMVALUE]
        if nodeValue == RANDOMMOVE:
           nodeValue = r.choice(self.legalmoves)
        return nodeValue
    """
      transition
      process an opponents move to move to a new node
      handles an ANYMOVE transition to automatically move to that state
    """
    def transition(self,move):
        if self.stateDict[self.currentNode][FSMTRANSITIONS].has_key(ANYMOVE):
           self.currentNode = self.stateDict[self.currentNode][FSMTRANSITIONS][ANYMOVE]
        elif self.stateDict[self.currentNode][FSMTRANSITIONS].has_key(move):
           self.currentNode = self.stateDict[self.currentNode][FSMTRANSITIONS][move]
    """
       addState
       add a new state to the fsm
       nodeName    any value that can serve as a dict key
       nodeValue   a legal move for being in the current state
       nodeTransitions  a dictionary of new states that can be reached from the current state
    """
    def addState(self,nodeName,nodeValue,nodeTransitions):
        assert(isinstance(nodeTransitions,dict))
        self.stateDict[nodeName] =  {FSMNAME: nodeName,FSMVALUE:nodeValue,FSMTRANSITIONS:nodeTransitions}
    """
       addStates
       process a list of states to setup the fsm
       statelist   list of states to add to the fsm
       startNode   node to use as starting node in the statelist
    """
    def addStates(self,startNode,statelist):
        self.startNode = startNode
        for state in statelist:
            nodeName        = state[NODENAME]
            nodeValue       = state[NODEVALUE]
            nodeTransitions = state[NODETRANSITIONS]
            self.addState(nodeName,nodeValue,nodeTransitions)
    """
       reset
       move the fsm back to its starting state
    """
    def reset(self):
        self.currentNode = self.startNode
    
        
"""
   FSMPlayer
   A minimal Rock Paper Scissors player that takes an fsm to determine strategy
"""
class FSMPlayer(p.Player):
    def __init__(self,fsm,id='NoId'):
        super(FSMPlayer,self).__init__(id)
        self.fsm = fsm
        
    def go(self):       
        return self.fsm.getValue()

    def result(self, res, moves):
        super(FSMPlayer,self).result(res,moves)
        opponentMove = moves[1]
        self.fsm.transition(opponentMove)


ROCKPLAYER     = "ROCK"
SCISSORSPLAYER = "SCISSORS"
PAPERPLAYER    = "PAPER"
TITFORTATPLAYER= "TITFORTAT"
REPEATPLAYER   = "REPEAT"
RANDOMPLAYER   = "RANDOM"
SEQUENCEPLAYER = "SEQUENCEPLAYER"


"""
   fsmplayerfactory
   A helper class to build common strategies
   sequence   Only used by the sequence player example [c.ROCK,c.PAPER,c.PAPER]
"""
def fsmplayerfactory(fsmplayertype,sequence=None):
    fsm = finitestatemachinev1() 
    if   fsmplayertype == ROCKPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,{ANYMOVE:'R'})
    elif fsmplayertype == SCISSORSPLAYER:
         fsm.startNode = 'S'
         fsm.addState('S',c.SCISSORS,{ANYMOVE:'S'})
    elif fsmplayertype == PAPERPLAYER:
         fsm.startNode = 'P'
         fsm.addState('P',c.PAPER,{ANYMOVE:'P'})
    elif fsmplayertype == TITFORTATPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,{c.PAPER:'S',c.ROCK:'P',c.SCISSORS:'R'})
         fsm.addState('S',c.SCISSORS,{c.PAPER:'S',c.ROCK:'P',c.SCISSORS:'R'})
         fsm.addState('P',c.PAPER,{c.PAPER:'S',c.ROCK:'P',c.SCISSORS:'R'})
    elif fsmplayertype == REPEATPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,{c.PAPER:'P',c.ROCK:'R',c.SCISSORS:'S'})
         fsm.addState('S',c.SCISSORS,{c.PAPER:'P',c.ROCK:'R',c.SCISSORS:'S'})
         fsm.addState('P',c.PAPER,{c.PAPER:'P',c.ROCK:'R',c.SCISSORS:'S'})
    elif fsmplayertype == RANDOMPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',RANDOMMOVE,{ANYMOVE:'R'})
    elif fsmplayertype == SEQUENCEPLAYER:
         fsm.startNode = 0
         for x in range(len(sequence) - 1) :
            fsm.addState(x,sequence[x],{ANYMOVE: x+1})
         fsm.addState(len(sequence) - 1,sequence[len(sequence) -1],{ANYMOVE:0}),        
    return FSMPlayer(fsm)
    


class testplayers(unittest.TestCase):
     def getsuite(self):
        suite = unittest.TestSuite()
        suite.addTest(testplayers('test_buildStupidPlayer'))
        suite.addTest(testplayers('test_buildTitForTatPlayer'))
        suite.addTest(testplayers('test_buildRepeatPlayer'))
        suite.addTest(testplayers('test_buildSequencePlayer'))
        suite.addTest(testplayers('test_buildRandomPlayer'))
        return suite
      
     def runTest(self):
         runner = unittest.TextTestRunner(verbosity=2)
         suite = self.getsuite()
         result = runner.run(suite)

     def test_buildRandomPlayer(self):
        r.seed(1)
        tt = fsmplayerfactory(RANDOMPLAYER)
        m = tt.go()
        self.assertEqual(c.ROCK,m)
        m = tt.go()
        self.assertEqual(c.SCISSORS,m)

     def test_buildStupidPlayer(self):
        for x in [ROCKPLAYER,PAPERPLAYER,SCISSORSPLAYER]:
           sp = fsmplayerfactory(x)
           move = sp.go()
           self.assertEqual(move,x)

     def test_buildTitForTatPlayer(self):
        tt = fsmplayerfactory(TITFORTATPLAYER)
        tt.go()
        tt.result([1,-1],[c.ROCK,c.PAPER])
        move = tt.go()
        self.assertEqual(move,c.SCISSORS)
        tt.result([1,-1],[c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.ROCK)
        tt.result([1,-1],[c.ROCK,c.ROCK])
        move = tt.go()
        self.assertEqual(move,c.PAPER)

    
     def test_buildRepeatPlayer(self):
        tt = fsmplayerfactory(REPEATPLAYER)
        tt.go()
        tt.result([1,-1],[c.ROCK,c.PAPER])
        move = tt.go()
        self.assertEqual(move,c.PAPER)
        tt.result([1,-1],[c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.SCISSORS)
        tt.result([1,-1],[c.ROCK,c.ROCK])
        move = tt.go()
        self.assertEqual(move,c.ROCK)

        
     def test_buildSequencePlayer(self):
        tt = fsmplayerfactory(SEQUENCEPLAYER,[c.ROCK,c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.ROCK)
        tt.result([1,-1],[c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.ROCK)
        tt.result([1,-1],[c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.SCISSORS)
        tt.result([1,-1],[c.ROCK,c.SCISSORS])
        move = tt.go()
        self.assertEqual(move,c.ROCK)


