import agent as a
import random as r
import environment as env

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
    return [r.randint(1,100) for x in STANDARDATTRIBUTES]

def buildRabbit():
    rabbit = [
                r.randrange(10,20,1),
                r.randrange(10,20,1),
                r.randrange(60,70,1),
                r.randrange(3,9,1),
                r.randrange(3,9,1),
                r.randrange(3,9,1),
                r.randrange(2,5,1),
                r.randrange(2,4,1),
                0,
                1
                ]
    return rabbit
                
def buildWolf():
    wolf = [
                r.randrange(40,50,1),
                r.randrange(40,50,1),
                r.randrange(50,60,1),
                r.randrange(10,15,1),
                r.randrange(35,50,1),
                r.randrange(10,20,1),
                r.randrange(10,15,1),
                r.randrange(5,10,1),
                1,
                0
                ]
    return wolf
    
