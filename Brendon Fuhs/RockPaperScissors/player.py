'''

player.py

additional players added by Brendon Fuhs

ID MIGHT NEEED TO BE FED TO SUPER INIT< NOT SURE

'''

import constants as c
import random
import math
import itertools as it


class Player():
    
    def __init__(self, id="noID"):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        self.id=id

    def getID():
        return self.id
        
    def go(self):
        return c.ROCK

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
        elif res[0]==0:
            pass
        else:
            self.myScore-=1


class RandomPlayer(Player): # plays random moves all the time
    
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])


class StupidPlayer(Player): # plays the same move over and over
    
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        self.stickToYerGuns = c.CHOICES[int(random.uniform(0,3))]
        
    def go(self):
        return(self.stickToYerGuns)


class SequencePlayer(Player): # plays the same sequence over and over
    
    def __init__(self, id="noID"):
        Player.__init__(self)
        self.id=id
        self.SEQUENCELENGTH = 42
        self.magicSequence = [" "]*self.SEQUENCELENGTH
        for i in range(self.SEQUENCELENGTH):
            self.magicSequence[i] = c.CHOICES[int(random.uniform(0,3))]
        self.moveNum = 0
        
    def go(self):
        return(self.magicSequence[self.moveNum % self.SEQUENCELENGTH])


class Tit4TatPlayer(Player): # plays opponent's last move
    
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        self.moveNum = -1 # Will change to proper moveNum at beginning of turns

    def go(self):
        self.moveNum += 1
        if self.moveNum == 0:
            return(c.CHOICES[int(random.uniform(0,3))])
        else:
            return(self.move_history[self.moveNum-1][1])


class HumanPlayer(Player): # provides a basic interface for humans to play the game
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        
    def go(self):

        print "Dear ", self.id, ", "
        while True:
            typedStuff = raw_input("Please type ROCK, PAPER, or SCISSORS and hit enter... ")
            if typedStuff in c.CHOICES:
                return typedStuff
            # Double-check above
            #for choice in c.CHOICES:
            #    if typedStuff == choice:
            #        return (choice)
            
    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
            print "You won. Your running score is ", self.myScore
        elif res[0]==0:
            print "You lost. Your running score is ", self.myScore
        else:
            self.myScore-=1
            print "You had a draw. Your running score is ", self.myScore

# Use math and itertools modules and maybe stats (if available by default) to rewrite this one
class MLPlayer(Player): # uses simple machine learning to estimate probability of next move

    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        self.DECAY_RATE = 0.01 # Float between 0(never forget) and inf(remember last only)
        self.GREEDINESS = 0.0 # Float between -1(random) and 1(totally greedy)
        self.enemyMoveProbs = { c.ROCK: 1.0/3.0,
                                c.PAPER: 1.0/3.0,
                                c.SCISSORS: 1.0/3.0 }
    def go(self):
        
        try: enemyLastMove = self.move_history[len(self.move_history)-1][1]
        except: return(c.CHOICES[int(random.uniform(0,3))])
                   
        self.enemyMoveProbs[enemyLastMove] += 3 * self.DECAY_RATE # I should think through whether
                                                                    # I want the three there.

        # renormalize
        totalProbs = sum(self.enemyMoveProbs.values())
        for move in self.enemyMoveProbs.keys():
            self.enemyMoveProbs[move] /= totalProbs

        # RPS is responded to with PSR (or rather, SPR is responded to with RPS)
        myMoveProbs = [ self.enemyMoveProbs[c.SCISSORS],
                        self.enemyMoveProbs[c.ROCK],
                        self.enemyMoveProbs[c.PAPER] ]
        if self.GREEDINESS <= 0.0:
            for i in range(3):
                myMoveProbs[i] += self.GREEDINESS * (myMoveProbs[i] - 1.0/3.0)
        else:
            indexToAdjust = -1
            for i in range(3):
                if myMoveProbs[i]==max(myMoveProbs):
                    myMoveProbs[i] += self.GREEDINESS * (1.0 - myMoveProb[i])
                elif myMoveProbs[i]==min(myMoveProbs):
                    myMoveProbs[i] -= self.GREEDINESS * myMoveProbs[i]
                else:
                    indexToAdjust = i
            myMoveProbs[indexToAdjust] = 1 - myMoveProbs[(indexToAdjust+1)%3] - myMoveProbs[(indexToAdjust+2)%3]
            
        diceRoll = random.random()
        if diceRoll <= myMoveProbs[0]:
            return(c.CHOICES[0])
        elif diceRoll <= myMoveProbs[0]+myMoveProbs[1]:
            return(c.CHOICES[1])
        else:
            return(c.CHOICES[2])


