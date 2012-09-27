'''
Craig Brown
CSS 605
Fall 2012

Rock, Paper, Scissors
Player Class
'''

import constants as c
import random

class Player(object):
    def __init__(self, id="noID"):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
    
    def getID():
        return self.id
    
    def go(self):
        pass
        
    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1:
            self.myScore+=1
            print "I WON! ", self.myScore
        elif res[0]==0:
            print "DRAW ", self.myScore
        else:
            self.myScore-=1
            print "I LOST ", self.myScore
   
class StupidPlayer(Player):
    def __init__(self):
        Player.__init__(self)
    
    def go(self):
        return c.CHOICES[1]

class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)
    
    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])
            
class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
    
    def go(self):
        self.move = raw_input("Select Move (Rock, Paper or Scissors): ")
        while self.move != c.CHOICES[0] and self.move != c.CHOICES[1] and self.move != c.CHOICES[2]:
            self.move = raw_input("ALL CAPS FOOL!  Try again: ")
        return self.move
        
class TitTatPlayer(Player):
    def __init__(self):
        Player.__init__(self)
    
    def go(self):
        
        movelength = len(self.move_history)
        
        if movelength <= 0:
            choice = int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            return self.move_history[movelength -1][1]
           
