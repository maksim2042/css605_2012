
from random import *
import exceptions

dim = 10
inc = .01

weights=[randint(-100,100) for x in range(dim)]

def fitness(x):
    if len(x) != dim:
        raise Exception("wrong dimensions on x")
    
    for i in range(0,dim):
        sum+=weights[i]*x[i]
        
    return sum
        
def random_x():
    return (random() for z in range(0,dim))

def hillclimb(x):
    #***make a small move in a direction that results in improvment in fitness***
    index = randint(dim)
    x1 = x2 =list(x)
    x1[index] += inc
    x2[index] += inc
    
    f1 = fitness(x1)
    f2 = fitness(x2)
    
    if f1 > f2:
        return x1
    else:
        return x2
    
def run():
    
    start = random_x()
    surface = []
    
    while True:
        x=hillclimb(x)
        surface.append(fitness(x))
        
        
    