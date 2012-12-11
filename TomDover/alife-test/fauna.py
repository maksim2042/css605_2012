from random import *
from math import *
import exceptions
import nk
import uuid
import environment as env
import agent
import genomeagent as g

dim=256
e=env.Environment(dim)
eats=[]

def buildRabbit():
    rabbit = [
                randrange(40,50,1),
                randrange(3,5,1),
                randrange(3,5,1),
                randrange(5,15,1),
                randrange(1,2,1),
                randrange(1,2,1),
                randrange(1,2,1),
                randrange(1,2,1),
                setDiet(0,1,95),
                setDiet(1,0,95)
                ]
    return rabbit
                
def buildWolf():
    wolf = [
                randrange(90,100,1),
                randrange(4,7,1),
                randrange(2,4,1),
                randrange(15,25,1),
                randrange(2,5,1),
                randrange(2,5,1),
                randrange(2,4,1),
                randrange(2,4,1),
                setDiet(1,0,75),
                setDiet(0,1,75)
                ]
    return wolf

def buildZipper():
    zipper = [
                randrange(60,70,1),
                randrange(5,10,1),
                randrange(2,5,1),
                randrange(5,15,1),
                randrange(1,3,1),
                randrange(1,3,1),
                randrange(1,2,1),
                randrange(3,5,1),
                setDiet(1,0,95),
                setDiet(0,1,5)
                ]
    return zipper

def setDiet(a,b,prob):
    eats=[]
    for x in range(prob):
        eats.append(a)
    for x in range(100-prob):
        eats.append(b)
    return choice(eats)

class Rabbit(g.GenomeAgent):
    def __init__(self,env,genome=buildRabbit(),species = "rabbit",parents = None):
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
        
class Wolf(g.GenomeAgent):
    def __init__(self,env,genome=buildWolf(),species = "wolf",parents = None):
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

class Zipper(g.GenomeAgent):
    def __init__(self,env,genome=buildZipper(),species = "zipper",parents = None):
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


    
