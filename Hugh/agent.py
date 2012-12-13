from random import *
from math import *
import exceptions
import nk
import uuid

class Agent(object):
    
    def __init__(self, env, x=None, y=None, genome=None, coords=None):
        self.id=str(uuid.uuid4()).split('-')[4]
        self.species="honeyBadger"
        self.alive=True
        self.env=env
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
            
        if x is None:
            self.x = randint(0,env.dim-1)
            self.y = randint(0,env.dim-1)
        else:
            self.x=x
            self.y=y
        self.env.putAgent(self)
        
        
        
        #### TODO :: ALL OF THESE INITILIZED FROM GENOME
        self.energy = 100 * sum(self.genome) ### Initial energy
        ### how much energy do I spend moving about per unit of distance and elevation
        self.energy_move_delta = self.genome[-1] + self.genome[0]
        
        ### how much energy do I spend in mating and childbirth?
        self.energy_mating_delta = int(5 * self.genome[-2]) +1
        self.energy_childbirth_delta = int(5 * (self.genome[-2]+self.genome[-3])) +1
        
        ### what is my maximum lifespan?
        self.max_lifespan = int(75 + 75*self.genome[0]) +1
        
        ### what is my movement rate?
        self.movement_rate = int(2 *sum(self.genome)) +1
        
        ### what is my vision radius?
        if random() < self.genome[1]:
            self.vision_radius = 2
        else:
            self.vision_radius = 1
        
        ### what is my size
        self.size= 2 + 2 * self.genome[-1] +1
        self.growth_energy_threshold = self.size * 0.2 * self.genome[0]
        self.growth_rate=0.002
        
        ### what do I eat?
        self.food_source='all' ### or 'prey' or 'all'
        self.consumption_rate = 0.2 * self.size
    
    def run(self):
        fov=self.getFOV()
        obstacles = self.avoid_obstacles(fov)
        if self.energy == 0: 
            self.die()
            
        if self.energy > self.growth_energy_threshold: 
            self.size += self.size*self.growth_rate
        
        ### are there predators?
        self.i_am_scared()
            
        ### am I hungry?
        self.i_am_hungry()
        #print 'hungry'
        
        ### am I looking for a mate?
        self.i_want_a_baby()
        #print 'baby'
        
        ###Fight something
        self.fight()
        #print 'fight'
        
        ###Eat something
        if random()< 0.1:
            self.eat_critter()
        #print 'eat'
        
        ###Figure out where to move next
        self.move()
        #print 'move'
    
    def avoid_obstacles(self,fov):
        obs=[]
        for x,row in enumerate(fov):
            for y,col in enumerate(row):
                if 'X' in col:
                    obs.append((x-self.vision_radius,y-self.vision_radius))

        x=sum([i[0] for i in obs])/2.0
        y=sum([i[1] for i in obs])/2.0

        eu_dist=sqrt(x**2 + y**2)
        if eu_dist==0: eu_dist=1.0
        ratio=self.movement_rate/eu_dist
        new_x=int(x*ratio)
        new_y=int(y*ratio)
        
        return obs
    
    def getFOV(self):
        fov=self.env.getFOV(self.x,self.y,self.vision_radius)
        return fov

    def i_am_scared(self):
        neighbors = self.get_neighbors()
        if len(neighbors)>0:
            n = choice(neighbors)
            if n[2].species != self.species:
                if n[2].size > self.size:
                    self.move_away_from_agent(n[2])
    
    def i_am_hungry(self):
        if self.eat_grass() > 1: return

    def i_want_a_baby(self):
        neighbors = self.get_neighbors()
        if len(neighbors)>0:
            n = choice(neighbors)
            if n[2].species == self.species:
                self.mate(n[2])    
    
    def get_food_cells(self, fov=None):    
        if fov==None: fov=self.getFOV()
        neighbors=[]
        for x,row in enumerate(fov):
            for y,col in enumerate(row):
                if 'food' in col:
                    neighbors.append((x-self.vision_radius,y-self.vision_radius,col['food']))
        return neighbors

    def expend_energy(self,units):
        self.energy-=self.energy_move_delta*units*self.size
    
    def get_neighbors(self,fov=None):
        if fov==None: fov=self.getFOV()
        neighbors=[]
        for x,row in enumerate(fov):
            for y,col in enumerate(row):
                if 'agents' in col:
                    for a in col['agents'].values():
                        neighbors.append((x-self.vision_radius,y-self.vision_radius,a))
        return neighbors
        
    def move_toward_agent(self,agent):
        x=(self.x+agent.x)/2
        y=(self.y+agent.y)/2
        self.expend_energy(self.env.moveAgent(self,x,y))
        
    def move_toward_cell(self,x,y):
        xx=(self.x+x)/2
        yy=(self.y+y)/2
        self.expend_energy(self.env.moveAgent(self,xx,yy))
        
    def move_away_from_agent(self,agent):
        x = self.env.wrap(self.x+self.x-agent.x)
        y = self.env.wrap(self.y+self.y-agent.y)
        self.expend_energy(self.env.moveAgent(self,x,y))
    
    def move(self):
        neighbors = self.get_neighbors()
        if len(neighbors)>0:
            n = choice(neighbors)
        else:
            x = self.env.wrap(self.x+choice([-1,0,1]))
            y = self.env.wrap(self.y+choice([-1,0,1]))
            self.expend_energy(self.env.moveAgent(self,x,y))
        
        if n[2].species==self.species:
            self.move_toward_agent(n[2])
        else:
            if n[2].size>self.size:
                self.move_away_from_agent(n[2])
            else:
                self.move_toward_agent(n[2])

    def eat_grass(self):
        if self.env.env[self.x][self.y]['food']>self.consumption_rate:
            self.energy += self.consumption_rate
            self.env.env[self.x][self.y]['food']-=self.consumption_rate
            
        return self.env.env[self.x][self.y]['food']
    
    def eat_critter(self):
        
        neighbors = self.get_neighbors()
        if len(neighbors)>0:
            n = choice(neighbors)
            if self.size > n[2].size:
                print 'i win',self.id,n[2].id
                self.energy+=n[2].energy
                n[2].die()
                self.env.removeAgent(n[2])

    def mate(self,agent):
            if agent.energy > 0.9 * self.energy:
                self.mate_with_agent(agent)

    def mate_with_agent(self,agent):
        first = [self.genome[i] for i in range(int(len(self.genome)/2))]
        last = [agent.genome[i] for i in range(int(len(self.genome)/2),len(agent.genome),1)]
        newgenome = first+last
        
        baby=self.__class__(self.env,x=self.x,y=self.y,genome=newgenome)      
        self.expend_energy(self.energy_mating_delta+self.energy_childbirth_delta)

    def fight(self):
        neighbors=self.get_neighbors()
        if len(neighbors)>0:
            victim=choice(neighbors)
            if self.size > victim[2].size:
                victim[2].energy -= victim[2].energy_childbirth_delta
            else:
                self.energy -= self.energy_childbirth_delta

    def die(self):
        ### did our energy run out? or did we just get eaten?
        self.alive=False
        self.env.removeAgent(self)

    def fitness(self,x):
        return nk.fitness(x,self.weights)
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
            return (f)
        elif f1>f2: 
            return x1,f1
        elif f2>f1:
            return x2,f2
        else:
            return choice([f,f1,f2])


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
            return (f)
        elif f1>f2: 
            return x1,f1
        elif f2>f1:
            return x2,f2
        else:
            return choice([f,f1,f2])