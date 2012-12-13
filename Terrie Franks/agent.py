'''
12-12-12
Max's and Michael Palmer's code
Terrie's code at bottom of file for roadrunner and coyote
12-6-12 code, which was before last change, has been commented out
'''

from random import *
from math import *
import exceptions
import nk
import uuid
from environment import Environment

ROADRUNNER = [10, 9, 9, 10, 3, 1,1,1,1,2, 10]

COYOTE = [ 10, 36, 9, 20, 20, 1, 16, 20,2,1,20]

class Agent(object):

    def __init__(self, env, x=None, y=None, genome=None, coords=None):
        self.id = str(uuid.uuid4()).split('-')[4]
        self.species = "critter"
        #self.species1 = ["rabbit", 1, "grass"]
        self.alive=True
        self.env = env
        self.inc = 0.1
        self.stop_delta=0.01
        self.temperature=1
        self.anneal_rate=0.001
        if genome == None:
            self.dim=env.dim
            self.genome=self.random_x()
        else:
            self.genome=genome
            self.dim=len(genome)
            
        #to do:  if born from parents, initialize to parents location
        if x is None:
            self.x = randint(0, env.dim-1)
            self.y = randint(0, env.dim-1)
        else:
            self.x = x
            self.y = y
        self.env.putAgent(self)
        
        #to do:  all of these initialized from genome
        self.energy = 100 #initial energy
        self.energy_move_delta = 1  #energy spent moving per unit of distance and elevation
        
        #energy for childbirth
        self.energy_mating_delta = 1
        self.energy_childbirth_delta = 10
        
        #max lifespan
        self.max_lifespan = 100
        
        #movement rate
        self.movement_rate = 3
        
        #vision radius
        self.vision_radius = 3
        
        #size
        self.size = 1
        self.growth_energy_threshold=20
        self.growth_rate=0.001
        
        #what do I eat
        self.food_source = 'env' #or prey or all
        self.consumption_rate=1
    
    def run(self):
        fov=self.getFOV()
        self.avoid_obstacles(fov)
        
        if self.energy == 0:
            self.die()
            return
            
        if self.energy > self.growth_energy_threshold:
            self.size += self.size*self.growth_rate
        
        # are there predators?
        self.i_am_scared()
        
        # am I hungry?
        self.i_am_hungry()
        
        # am I looking for a mate?
        self.i_want_a_baby()
        
        
        #check for neighbors; friend or foe?
        
        
        
       
    def avoid_obstacles (self, fov):
        obs=[]
        for x, row in enumerate (fov):
            for y, col in enumerate(row):
                if 'X' in col:
                    obs.append((x-self.vision_radius, y-self.vision_radius))
        x=sum([i[0] for i in obs])/2.0
        y=sum([i[1] for i in obs ])/2.0
        
        eu_dist=sqrt(x**2 + y**2)
        if eu_dist==0: eu_dist=1
        ratio=self.movement_rate/eu_dist
        new_x=int(x*ratio)
        new_y=int(y*ratio)
        
        return obs
    
    def getFOV(self):
        fov=self.env.getFOV(self.x, self.y, self.vision_radius)
        return fov
    
    def i_am_scared(self):
        neighbors = self.get_neighbors()
        for n in neighbors:
            if n[2].food_source == "prey" or n[2].food_source == 'all':
                self.move_away_from_agent(n)
                
    def i_am_hungry(self):
        if self.eat_grass() > 1: return
        fov=self.env.getFOV(self.x, self.y, self.vision_radius)
        
    def i_want_a_baby(self):
        
        neighbors = self.get_neighbors()
        for n in neighbors:
            if n[2].species == self.species:
                self.move_towards_agent(n[2])
        self.mate()
        
    def get_food_cells (self, fov=None):
        if fov == None: fov=self.getFOV()
        neighbors=[]
        for x, row in enumerate (fov):
            for y, col in enumerate (row):
                if 'food' in col:
                    neighbors.append((x-self.vision_radius, y-self.vision_radius, col ['food']))
        return neighbors
    
    def expend_energy(self, units):
        self.energy-=self.energy_move_delta*delta*units*self.size
        
    def get_neighbors (self, fov=None):
        if fov==None: fov=self.getFOV()
        neighbors=[]
        for x, row in enumerate(fov):
            for y, col in enumerate (row):
                if 'agents' in col:
                    for a in col['agents'].values():
                        neighbors.append((x-self.vision_radius, y-self.vision_radius, a))
        return neighbors
    
    def move_toward_agent(self, agent):
        x=(self.x+agent.x)/2
        y=(self.y+agent.y)/2
        self.expend_energy(self.env.moveAgent(self, x, y))
        
    def move_toward_cell(self,x,y):
        xx=(self.x+x)/2
        yy=(self.y+y)/2
        self.expend_energy(self.env.moveAgent(self, xx, yy))
        
        
    def move_away_from_agent(self, agent):
        x=self.env.wrap(self.x+ self.x-agent.x)
        y=self.env.wrap(self.y+self.y-agent.y)
        self.expend_energy (self.env.moveAgent(self, x, y))
                        
    #decide where to go   
    def move(self):
        #if self.vision_radius < 3:
         #   x= self.x+abs (self.x-agent.x)
          #  y = self.y + abs (self.y-agent.y)
           # self.env.moveAgent (self, x, y)
        pass
            
    
    def eat_grass(self):
        if self.env.env[self.x][self.y]['food']>self.consumption_rate:
            self.energy+= self.consumption_rate
            self.env.env[self.x][self.y]['food']-=self.consumption_rate
            
        return self.env.env[self.x][self.y]['food']
    
    def eat_critter(self, agent):
        self.energy+=agent.energy
        agent.die()
        env.removeAgent(agent)


