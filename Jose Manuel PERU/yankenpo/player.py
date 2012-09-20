'''
Created on Sep 13, 2012
you need to use yankenpo
to see how the game run!!!

@author: josemagallanes
'''


import constants as c
import random

class Player(object):

    def __init__(self,name):
        self.name=name
        self.myScore=0
        self.score_history=[]
        self.move_history=[]

    def go(self):
        print self.name, "is a stupid player!"
        return c.CHOICES[1]

    def result(self, choice, moves):
        self.score_history.append(choice)
        self.move_history.append(moves)
        
        if choice[0]==1: 
            self.myScore+=1
            print self.name,": Good Choice!", self.myScore 
        elif choice[0]==0:
            print self.name,': Just a Draw...', self.myScore
        else:
            self.myScore-=1
            print self.name,': Bad Move!', self.myScore
        
        
            
    def history(self):
        print self.score_history  
        print self.move_history 
     
class RandomPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def go(self):
        print self.name, "is a random player!"
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])