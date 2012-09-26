'''

player.py

additional players added by Brendon Fuhs

ID MIGHT NEEED TO BE FED TO SUPER INIT< NOT SURE

'''

import constants as c
import random


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
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])


class StupidPlayer(Player): # plays the same move over and over
    def __init__(self, id="noID"):
        Player.__init__(self)
        self.stickToYerGuns = c.CHOICES[int(random.uniform(0,3))]
    def go(self):
        return(self.stickToYerGuns)


class SequencePlayer(Player): # plays the same sequence over and over
    def __init__(self, id="noID"):
        Player.__init__(self)
        self.SEQUENCELENGTH = 42
        self.magicSequence = [" "]*self.SEQUENCELENGTH
        for i in range(self.SEQUENCELENGTH):
            self.magicSequence[i] = c.CHOICES[int(random.uniform(0,3))]
        self.moveNum = 0
    def go(self):
        return(self.magicSequence[self.moveNum % self.SEQUENCELENGTH])


class Tit4TatPlayer(Player): # plays opponent's last move
    def __init__(self, id="noID"):
        Player.__init__(self)
        self.moveNum = -1 # Will change to proper moveNum at beginning of turns
    def go(self):
        self.moveNum += 1
        if self.moveNum == 0:
            return(c.CHOICES[int(random.uniform(0,3))])
        else:
            return(self.move_history[self.moveNum-1][1])


# RE-TEST THIS
class HumanPlayer(Player): # provides a basic interface for humans to play the game
    def __init__(self, id="noID"):
        Player.__init__(self)
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


class MLPlayer(Player): # uses simple machine learning to estimate probability of next move
    def __init__(self, id="noID"):
        Player.__init__(self)
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
            myMoveProbs[i] = 1 - myMoveProbs[(i+1)%3] - myMoveProbs[(i+2)%3]
            
        diceRoll = random.random()
        if diceRoll <= myMoveProbs[0]:
            return(c.CHOICES[0])
        elif diceRoll <= myMoveProbs[0]+myMoveProbs[1]:
            return(c.CHOICES[1])
        else:
            return(c.CHOICES[2])

    

# FIX
class MarkovPlayer(Player): # uses Markov processes to estimate sequence of moves for the opponent
    def __init__(self, id="noID"):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

# FIX
class SleeperCell(Player): # This player waits...
    def __init__(self, id="noID"):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

#    class strategem():
    
'''

import referee.py as r
# These both depend on what's happening with the referee

# This isn't working properly
class TheCheat(Player): # This player tries to cheat by peeking
    def __init__(self, id="noID"):
        Player.__init__(self)
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
        Player.__init__(self)
    def go(self):
        del p2
'''
