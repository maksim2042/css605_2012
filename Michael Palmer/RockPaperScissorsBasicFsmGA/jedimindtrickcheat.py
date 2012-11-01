"""
Michael Palmer 
CSS605
Fall 2012

   This is a cheat.

   The code looks for the choices and payoffs matrix in memory and alters them 
   to add a new alternative - JEDIMINDTRICK. JEDIMINDTRICK beets anything except
   another JEDIMINDTRICK. 

"""


import constants as c
import player as p


JEDIMINDTRICK = "JEDIMINDTRICK"
cleanChoices = list(c.CHOICES)
if (JEDIMINDTRICK not in cleanChoices):
   jediChoices  = list(cleanChoices)
   jediChoices.append(JEDIMINDTRICK)
   c.CHOICES    = tuple(jediChoices)
   jediPosition = jediChoices.index(JEDIMINDTRICK)
   c.PAYOFFS[JEDIMINDTRICK,JEDIMINDTRICK] = (0,0)
   for x in cleanChoices:
       c.PAYOFFS[(x,JEDIMINDTRICK)] = (-1,1)
       c.PAYOFFS[(JEDIMINDTRICK,x)] = (1,-1)

class JediMindTrick(p.Player):
    def go(self):
        return JEDIMINDTRICK

     


