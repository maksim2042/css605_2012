from altagent import Agent
from math import sqrt
import random as r


POSSIBLESTEPS= [ (1,0,1),
                 (-1,0,1),
                 (0,1,1),
                 (0,-1,1),
                 (1,-1,sqrt(2)),
                 (1,1,sqrt(2)),
                 (-1,-1,sqrt(2)),
                 (-1,1,sqrt(2)) ]
                 

class StupidSimpleAgent(Agent):
    def move(self):
        #Random Walk!
        if self.isAlive:
          step = r.choice(POSSIBLESTEPS)
          oldcell = self.env.env[self.x][self.y]
          oldelevation = oldcell['el']
          self.x = self.env.wrap(self.x + step[0])
          self.y = self.env.wrap(self.y + step[1])
          newcell = self.env.env[self.x][self.y]
          newelevation = newcell['el']
          newradiation  = newcell['radiation']
          deltael = abs(newelevation - oldelevation)
          if deltael > 0.2:
             length = sqrt(deltael**2 + step[2]**2)
          else:
             length = step[2]
          self.energy -= newradiation + length + self.energy_move_delta
          if self.shoulddie(): self.die()
        
