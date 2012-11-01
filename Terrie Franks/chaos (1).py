
''''
Terrie Franks
CSS 605 Fall 2012
NK Model

'''

import matplotlib.pylab as plot
import numpy as np
from random import *
from math import *

#changed dim and k from 8 and 4, respectively
dim=15
k=20
density=float(k)/(dim-1)

#added weights to be random numbers (same as used in genetic algorithm)
weights = [randint(-100,100) for x in range (dim)]

#changed the genome to be random
#def random_genome():
#    return([randrange(-1, 2,1) for z in range(dim)])

def random_genome():
    return([random() for z in range (dim)])


def toInt(genome):
    i = 0
    sum = 0
    for bit in genome:
        sum+=2**i*bit
        i=+1
    return sum
        
def make_weight_matrix():
    matrix = []
    for i in range(dim):
        row=[None for x in range (dim)]
        for j in range(dim):
            if random() < density:
                row[j]=randrange(-1,2,1)
        matrix.append(row)
    return matrix

#w = make_weight_matrix()

def fitness(genome, weights):
    f=0
    for row in range(dim):
        row_fitness=0
        print genome[row], weights[row]
        for column in range(dim):
            if weights[row][column] is not None:
                row_fitness+=genome[row]*weights[row][column]
        f+=row_fitness
        print row_fitness
    return f


if __name__ == '__main__':
    g=random_genome()
    toInt(g)
    #dim = 10
    
    w=make_weight_matrix()
      
    
    fitness(g,w)

x=[]
y=[]

for i in range(1000):
    g=random_genome()
    x.append(toInt(g))
    y.append(fitness(g,w))

#got matplotlib to work and added title    
plot.scatter(x,y)
plot.title ('NK Model')
plot.show()


    



