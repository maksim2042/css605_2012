from random import *
from math import *
import exceptions
import nk
import uuid



class Agent(object):

    def __init__(self, env, genome=None, coords=None):
        self.id=str(uuid.uuid4()).split('-')[4]
        self.dim=len(genome)
        self.inc = 0.1
        self.stop_delta=0.01
        self.temperature=1
        self.anneal_rate=0.001
        if genome == None:
            self.genome=self.random_x()
        else:
            self.genome=genome

        #weights=[randint(-100,100) for x in range(dim)]
        #self.weights=w

        #### TODO :: IF BORN FROM PARENTS, INITIALIZE TO PARENTS LOCATION
        self.x = random.randint(0,env.dim-1)
        self.y = random.randint(0,env.dim-1)

        #### TODO :: ALL OF THESE INITILIZED FROM GENOME
        self.energy = 100 ### Initial energy
        ### how much energy do I spend moving about per unit of distance and elevation
        self.energy_move_delta = 1 

        ### how much energy do I spend in mating and childbirth?
        self.energy_mating_delta = 1
        self.energy_childbirth_delta = 10

        ### what is my maximum lifespan?
        self.max_lifespan = 100

        ### what is my movement rate?
        self.movement_rate = 1

        ### what is my vision radius?
        self.vision_radius = 3

        ### what is my size
        self.size=1
        self.growth_rate=0.01

        ### what do I eat?
        self.food_sorce='env' ### or 'prey' or 'all'
        self.consumption_rate=1


    def run(self):
        self.move()
        self.eat()
        self.fight()
        self.mate()
        if self.energy==0: self.die()

    def move(self):
        ### TODO: decide where to go
        pass
        
    def eat(self):
        ### TODO: consume the food at the current patch
        pass
        
        ### OR -- if I'm a predator -- consume my prey at the consumption rate
        
    def mate(self):
        ### if next to me is a member of my species (i.e. genome match > 70%)
        ### then we should mate and make babies
        pass
        
    def fight(self):
        ### if next to me is another animal, fight with them 
        pass
        ### the outcome is determined by the size and energy difference 
        
    def die(self):
        ### did our energy run out? or did we just get eaten?
        pass


    def fitness(self,x):
        #return nk.fitness(x,self.weights)
        ### return estimated value of changing my own genome
        return 1


    def random_x(self):
        return([random() for z in range(self.dim)])



    def anneal(self,x):
        """ make a small move in a direction that results in improvement in fitness"""

        index = randint(0,self.dim-1)
        x1 = list(x)
        x2 = list(x)
        x1[index]+=self.inc
        x2[index]-=self.inc
        f=self.fitness(x)
        f1=self.fitness(x1)
        f2=self.fitness(x2)

        self.temperature-=self.temperature*self.anneal_rate

        if f>f1 and f>f2: 
            if random()< self.temperature: 
                x1[randint(0,self.dim-1)]+=2*self.inc
                return(x1,self.fitness(x1))
            else:
                return x,f
        elif f1>f2: 
            return x1,f1
        else:
            return x2,f2


    def hillclimb_agent(self):
        genome,fitness=self.hillclimb(self.genome)
        self.genome=genome
        return fitness

    def anneal_agent(self):
        genome,fitness=self.anneal(self.genome)
        self.genome=genome
        return fitness

    def hillclimb(self,x):
        """ make a small move in a direction that results in improvement in fitness"""

        index = randint(0,self.dim-1)
        x1 = list(x)
        x2 = list(x)
        x1[index]+=self.inc
        x2[index]-=self.inc
        f=self.fitness(x)
        f1=self.fitness(x1)
        f2=self.fitness(x2)

        if f>f1 and f>f2: 
            return x,f
        elif f1>f2: 
            return x1,f1
        else:
            return x2,f2

"""
    def run(self,function):
        
        self.temperature = 1
        start = random_x()
        x=start    
        surface = []
        while True:
            x,f=function(x)
            surface.append(f)
            print x,f
            if self.temperature < 0.1:
                delta=abs(surface[-1]-surface[-4])
                if delta < 1:
                    return surface, x
"""