class MarkovPlayer(Player): # uses Markov processes to estimate sequence of moves for the opponent

    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        
        self.DECAY_RATE = 0.01 # Float between 0(never forget) and 1(remember last only(if that?))
        self.GREEDINESS = 0.0 # Float between -1(random) and 1(totally greedy)
        self.DEPTH = 3 # int; how many rounds considered as a state
                        # set to 1 for more-or-less ordinary transition probabilities.
                        # Keep small or your computer will explode.

        self.possibleRounds = tuple(it.product(c.CHOICES,repeat=2))
        self.states = tuple(it.product(self.possibleRounds,repeat=self.DEPTH))
        self.stateResponses = {}
        for state in self.states:
            self.stateResponses[state] = [0.1,0.1,0.1]

        
    def go(self):
        # Just do random until we have enough move depth
        lastMoveNum = len(self.move_history)
        if lastMoveNum <= self.DEPTH+1:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])

        lastMove = self.move_history[lastMoveNum-1][1]

        lastState=[("None","None")]*self.DEPTH
        thisState=[("None","None")]*self.DEPTH

        for i in range(self.DEPTH):
            lastState[i] = tuple(self.move_history[i+lastMoveNum-self.DEPTH-2])
            thisState[i] = tuple(self.move_history[i+lastMoveNum-self.DEPTH-1])

        lastState=tuple(lastState)
        thisState=tuple(thisState)

        # Tally the last response in terms of the state it was responding to
        if lastMove == c.ROCK:
            self.stateResponses[lastState][0] += 1
        elif lastMove == c.PAPER:
            self.stateResponses[lastState][1] += 1
        else:
            self.stateResponses[lastState][2] += 1

        self.applyDecay()

        
        # determine probs for this round
        numThisState = sum(self.stateResponses[thisState])
        
        probsThisRound = [0]*3
        # for response in self.stateResponses[thisState]:
        for i in range(3):
            probsThisRound[i] = self.stateResponses[thisState][i] / float(numThisState)
    
        # rotate to get neutral-greed move probabilties
        myMoveProbs = [0]*3
        for i in range(3):
            myMoveProbs[i] = probsThisRound[(i-1)%3]

        # apply greed
        myMoveProbs = self.applyGreed(myMoveProbs)
        
        # roll the dice to decide more
        diceRoll = random.random()
        if diceRoll <= myMoveProbs[0]:
            return(c.CHOICES[0])
        elif diceRoll <= myMoveProbs[0]+myMoveProbs[1]:
            return(c.CHOICES[1])
        else:
            return(c.CHOICES[2])

    def applyDecay(self):
        for state in self.stateResponses.keys():
            for i in range(3):
                self.stateResponses[state][i] *= (1-self.DECAY_RATE)

    # maybe recheck this one to comment through
    def applyGreed(self, probs):
        
        if self.GREEDINESS <= 0.0:
            for i in range(3):
                probs[i] += self.GREEDINESS * (probs[i] - 1.0/3.0)
        else:
            indexToAdjust = -1
            for i in range(3):
                if probs[i]==max(probs):
                    probs[i] += self.GREEDINESS * (1.0 - probs[i])
                elif probs[i]==min(probs):
                    probs[i] -= self.GREEDINESS * probs[i]
                else:
                    indexToAdjust = i
            probs[indexToAdjust] = 1 - probs[(indexToAdjust+1)%3] - probs[(indexToAdjust+2)%3]
            
        return probs



# FIX
# I might not have time to do anything too supercool with this.
class SleeperCell(Player): # This player waits...
    
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
        
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])
'''
    class Strategem():
        def __init__(self, paramList=[]):
            #decay
            #greediness
            #depth

        def applyDecay():
            pass

        def applyGreed():
            pass

        def applyDepth():
            pass
        def recommendMove():
            return a recommendation

    class Adapt(Strategem):
        pass

    class DeepMarkov(Strategem):
        pass

    class MLprobs(Strategem):
        pass

    # fourier/cyclic, treeprobs, etc


import referee.py as r
# These both depend on what's happening with the referee

# This isn't working properly
class TheCheat(Player): # This player tries to cheat by peeking
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
        self.id=id
    # import referee as r # I don't think I need to do this.
    def go(self):        # make this point to the referee or the thing calling this function
        try:
            Ref.move1
        except:
            return(c.CHOICES[int(random.uniform(0,3))])
        for i in range(3):
            if Ref.move1 == c.CHOICES[i]:
                return c.CHOICES[(i+1)%3]

class TheAssassin(Player)
    def __init__(self, id="noID"):
        Player.__init__(self, id="noID")
    def go(self):
        del p2
'''
