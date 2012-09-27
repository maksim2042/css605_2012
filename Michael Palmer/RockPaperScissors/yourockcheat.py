"""
Michael Palmer
CSS 605
Fall 2012
      
This is a cheat. The code redefines the opponents (all of them) to always play ROCK. 
"""


import constants as c
import player as p

def asyouwish(self):
    return c.ROCK

class YouRock(p.Player):
    def go(self):
        gls = globals()
        for x in gls:
            if  ((isinstance(gls[x], p.Player)==True)and (isinstance(gls[x],YouRock)==False) ):
                gls[x].go = asyouwish.__get__(asyouwish,x)
        return c.PAPER
