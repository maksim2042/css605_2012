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
      def get_predators(self,fov):
          neighbors = self.get_neighbors(fov)
          predators = [x for x in neighbors  if x[2].eats_meat == True]
          return predators
      def find_closest_predator(self,fov):
          predators = self.get_predators(fov)
          if predators == []: return []
          distances = [(self.dist(x[2]),x[0],x[1],x[2]) for x in predators]
          distances.sort()
          return [distances[0]]
      def get_directionaway(self,x,y):
          if abs(x) > 1 : x = x / abs(x)
          if abs(y) > 1 : y = y / abs(y)
          if x == 0 : x = 1
          if y == 0 : y = 1
          return x *-1 , y *-1
      def run(self):
          fov=self.getFOV()
          closest_predator = self.find_closest_predator(fov)
          if closest_predator != []:
             print closest_predator[0]
             x_move,y_move = self.get_directionaway(closest_predator[0][1],closest_predator[0][2])
             print 'rabbitmove' + repr(x_move) + ',' + repr(y_move) + '\n'
             self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move))
             print 'rabit ' + repr(self.x) + ',' + repr(self.y) + '\n'
          return (self.x,self.y)

          
class Wolf(GenomeAgent):
      def get_prey(self,fov):
          neighbors = self.get_neighbors(fov)
          prey = [x for x in neighbors if x[2].eats_plants == True]
          return prey
      def find_closest_prey(self,fov):
          prey = self.get_prey(fov)
          if prey == []: return []
          distances = [(self.dist(x[2]),x[0],x[1],x[2]) for x in prey]
          distances.sort()
          return [distances[0]]
      def get_directiontoward(self,x,y):
          if abs(x) > 1 : x = x / abs(x)
          if abs(y) > 1 : y = y / abs(y)
          if x == 0 : x = 1
          if y == 0 : y = 1
          return x  , y  
      def run(self):
          fov=self.getFOV()
          closest_prey = self.find_closest_prey(fov)
          if closest_prey != []:
              print closest_prey[0]
              x_move,y_move = self.get_directiontoward(closest_prey[0][1],closest_prey[0][2])
              print 'wolfmove' + repr(x_move) + ',' + repr(y_move) + '\n'
              self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move))
              print 'wolf ' + repr(self.x) + ',' + repr(self.y) + '\n'
          return (self.x,self.y)
