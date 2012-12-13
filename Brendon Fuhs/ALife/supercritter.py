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
        self.STOMACH_EXPLODE = 10
        
    def consume(self, doomedCritters):
        for critter in doomedCritters:
            stomach.append(c.deep.copy(doomedCritters[critter]))
            del doomedCritters[critter]
        if len(stomach) > STOMACH_EXPLODE:
            del self ## Pretty sure this won't work

    def spawn(self):
        self.world.putAgent(SuperCritter(self.world))

    def moveSomewhere(self):
        pass

    def run(self):
        if 'agents' in self.world[self.x][self.y]:
            self.consume(self.world[self.x][self.y]['agents'])
        elif len(uterus)>0:
            self.spawn()
        self.moveSomewhere()
            
        
        
        
        



