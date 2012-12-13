## Death-Bunny agent....
## By Tom Dover (CSS 605, 2012)
## Much of this code is adapted from Michael Palmer's implementation of the genomeagent!!!
##
## The Northern Death-Bunny is a close relative of the
## Notorious Killer Rabbit of Caerbannog.  While the Rabbit
## of Caerbannog is often noted to have "a vicious streak a mile wide," and has
## been documented with the ability to decapitate a grown man in a single strike
## of its "nasty, big, pointy teeth," its more temperate cousin, the Northern
## Death-Bunny is noted to only have "mildly iritated streak half-a-mile wide" and
## thus is slightly less motivated to rip the heads off of grown men
## while wiggling its cute little whiskery nose.  The Northern Death-Bunny,
## therefore, has always been regarded as the more tame of the two rodents.
##
## In recent years it has come to the attention of wildlife management specialists
## that cross-breeding between the two rodent populations may have at some point been possible.
## Although ever since the unfortunate "Holy Hand-Grenade Incident," which wiped out what was believed to
## be the last known Rabbit of Caerbannog, hopes for the survival of this rare and wonderful
## fauna appear to rest squarely on the fuzzy little head of the Northern Death-Bunny.   

from random import *
from math import *
import exceptions
import nk
import uuid
import environment as env
import agent



dim=256
e=env.Environment(dim)
eats=[]

### setting the diet of the Death-Bunny. Meat-eater and plant-eater are not mutually exlusive attributes
def setDiet(a,b,prob): 
    eats=[]
    for x in range(prob): eats.append(a)
    for x in range(100-prob): eats.append(b)
    return choice(eats)

###this portion of the Death-Bunny is borrowed from Michael Palmer's genomeagent

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

MOVES = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

### My version of building the Death-Bunny genome...
class DeathBunny(agent.Agent):
    def __init__(self,env,species = "death-bunny",parents = None):
        self.id = str(uuid.uuid4()).split('-')[4]
        self.genome = self.buildGenome(parents)
        self.dim = len(self.genome)
        self.env = env
        self.x,self.y = self.returnBirthPlace(parents)
        self.setStandardGenomeAttributes(self.genome)
        self.setInitialEnergy(self.genome,parents)
        self.setFoodSource()
        self.age = 0
        self.alive = True
        self.species = species
        self.consumption_rate=1
        self.parents = parents
        self.growth_energy_threshold=20

    def buildGenome(self,parents):
        if parents == None:
            genomesList=[]
            for i in range(1000):
                gen = [
                    randrange(60,70,1),
                    randrange(5,10,1),
                    randrange(2,5,1),
                    randrange(5,15,1),
                    randrange(1,3,1),
                    randrange(1,3,1),
                    randrange(1,2,1),
                    randrange(3,5,1),
                    setDiet(1,0,95), ### 95% probability the Death-Bunny will be a meat-eater
                    setDiet(1,0,50) ### 50% probability the Death-Bunny will like salad
                    ]
                genomesList.append(gen)
            return choice(genomesList)
        else:
            p1= parents[0].genome[0:(len(parents[0].genome)/2)]
            p2= parents[1].genome[(len(parents[1].genome)/2):len(parents[1].genome)]
            return p1 + p2

##    These functions are part of the GenomeAgent class initialization.
##    These functions adapted from Michael Palmer's implementation of the genomeagent.
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
            getattr(self,funcName)(genome[position])

    def setInitialEnergy(self,genome,parents):
        self.energy = 0.0
        if parents != None:
            parent0ChildCost = parents[0].energy_childbirth_delta
            parent1ChildCost = parents[1].energy_childbirth_delta
        else:
            parent0ChildCost = self.energy_childbirth_delta
            parent1ChildCost = self.energy_childbirth_delta
        self.energy = (parent0ChildCost * parent1ChildCost)

    ### This function determines the type of food the Death-Bunny eats 
    def setFoodSource(self):
        self.food_source = "unknown"
        m = self.eats_meat
        p = self.eats_plants
        if m == True and p == True:
            self.food_source = "all"
        elif m == True and p == False:
            self.food_source = "prey"
        elif m == False and p == True:
            self.food_source = "env"
        elif m == False and p == False:
            self.food_source = "nothing"
        else:
            self.food_source = "unknown"
        
