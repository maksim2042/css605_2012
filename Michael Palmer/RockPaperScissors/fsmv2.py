
"""
Michael Palmer
CSS605
Fall2012
FiniteStateMachine - RockPaperScissors

fsmv2.py represents a suggested implementation for a finite state machine Rock Paper Scissors player.

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

"""
   finitestatemachinev2
   Stores the data and current state for a finite state machine
"""
class finitestatemachinev2(object):
    NODENAME           = 0
    NODEVALUE          = 1
    ROCKTRANSITION     = 2
    PAPERTRANSITION    = 3
    SICSSORSTRANSITION = 4
    """
      __init__
      legalmoves = a list of leagal moves for this FSM
    """
    def __init__(self,legalmoves = c.CHOICES):
        self.currentNode = None
        self.startNode   = None
        self.stateDict   = {}
        self.legalmoves  = c.CHOICES

    def getValue(self):
        if self.currentNode == None: self.currentNode = self.startNode
        nodeValue = self.stateDict[self.currentNode][FSMVALUE]
        return nodeValue

    def transition(self,move):
        if self.stateDict[self.currentNode][FSMTRANSITIONS].has_key(move):
           self.currentNode = self.stateDict[self.currentNode][FSMTRANSITIONS][move]

    def addState(self,nodeName,nodeValue,rockTrans,paperTrans,scissorsTrans):
        nodeTransitions          = {c.ROCK:rockTrans,c.PAPER:paperTrans,c.SCISSORS:scissorsTrans}
        self.stateDict[nodeName] =  {FSMNAME: nodeName,FSMVALUE:nodeValue,FSMTRANSITIONS:nodeTransitions}

    def addStates(self,startNode,statelist):
        self.startNode = startNode
        for state in statelist:
            nodeName        = state[NODENAME]
            nodeValue       = state[NODEVALUE]
            rockTrans       = state[ROCKTRANSITION]
            paperTrans      = state[PAPERTRANSITION]
            scissorsTrans   = state[SCISSORSTRANSITION]
            self.addState(nodeName,nodeValue,rockTrans,paperTrans,scissorsTrans)

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
    fsm = finitestatemachinev2() 
    if   fsmplayertype == ROCKPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,'R','R','R')
    elif fsmplayertype == SCISSORSPLAYER:
         fsm.startNode = 'S'
         fsm.addState('S',c.SCISSORS,'S','S','S')
    elif fsmplayertype == PAPERPLAYER:
         fsm.startNode = 'P'
         fsm.addState('P',c.PAPER,'P','P','P')
    elif fsmplayertype == TITFORTATPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,'P','S','R')
         fsm.addState('S',c.SCISSORS,'P','S','R')
         fsm.addState('P',c.PAPER,'P','S','R')
    elif fsmplayertype == REPEATPLAYER:
         fsm.startNode = 'R'
         fsm.addState('R',c.ROCK,'R','P','S')
         fsm.addState('S',c.SCISSORS,'R','P','S')
         fsm.addState('P',c.PAPER,'R','P','S')
    elif fsmplayertype == SEQUENCEPLAYER:
         fsm.startNode = 0
         for x in range(len(sequence) - 1) :
            fsm.addState(x,sequence[x],x+1,x+1,x+1)
         fsm.addState(len(sequence) - 1,sequence[len(sequence) -1],0,0,0),        
    return FSMPlayer(fsm)
    


class testplayers(unittest.TestCase):
     def getsuite(self):
        suite = unittest.TestSuite()
        suite.addTest(testplayers('test_buildStupidPlayer'))
        suite.addTest(testplayers('test_buildTitForTatPlayer'))
        suite.addTest(testplayers('test_buildRepeatPlayer'))
        suite.addTest(testplayers('test_buildSequencePlayer'))
        return suite
      
     def runTest(self):
         runner = unittest.TextTestRunner(verbosity=2)
         suite = self.getsuite()
         result = runner.run(suite)

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


