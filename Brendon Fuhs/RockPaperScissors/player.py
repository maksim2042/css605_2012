'''

player.py

additional players added by Brendon Fuhs

'''

import constants as c
import random


class Player():
    def __init__(self):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        
    def go(self):
        return c.ROCK

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1: 
            self.myScore+=1
        #   print "I WON!!! ", self.myScore
        elif res[0]==0:
            pass  # I don't want this talking to me.
        #   print 'DRAW ', self.myScore
        else:
            self.myScore-=1
        #   print 'I LOST :((( ', self.myScore


class RandomPlayer(Player): # plays random moves all the time
    def __init__(self):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])


class StupidPlayer(Player): # plays the same move over and over
    def __init__(self):
        Player.__init__(self)
        self.stickToYerGuns = c.CHOICES[int(random.uniform(0,3))]
    def go(self):
        return(self.stickToYerGuns)


class SequencePlayer(Player): # plays the same sequence over and over
    def __init__(self):
        Player.__init__(self)
        self.SEQUENCELENGTH = 42
        self.magicSequence = [" "]*self.SEQUENCELENGTH
        for i in range(self.SEQUENCELENGTH):
            self.magicSequence[i] = c.CHOICES[int(random.uniform(0,3))]
        self.moveNum = 0
    def go(self):
        return(self.magicSequence[self.moveNum % self.SEQUENCELENGTH])


class Tit4TatPlayer(Player): # plays opponent's last move
    def __init__(self):
        Player.__init__(self)
        self.moveNum = -1 # Will change to proper moveNum at beginning of turns
    def go(self):
        self.moveNum += 1
        if self.moveNum == 0:
            return(c.CHOICES[int(random.uniform(0,3))])
        else:
            return(self.move_history[self.moveNum-1][1])


class HumanPlayer(Player): # provides a basic interface for humans to play the game
    def __init__(self):
        Player.__init__(self)
        self.firstTime = True
        self.playerName = "I AM NO MAN"
    def go(self):
        if self.firstTime == True:
            self.playerName = raw_input("Please enter your name... ")
            print "Thank you, ", self.playerName
            self.firstTime = False
        
        print "Dear ", self.playerName, ", "
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


# FIX
class MLPlayer(Player): # uses simple machine learning to estimate probability of next move
    def __init__(self):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

# FIX
class MarkovPlayer(Player): # uses Markov processes to estimate sequence of moves for the opponent
    def __init__(self):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

# FIX
class SleeperCell(Player): # This player waits...
    def __init__(self):
        Player.__init__(self)
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])

# This isn't working properly
class TheCheat(Player): # This player tries to cheat by peeking
    def __init__(self):
        Player.__init__(self)
    # import referee as r # I don't think I need to do this.
    def go(self):
        # make this point to the referee or the thing calling this function
        try:
            Ref.move1
        except:
            return(c.CHOICES[int(random.uniform(0,3))])
        for i in range(3):
            if Ref.move1 == c.CHOICES[i]:
                return c.CHOICES[(i+1)%3]
'''
class TheAssassin(Player)
    def __init__(self):
        Player.__init__(self)
    def go(self):
        del p2
'''