#Terrie's code not used for Max's new implementation
    #consume the food at the current patch or if predator, consume at rate
#    def eat(self):
 #       if self.vision_radius < 1:
  #          if self.genome < 1:
   #if self.size <= 1:
    #                self.energy = +5 #energy from food
     #   else:
      #      self.energy = -1  #energy expended to run from potential prey                     
    
    def mate(self):
    # if next to me is a member of my species (ie genome match) > 70%
    # if next to me is another animal, fight with them
    # outcome is determined by the size and energy difference
        miniFOV=self.env.getFOV(self.x,self.y, 1)
        neighbors = self.get_neighbors(fov=miniFOV)
        for n in neighbors:
            if n[2].species == self.species:
                self.mate_with_agent(n[2])
                
    def mate_with_agent(self,agent):
        #perform genome crossover
        baby=self.__class__(self.env, x=self.x, y=self.y)
        self.env.putAgent(baby)
        self.expend_energy(self.energy_mating_delta+self.energy_childbirth_delta)
        
                
    def fight(self):
        pass
        # determine if anyone is next to your and determine if they are food and their size; if all matches then will eat and use 4 units of energy
#Terrie's code not used with Max's new implementation
       # if self.vision_radius < 1:
       #     if self.genome < 1:
        #        if self.size <= 1:
         #           self.energy = -4
                    
       # elif self.size > 1:
        #    self.energy = -1 #run and don't fight
            
       # else:
        #    if my_energy > other_energy:
         #       if my_size > other_size:
          #          self.energy +10
            
    
    #if next to me is a member of my species (genome match > 70%)    
   # def mate(self):
    #    if self.vision_radius <= 1:
     #       if self.my_genome == self.other_genome:
      #          self.energy_mating_delta
       #         self.energy_childbirth_delta
        #        self.new_genome
                    
        #self.x = random.randint(0, env.dim-1)
        #self.y = random.randint(0, env.dim-1)
        
    #did our energy run out or did we get eaten    
    def die(self):
        self.alive=False
        self.env.removeAgent(self)
        #if energy ==0:
         #   stop
    
    #return nk.fitness (x, self.weights)
    # return estimated value of changing my own genome
    def fitness(self, x):
        return 1
    
    def random_x(self):
        return([random() for z in range (self.dim)])
    
    # make a small move in a direction that results in improvement in fitness
    def anneal (self, x):
        
        index = randint(0,self.dim-1)
        x1=list(x)
        x2=list(x)
        x1[index] += self.inc
        x2[index]-=self.inc
        f=self.fitness(x)
        f1=self.fitness(x1)
        f2=self.fitness(x2)
        
        self.temperature-=self.temperature*self.anneal_rate
        
        if f>f1 and f>f2:
            if random()<temp:
                x1[randint(0,dim-1)]+=2*self.inc
                return (x1, fitness(x1))
            
            else:
                return x,f
            
        elif f1>f2:
            return x1, f1
        else:
            return x2, f2
        
    def hillclimb_agent(self):
        genome, fitness=self.hillclimb(self.genome)
        self.genome=genome
        return fitness
    
    def anneal_agent(self):
        genome,fitness=self.anneal(self.genome)
        self.genome=genome
        return fitness
    
    # make a small move in a direction that resulus in improvement in fitness
    def hillclimb(self, x):
        index = randint(0, self.dim-1)
        x1 = list (x)
        x2 = list(x)
        x1[index]+=self.inc
        x2[index]-=self.inc
        f=self.fitness(x)
        f1=self.fitness(x1)
        f2=self.fitness(x2)
        
        if f>f1 and f>f2:
            return x, f
        elif f1>f2:
            return x1, f1
        else:
            return x2, f2
 
class Roadrunner(Agent):
    def __init__ (self, env, genome=ROADRUNNER, species='roadrunner'):
        super (Roadrunner, self).__init__(env, genome, species)
        
    def run(self):
        if vision_radius < 2:
            sp1.move_away_from_agent()
            
        else:
            if vision_radius > 2:
                sp1.move_toward_agent()
            
            
        
        
class Coyote(Agent):
    def __init__ (self, env, genome=COYOTE, species = 'coyote'):
        super (Coyote, self).__init__(env, genome, species)
        
    def run (self):
        if vision_radius <2:
            sp2.move_toward_agent()
            
        else:
            if vision_radius >2:
                sp2.move_away_from_agent()
        

if __name__ == '__main__':
    env = Environment(10)
    sp1 = Roadrunner(env)
    sp2 = Coyote (env)
    env.putAgent(sp2)
    env.putAgent(sp1)
    sp1.run()
    sp2.run()
    
   
    
    
    