##    These functions define characteristics and dynamic elements of the class.
##    These functions are adapted Michael Palmer's implementation of the genomeagent
##    with some tinkering in the variable equations.
            
    def setMaxLife(self,value):
        self.max_lifespan = value  

    def setVisionRadius(self,value):
        self.vision_radius = value 

    def setMovementRate(self,value):
        self.movement_rate = value 

    def setChildBirthCost(self,value):
        self.energy_childbirth_delta = value 

    def setMatingCost(self,value):
        self.energy_mating_delta = value 

    def setMoveCost(self,value):
        self.energy_move_delta = value 

    def setStartSize(self,value):
        self.size = value 

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

    def getFOV(self):
        return self.env.getFOV(self.x,self.y,self.vision_radius)

    def dist(self,coords):
        return sqrt(abs(self.x-coords[0]) + abs(self.y - coords[1]))

    def shouldDie(self):
        if self.energy<= 0 or self.age > self.max_lifespan:
            return True
        else:
            return False

    ### scanning the environment for prey items...
    def get_prey(self,fov):
        neighbors = self.get_neighbors(fov)
        prey = [x for x in neighbors]### will even eat other predators or its own species
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
        if x == 0 :
            x = 1
        if y == 0 :
            y=1
        if abs(x) > 1:
            x = x / abs(x)
        if abs(y) > 1:
            y = y / abs(y)
        return x,y

    #### Identify potential predators in the area
    def get_predators(self,fov):
        neighbors = self.get_neighbors(fov)
        predators = [x for x in neighbors if (x[2].food_source == "prey" or x[2].food_source == "all")]
        return predators

    ### the next three functions classify those agents within the FOV
    def visible_predators(self):
        if len(self.get_predators(self.getFOV())) > 0:
            return True
        else:
            return False

    def visible_prey(self):
        if len(self.get_prey(self.getFOV())) > 0:
            return True
        else:
            return False

    def visible_same_species(self):
        if len(self.get_same_species(self.getFOV())) > 0:
            return True
        else:
            return False

    ### the next three functions identify the closest food, threat, and potential mate
    def find_closest_food(self,fov):
        cells = self.get_food_cells(fov)
        if cells == []:
            return []
        distances = [(self.dist((x[0],x[1])),x[0],x[1],x[2]) for x in cells]
        distances.sort()
        return[distances[0]]

    def find_closest_predator(self,fov):
        return self.find_closest(fov,self.get_predators)

    def find_closest(self,fov,func):
        fauna = func(fov)
        if fauna == []:
            return []
        distances = [(self.dist((x[0],x[1])),x[0],x[1],x[2]) for x in fauna]
        distances.sort()
        return[distances[0]]

    ### determines direction of movement
    def get_directionaway(self,x,y):
        x,y = self.get_directiontoward(x,y)
        return x*-1,y*-1

    ### hitting on the mate...
    def move_to_mate(self_movement):
        while (movement > 0 and self.visible_same_species > 0):
            closest = self.find_closest_same_species(self.getFOV())
            if closest != [] and closest[0] > 0:
                x_move, y_move = self.get_directiontoward(closest[0][1],closest[0][2])
                self.expend_energy(self.env.moveagent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y+y_move)))
                movement -= 1
        return movement

    ### getting the mate in the mood...
    def mate(self):
        miniFOV=self.env.getFOV(self.x,self.y,0)
        neighbors = self.getneighbors(fov=miniFOV)
        for n in neighbors:
            if n[2].species == self.species and n[2].id !=self.id:
                printn[2].parents
                if (n[2].parents != None and self in n[2].parents) or (self.parents != None and n[2] in self.parents):
                    continue
                self.mate_with_agent(n[2])

    ### doing the deed...
    def mate_with_agent(self,agent):
        baby = self.__class__(self.env,self.species,[self,agent])
        self.env.putAgent(baby)
        self.expend_energy(self.energy_mating_delta + self.energy_childbirth_delta)

    ###allows the death-bunny to randomly move     
    def wander(self,movement,func):
        while(movement>0 and self.visible_same_species() == False and func() == False):
            x,y = choice(MOVES)
            self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x+x),self.env.wrap(self.y+y)))
            movement -= 1
        return movement

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
##  Allows the prey to react to a new, closer predator
##  Does not stop the prey from running back towards a previous predator
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

    def chase_prey(self,movement):
         while (self.visible_prey() and movement > 0):
            closest = self.find_closest_prey(self.getFOV())
            if closest != [] and closest[0][0] > 0.5:
                 x_move,y_move = self.get_directiontoward(closest[0][1],closest[0][2])
                 self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                 movement -= 1
            else :
                 self.attackprey(closest[0][3])
                 movement -= 1
         return movement
        
    def attackprey(self,agent):
          ratio = ((agent.energy / 10.0) + agent.size) / (((agent.energy / 10.0) + agent.size) + ((self.energy / 10) + self.size))
          attack = uniform(0,1)
          if attack > max(ratio,.80):
              self.energy += agent.size
              agent.die()
          else:
              print 'attack failed!!'
              
    def run(self):
          movement = self.movement_rate

          self.age += 0.1
          eat_now=None
        
          if self.food_source == "all":
              eat_now=choice(["prey","env"])
              
          if self.food_source == "prey" or eat_now == "prey":
              if self.visible_prey():movement = self.chase_prey(movement)
          elif self.food_source == "env" or eat_now == "env":
              self.eat_grass()
              if self.visible_predators():
                 movement = self.avoid_predators(movement)
              
          if self.shouldDie():
              self.die()
              return (self.x,self.y)

          if self.visible_same_species() and movement >0:
              movement = self.move_to_mate(movement)
              self.mate()

          if self.shouldDie():
              self.die()
              return(self.x,self.y)

          if self.food_source == "prey" or eat_now == "prey":
              if self.visible_prey() == False and self.visible_same_species() == False and movement > 0:
                 movement = self.wander(movement,self.visible_prey)
          elif self.food_source == "env" or eat_now == "env":
              if self.no_food() and movement > 0:
                 movement = self.move_towards_food(movement)

          if self.shouldDie() :
              self.die()
              return(self.x,self.y)

          if self.energy > self.growth_energy_threshold: 
              self.size += self.size*self.growth_rate
          
          print 'death-bunny'
          return (self.x,self.y)

