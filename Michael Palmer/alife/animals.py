from environment import Environment
from genomeagent import *
from math        import sqrt
from clock       import run


def make_rabbit(env):
   rabbit = [ 10,
               9,
               9,
               5,
               1,
               1,
               1,
               1,
               1,
               2,
              10]
   return Rabbit(env,rabbit,'rabbit')

def make_wolf(env):
    wolf = [ 10,
             36,
              9,
             20,
             20,
              1,
              9,
             20,
              2,
              1,
             20]
    return Wolf(env,wolf,'wolf')

def test_rabbit():
   ev = Environment(10)
   rb = make_rabbit(ev)
   ev.putAgent(rb)
   rb.run()

def test_wolf():
   ev = Environment(10)
   wf = make_wolf(ev)
   ev.putAgent(wf)
   wf.run()

def test_chase():
   ev = Environment(10)
   wf = make_wolf(ev)
   rb = make_rabbit(ev)
   rb.x = 1
   rb.y = 1
   wf.x = 3
   wf.y = 3
   ev.putAgent(rb)
   ev.putAgent(wf)
   return run(ev)

class Rabbit(GenomeAgent):
      def eat_grass(self):
        if self.env.env[self.x][self.y].has_key('food') and self.env.env[self.x][self.y]['food'] > 0:
           food_consumed = self.consumption_rate
           if self.env.env[self.x][self.y]['food'] < self.consumption_rate:
              food_consumed = self.env.env[self.x][self.y]['food']
           self.energy += food_consumed 
           self.env.env[self.x][self.y]['food']-=food_consumed
            
        return self.env.env[self.x][self.y]['food']   
      def avoid_predators(self,movement):
         # Allows the rabbit to react to a new, closer predator
         # Does not stop the rabbit from running back towards a previous predator
         while (self.visible_predators() and movement > 0):
              closest = self.find_closest_predator(self.getFOV())
              if closest != []:
                 x_move,y_move = self.get_directionaway(closest[0][1],closest[0][2])
                 self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                 movement -= 1
         return movement
      def run(self):
          movement = self.movement_rate

          self.age += 0.1

          self.eat_grass()
          
          if self.visible_predators(): movement = self.avoid_predators(movement)

          self.eat_grass()


          if self.shoulddie() :
             self.die()
             return (self.x,self.y)

          
         

          print 'rabbit %s %s %s \n'%(self.x,self.y,self.energy)
          return (self.x,self.y)

          
class Wolf(GenomeAgent):
      def chase_prey(self,movement):
         #
         # If a prey gets ahead of the wolf through activation order a new prey may actually be closer
         #
         while (self.visible_prey() and movement > 0):
            closest = self.find_closest_prey(self.getFOV())
            if closest != []:
                 x_move,y_move = self.get_directiontoward(closest[0][1],closest[0][2])
                 self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                 movement -= 1
         return movement
      def run(self):
          movement = self.movement_rate

          self.age += 0.1
          
          if self.visible_prey():movement = self.chase_prey(movement)

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)
          
          print 'wolf %s %s \n'%(self.x,self.y)
          return (self.x,self.y)
