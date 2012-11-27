from random import *
from math import *
import exceptions
import uuid

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
                             ('setEatsPlants',EATSPLANTS)
                     ]


def random_genome():
    return [ randint(1,100)   for x in STANDARDATTRIBUTES]

class Agent(object):
    def __init__(self, env, genome=random_genome(), parents=None):
        self.id =str(uuid.uuid4()).split('-')[4]
        self.dim=len(genome)
        self.env=env
        self.env.agents.add(self)

        self.x,self.y = self.returnBirthPlace(parents)
        self.genome   = genome

        self.setStandardGenomeAttributes(genome)
        self.setInitialEnergy(genome,parents)

    def returnBirthPlace(self,parents):

        if parents == None:
           x = randint(0,self.env.dim-1)
           y = randint(0,self.env.dim-1)
        else:
           x = parents[0].x
           y = parents[1].y
        return x,y

    def setInitialEnergy(self,genome,parents):
        energy = 0.0
        if parents != None:
           parent0ChildCost = parents[0].energy_childbirth_delta
           parent1ChildCost = parents[1].energy_childbirth_delta
        else:
           parent0ChildCost = self.energy_childbirth_delta
           parent1ChildCost = self.energy_childbirth_delta

        self.energy      = parent0ChildCost * parent1ChildCost

    def setStandardGenomeAttributes(self,genome):

        for attribute in STANDARDATTRIBUTES:
            funcName = attribute[0]
            position = attribute[1]
            getattr(self,funcName)(genome[position])

    def setMaxLife(self,value):
        self.max_lifespan = floor(value)

    def setVisionRadius(self,value):
        self.vision_radius = floor(sqrt(value))

    def setMovementRate(self,value):
        self.movement_rate = floor(sqrt(value))

    def setChildBirthCost(self,value):
        self.energy_childbirth_delta = floor(sqrt(value))

    def setMatingCost(self,value):
        self.energy_mating_delta = floor(sqrt(value))

    def setMoveCost(self,value):
        self.energy_move_delta = floor(sqrt(value))

    def setStartSize(self,value):
        self.size = floor(sqrt(value))

    def setGrowthRate(self,value):
        self.growth_rate = value / 100.0

    def setEatsMeat(self,value):
        if value % 2 == 0:
            self.eats_meat = True
        else:
            self.eats_meat = False

    def setEatsPlants(self,value):
        if value % 2 == 0:
            self.eats_plants = True
        else:
            self.eats_plants = False
        

    def isSameSpecies(self,otherAgent):

        if len(self.genome) != len(otherAgent.genome):
            return False
        else:
            diffs = sum([ abs(otherAgent.genome[x] - self.genome[x]) for x in range(len(self.genome))])
            if diffs < 300:
                return True
            else:
                return False
            
            
    def run():
        self.move()
        self.eat()
        self.fight()
        self.mate()
        if self.energy<=0: self.die()
        
    def move(self):
        ### TODO: decide where to go
        pass
        
    def eat(self):
        ### TODO: consume the food at the current patch
        
        ### OR -- if I'm a predator -- consume my prey at the consumption rate
        pass
        
    def mate(self):
        ### if next to me is a member of my species (i.e. genome match > 70%)
        ### then we should mate and make babies
        pass
    def fight(self):
        ### if next to me is another animal, fight with them 
        ### the outcome is determined by the size and energy difference 
        pass
    def die(self):
        ### did our energy run out? or did we just get eaten?
        pass



    
