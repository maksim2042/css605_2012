"""
CSS605 Homework 2: RPS Game
Creates Players for RPS
"""

import RPS_constants

import random

class Player(object):
    def __init__(self):
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        
    def go(self):
        choice = random.randint(1,3)
        if choice = 1
            playermove = ROCK
        else choice = 2
            playermove = SCISSORS
        else playermove = PAPER    
        
print "The players are here!"