##    These functions are a series of heuristics to determine the agent's current priorities
##    The priorities are listed as follows:
##        Avoid Death by:
##            moving away from other animals that are potentially hungry(DEFINE) meat-eaters,
##            ensuring that energy does not fall to (or below) 0 by
##               ensuring moving, mating, and giving birth are not fatal depletions of energy
##                eating whatever it can if energy becomes critical(DEFINE)
##        Increase Energy by:
##            eating what is appropriate(DEFINE) when given the chance
##            when encountering same species determine current energy condition and act appropriately
##            increasing stores of energy to allow movement, mating, and childbirth
##        Procreate by:
##            determining energy levels will allow mating (and giving birth) and the agent is therefore looking for a mate
##            determining if the animal encountered is the same species
##            determining if the animal is not the same species, if it is compatible (DEFINE)        
##        Write Poetry
##            probably not going to happen this round...
##        
##    The following six functions are some possibilities for Heuristics that have not yet been implemented
##
##    def inDanger(self,other): ### defines when in danger...
##        if other.eats_meat == True and other.hungry() == True:
##            return True
##        else:
##            return False
##
##    def canMove(self,weak): ### defines when starving...
##        if self.energy <= weak * 3:
##            return False
##        else:
##            return True
##
##    def canMate(self,impotent): ### defines when unable to mate...
##        if self.energy <= impotent:
##            #return False
##        else:
##            return True
##
##    def canBirth(self,birthing): ### defines when unable to give birth...
##        if self.energy <= birthing:
##            return False
##        else:
##            return True
##
##    def hungry(self): ## defines an agent's hunger status
##        if self.canMove(self,self.setMoveCost(value)) == False:
##            return True
##        elif self.canMate(self,self.setMateCost(value)) == False and self.species != other.species:
##            return True
##        
##        
##    def canMateWith(self,other):
##        if len(self.genome) == len(other.genome):
##            return True
##        else:
##            return False
    
def test_wander():
       e=env.Environment(dim)    
       db = DeathBunny(e)
       db.x = 8
       db.y = 6
       e.putAgent(db)
       return db.run()     
        
    
                
