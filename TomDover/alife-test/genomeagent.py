from random import *
from math import *
import exceptions
import nk
import uuid
import environment as env
import agent

###Some of this genomeAgent is borrowed from Michael Palmer!!!

dim=256
e=env.Environment(dim)

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

standardAttributes = [
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
    return [randint(1,100) for x in standardAttributes]

class GenomeAgent(agent.Agent):
    def __init__(self,env,genome = random_genome(),species = "Thing-a-ma-jig",parents = None):
        self.id = str(uuid.uuid4()).split('-')[4]
        self.dim = len(genome)
        self.env = env
        self.x,self.y = self.returnBirthPlace(parents)
        self.genome = genome
        self.setStandardGenomeAttributes(genome)
        self.setInitialEnergy(genome,parents)
        self.age = 0
        self.alive = True
        self.species = species
        ### what do I eat?
        self.food_source='all' ### or 'prey' or 'all'
        self.consumption_rate=1

    ### These functions are part of the GenomeAgent class initialization.
    ### These functions come from Michael Palmer's implementation of the genomeagent.
    def returnBirthPlace(self,parents):
        if parents == None:
            x = randint(0,self.env.dim-1)
            y = randint(0,self.env.dim-1)
        else:
            x = parents[0].x
            y = parents[1].y
        return x,y

    def setStandardGenomeAttributes(self,genome):
        for attr in standardAttributes:
            funcName = attr[0]
            position = attr[1]
            getattr(self,funcName)(genome[position])  ###I DON"T UNDERSTAND THIS LINE!

    def setInitialEnergy(self,genome,parents):
        self.energy = 0.0
        if parents != None:
            parent0ChildCost = parents[0].energy_childbirth_delta
            parent1ChildCost = parents[1].energy_childbirth_delta
        else:
            parent0ChildCost = self.energy_childbirth_delta
            parent1ChildCost = self.energy_childbirth_delta
        self.energy = (parent0ChildCost * parent1ChildCost)

    ### These functions define characteristics and dynamic elements of the GenomeAgent class.
    ### These functions come from Michael Palmer's implementation of the genomeagent.
    def setMaxLife(self,value):
        self.max_lifespan = value #floor(value) ###I DON'T UNDERSTAND WHERE FLOOR() COMES FROM!

    def setVisionRadius(self,value):
        self.vision_radius = value #int(floor(sqrt(value)))

    def setMovementRate(self,value):
        self.movement_rate = value #floor(sqrt(value))

    def setChildBirthCost(self,value):
        self.energy_childbirth_delta = value #floor(sqrt(value))

    def setMatingCost(self,value):
        self.energy_mating_delta = value #floor(sqrt(value))

    def setMoveCost(self,value):
        self.energy_move_delta = value #floor(sqrt(value))

    def setStartSize(self,value):
        self.size = value #floor(sqrt(value))

    def setGrowthRate(self,value):
        self.growth_rate = float(value) / 1000.0

    def setEatsMeat(self,value):
        if value == 1:
            self.eats_meat = True
        else:
            self.eats_meat = False

    def setEatsPlants(self,value):
        if value == 1:
            self.eats_plants = True
        else:
            self.eats_plants = False

    def isSameSpecies(self,other):
        if self.species == other.species:
            return True
        else:
            return False

    def shouldDie(self):
        if self.energy<= 0 or self.age > self.max_lifespan:
            return True
        else:
            return False
        
    ### These functions are a series of heuristics to determine the agent's current priorities
    ### The priorities are listed as follows:
        ### Avoid Death by:
            ### moving away from other animals that are potentially hungry(DEFINE) meat-eaters,
            ### ensuring that energy does not fall to (or below) 0 by
                ### ensuring moving, mating, and giving birth are not fatal depletions of energy
                ### eating whatever it can if energy becomes critical(DEFINE)
        ### Increase Energy by:
            ### eating what is appropriate(DEFINE) when given the chance
            ### when encountering same species determine current energy condition and act appropriately
            ### increasing stores of energy to allow movement, mating, and childbirth
        ### Procreate by:
            ### determining energy levels will allow mating (and giving birth) and the agent is therefore looking for a mate
            ### determining if the animal encountered is the same species
            ### determining if the animal is not the same species, if it is compatible (DEFINE)        
        ### Write Poetry
            ### probably not going to happen this round...
        

    def inDanger(self): ### defines when in danger...
        if other.eats_meat == True and other.hungry() == True:
            return True
        else:
            return False

    def canMove(self,weak): ### defines when starving...
        if self.energy <= weak * 3:
            return False
        else:
            return True

    def canMate(self,impotent): ### defines when unable to mate...
        if self.energy <= impotent:
            return False
        else:
            return True

    def canBirth(self,birthing): ### defines when unable to give birth...
        if self.energy <= birthing:
            return False
        else:
            return True

    def hungry(self): ## defines an agent's hunger status
        if self.canMove(self,self.setMoveCost(value)) == False:
            return True
        elif self.canMate(self,self.setMateCost(value)) == False and self.species != other.species:
            return True
        
        
    def canMateWith(self,other):
        if len(self.genome) == len(other.genome):
            return True
        else:
            return False

    
    
        
    
                
