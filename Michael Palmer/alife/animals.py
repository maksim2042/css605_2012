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
               2 ]
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
              1]
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
   return run([wf,rb])

class Rabbit(GenomeAgent):
      def get_predators(self,fov):
          neighbors = self.get_neighbors(fov)
          predators = [x for x in neighbors  if x[2].eats_meat == True]
          return predators
      def find_closest_predator(self,fov):
          predators = self.get_predators(fov)
          if predators == []: return []
          distances = [(self.dist(x[2]),x[2]) for x in predators]
          distances.sort()
          return [distances[0]]        
      def run(self):

          fov=self.getFOV()
          closest_predator = self.get_predators(fov)
          if closest_predator != []:
             self.move_away_from_agent(closest_predator[0][2])
          return (self.x,self.y)
          
class Wolf(GenomeAgent):
      def get_prey(self,fov):
          neighbors = self.get_neighbors(fov)
          prey = [x for x in neighbors if x[2].eats_plants == True]
          return prey
      def find_closest_prey(self,fov):
          prey = self.get_prey(fov)
          if prey == []: return []
          distances = [(self.dist(x[2]),x[2]) for x in prey]
          distances.sort()
          return [distances[0]]        
      def run(self):
          fov=self.getFOV()
          closest_prey = self.find_closest_prey(fov)
          if closest_prey != []:
              self.move_toward_agent(closest_prey[0][1])
          return (self.x,self.y)
