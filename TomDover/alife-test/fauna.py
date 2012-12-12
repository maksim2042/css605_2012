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

def setDiet(a,b,prob):
    eats=[]
    for x in range(prob): eats.append(a)
    for x in range(100-prob): eats.append(b)
    return choice(eats)

class Rabbit(g.GenomeAgent):
    def __init__(self,env,species = "rabbit",parents = None):
        self.id = str(uuid.uuid4()).split('-')[4]
        self.genome = self.buildGenome()
        self.dim = len(genome)
        self.env = env
        self.x,self.y = self.returnBirthPlace(parents)
        self.genome = genome
        self.setStandardGenomeAttributes(self.genome)
        self.setInitialEnergy(self.genome,parents)
        self.setFoodSource()
        self.age = 0
        self.alive = True
        self.species = species

    def buildGenome(self):
        genomesList=[]
        for i in range(1000):
            gen = [
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
            genomesList.append(gen)
        return choice(genomesList)                    
        
class Wolf(g.GenomeAgent):
    def __init__(self,env,species = "wolf",parents = None):
        self.id = str(uuid.uuid4()).split('-')[4]
        self.genome = self.buildGenome()
        self.dim = len(genome)
        self.env = env
        self.x,self.y = self.returnBirthPlace(parents)
        self.genome = genome
        self.setStandardGenomeAttributes(self.genome)
        self.setInitialEnergy(self.genome,parents)
        self.setFoodSource()
        self.age = 0
        self.alive = True
        self.species = species

    def buildGenome(self):
        genomesList=[]
        for i in range(1000):
            gen = [
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
            genomesList.append(gen)
        return choice(genomesList)

class Zipper(g.GenomeAgent):
    def __init__(self,env,species = "zipper",parents = None):
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
                    setDiet(1,0,95),
                    setDiet(0,1,5)
                    ]
                genomesList.append(gen)
            return choice(genomesList)
        else:
            p1= parents[0].genome[0:(len(parents[0].genome)/2)]
            p2= parents[1].genome[(len(parents[1].genome)/2):len(parents[1].genome)]
            return p1 + p2
        
        

                
        
        
    


    
