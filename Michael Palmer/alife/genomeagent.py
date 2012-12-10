from random import *
from agent import Agent
from math import *
import exceptions
import uuid
from environment import Environment
from clock       import run

MAXLIFE    = 0
VISION     = 1
MOVERATE   = 2
CHILDCOST  = 3
MATECOST   = 4
MOVECOST   = 5
STARTSIZE  = 6
GROWTHRATE = 7
EATSMEAT   = 8
EATSPLANTS = 9
CONSUMPTIONRATE = 10


STANDARDATTRIBUTES = [
                             ('setMaxLife',MAXLIFE),
                             ('setVisionRadius',VISION),
                             ('setMovementRate',MOVERATE),
                             ('setChildBirthCost',CHILDCOST),
                             ('setMatingCost',MATECOST),
                             ('setMoveCost',MOVECOST),
                             ('setStartSize',STARTSIZE),
                             ('setGrowthRate',GROWTHRATE),
                             ('setEatsMeat',EATSMEAT),
                             ('setEatsPlants',EATSPLANTS),
                             ('setConsumptionRate',CONSUMPTIONRATE)
                     ]


def random_genome():
    return [ randint(1,100)   for x in STANDARDATTRIBUTES]


    

class GenomeAgent(Agent):
    def __init__(self, env, genome=random_genome(), species = 'Bug Eyed Monster',parents=None):
        self.id =str(uuid.uuid4()).split('-')[4]
        self.dim=len(genome)
        self.env=env

        self.parents = parents
        self.x,self.y = self.returnBirthPlace(parents)
        self.genome   = genome
        self.food_source = ''
        
        self.setStandardGenomeAttributes(genome)
        self.setInitialEnergy(genome,parents)
        self.age = 0
        self.alive = True

        self.species = species

        self.growth_energy_threshold=20


        

    def returnBirthPlace(self,parents):

        if parents == None:
           x = randint(0,self.env.dim-1)
           y = randint(0,self.env.dim-1)
        else:
           x = parents[0].x
           y = parents[1].y
        return x,y
    def getFOV(self):
        return self.env.getFOV(self.x,self.y,self.vision_radius)

    def dist(self,coords):
          return sqrt(abs(self.x - coords[0]) + abs(self.y - coords[1]))

    def setInitialEnergy(self,genome,parents):
        energy = 0.0
        if parents != None:
           parent0ChildCost = parents[0].energy_childbirth_delta
           parent1ChildCost = parents[1].energy_childbirth_delta
        else:
           parent0ChildCost = self.energy_childbirth_delta
           parent1ChildCost = self.energy_childbirth_delta

        self.energy      = (parent0ChildCost * parent1ChildCost) / 1.5

    def setStandardGenomeAttributes(self,genome):

        for attribute in STANDARDATTRIBUTES:
            funcName = attribute[0]
            position = attribute[1]
            getattr(self,funcName)(genome[position])

    def setConsumptionRate(self,value):
        self.consumption_rate = value / 10.0

    def setMaxLife(self,value):
        self.max_lifespan = floor(value)

    def setVisionRadius(self,value):
        self.vision_radius = int(floor(sqrt(value)))

    def setMovementRate(self,value):
        self.movement_rate = int(floor(sqrt(value)))

    def setChildBirthCost(self,value):
        self.energy_childbirth_delta = value

    def setMatingCost(self,value):
        self.energy_mating_delta = floor(sqrt(value))

    def setMoveCost(self,value):
        self.energy_move_delta = sqrt(value)/2

    def setStartSize(self,value):
        self.size = sqrt(value)/2.0

    def setGrowthRate(self,value):
        self.growth_rate = value / 1000.0

    def setEatsMeat(self,value):
        if value % 2 == 0:
            self.eats_meat = True
            self.food_source = 'prey'
        else:
            self.eats_meat = False

    def setEatsPlants(self,value):
        if value % 2 == 0:
            self.eats_plants = True
            if self.food_source == 'prey':
                self.food_source = 'all'
            else:
                self.food_source = 'env'
        else:
            self.eats_plants = False
        

    def isSameSpecies(self,otherAgent):

