'''
supercritter.py

Brendon Fuhs
12/13/2012

Attempt at an artificial life form

Things referenced:

someEnvironment.env[x][y]['key'] => attribute
'el' is elevation, with 0 being ground level
'food'
'radiation'
Also,
'agents' is a dict: agent.id=agent
'X' is 1 if there's an obstacle


Does someEnvironment.getFOV do something?
getFOV(self,x,y,radius)
returns list of xrange and yrange
Actually, I don't know what the heck it does.

do_gradient(self,x,y,radius,rate,type) returns what?

use moveAgent to move

Agents need to have...
x
y
run (function)
id
species

'''

import random as r
import math as m
import copy as c

class SuperCritter(object):
    def __init__(self, world, x=0, y=0, myID="anon"):
        self.x = x
        self.y = y
        self.species = "supercritter"
        self.world = world ## The environment
        self.id = myID
        self.stomach = []
        self.uterus = []
        self.SIGHT = 8
        
    def eat(self, target_x, target_y):
        ## 
        self.stomach.append(something)## 

    def spawn(self):
        # Put contents of uterus in the environment
        self.uterus = []

    def gestate(self):
        uterus.append(SuperCritter)

    def moveSomewhere(self):
        pass

    def run(self):
        pass