##        if len(self.genome) != len(otherAgent.genome):
##            return False
##        else:
##            diffs = sum([ abs(otherAgent.genome[x] - self.genome[x]) for x in range(len(self.genome))])
##            if diffs < 300:
##                return True
##            else:
##                return False
        if self.species == otherAgent.species: return True
        return False

    def shoulddie(self):
        if self.energy<=0 or self.age> self.max_lifespan: return True
        return False
    def get_prey(self,fov):
        neighbors = self.get_neighbors(fov)
        prey = [x for x in neighbors if x[2].food_source == 'env']
        return prey
    def get_same_species(self,fov):
        neighbors = self.get_neighbors(fov)
        same = [x for x in neighbors if self.isSameSpecies(x[2]) and x[2].id != self.id]
        return same
    def find_closest_same_species(self,fov):
        return self.find_closest(fov,self.get_same_species)
    def find_closest_prey(self,fov):
        return self.find_closest(fov,self.get_prey)
    def get_directiontoward(self,x,y):
        if x == 0 : x = 1
        if y == 0 : y = 1         
        if abs(x) > 1 : x = x / abs(x)
        if abs(y) > 1 : y = y / abs(y)
        return x  , y      
    def get_predators(self,fov):
        neighbors = self.get_neighbors(fov)
        predators = [x for x in neighbors  if (x[2].food_source == 'prey' or x[2].food_source=='all')]
        return predators
    def visible_predators(self):
        if len(self.get_predators(self.getFOV())) > 0: return True
        return False
    def visible_prey(self):
        if len(self.get_prey(self.getFOV()))>0 : return True
        return False
    def visible_same_species(self):
        if len(self.get_same_species(self.getFOV()))>0: return True
        return False
    def find_closest_predator(self,fov):
        return self.find_closest(fov,self.get_predators)
    def find_closest_food(self,fov):
        cells = self.get_food_cells(fov)
        if cells == []: return []
        distances = [ (self.dist((x[0],x[1])),x[0],x[1],x[2]) for x in cells]
        distances.sort()
        return [distances[0]]
    def find_closest(self,fov,func):
        animals = func(fov)
        if animals == []: return []
        distances = [(self.dist((x[2].x,x[2].y)),x[0],x[1],x[2]) for x in animals]
        distances.sort()
        return [distances[0]]        
    def get_directionaway(self,x,y):
        x,y = self.get_directiontoward(x,y)
        return x *-1 , y *-1            
    def move_to_mate(self,movement):
        while (movement > 0 and self.visible_same_species > 0):
            closest = self.find_closest_same_species(self.getFOV())
            if closest != [] and closest[0] > 0:
               x_move, y_move = self.get_directiontoward(closest[0][1],closest[0][2])
               self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
               movement -= 1
        return movement 
    def mate(self):
        miniFOV=self.env.getFOV(self.x,self.y,0)
        neighbors = self.get_neighbors(fov=miniFOV)
        for n in neighbors:
            if n[2].species == self.species and n[2].id !=self.id:
               #prevent incest
               print n[2].parents
               if (n[2].parents != None and self in n[2].parents) or (self.parents!=None and n[2] in self.parents):
                  continue
               self.mate_with_agent(n[2])
               return
    def mate_with_agent(self,agent):
        baby=self.__class__(self.env,self.genome,self.species,[self,agent])
        self.env.putAgent(baby)
        self.expend_energy(self.energy_mating_delta+self.energy_childbirth_delta) 
       



RABBIT = [ 10,
            9,
            9,
            10,
            4,
            1,
            1,
            1,
            1,
            2,
            10]

WOLF   = [ 10,
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




def test_rabbit():
   ev = Environment(10)
   rb = Rabbit(ev)
   ev.putAgent(rb)
   rb.run()

def test_wolf():
   ev = Environment(10)
   wf = Wolf(ev)
   ev.putAgent(wf)
   wf.run()

def test_moveforfood():
   ev = Environment(10)
   rb = Rabbit(ev)
   rb.x = 1
   rb.y = 1   
   ev.putAgent(rb)
   return run(ev)

   
def test_chase():
   ev = Environment(10)
   wf = Wolf(ev)
   rb = Rabbit(ev)
   rb.x = 1
   rb.y = 1
   wf.x = 3
   wf.y = 3
   ev.putAgent(rb)
   ev.putAgent(wf)
   return run(ev)

def test_movetosame():
   ev = Environment(10)
   rb = Rabbit(ev)
   rb1= Rabbit(ev)
   rb.x = 1
   rb.y = 1
   rb1.x = 3
   rb1.y = 3
   ev.putAgent(rb)
   ev.putAgent(rb1)
   return run(ev)

class Rabbit(GenomeAgent):
      def __init__(self,env,genome=RABBIT,species = 'rabbit',parents=None):
        super(Rabbit,self).__init__(env,genome,species,parents)
      def no_food(self):
        if self.env.env[self.x][self.y].has_key('food') and self.env.env[self.x][self.y]['food'] > 0: return False
        return True
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
            
      
      def move_towards_food(self,movement):
         while (movement > 0 and self.no_food()==True):
            closest = self.find_closest_food(self.getFOV())
            if closest != []:
               x_move, y_move = self.get_directiontoward(closest[0][1],closest[0][2])
               self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
               movement -= 1
         return movement
      
      def run(self):
          movement = self.movement_rate

          self.age += 0.1

          self.eat_grass()
          
          if self.visible_predators():
             movement = self.avoid_predators(movement)

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)         

          if self.no_food() and movement > 0:
             movement = self.move_towards_food(movement)

          self.eat_grass()

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)          

          if self.visible_same_species() and movement >0 :
             movement = self.move_to_mate(movement)
             self.mate()

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)

          
         

          print 'rabbit %s %s %s %s \n'%(self.id,self.x,self.y,self.energy)
          return (self.x,self.y)

          
class Wolf(GenomeAgent):
      def __init__(self,env,genome=WOLF,species = 'wolf'):
        super(Wolf,self).__init__(env,genome,species)   
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

          if self.visible_same_species() and movement >0 :
             movement = self.move_to_mate(movement)
             self.mate()

          if self.shoulddie() :
             self.die()            
          
          print 'wolf %s %s \n'%(self.x,self.y)
          return (self.x,self.y)


    
