
from random import *
from math import *
from csv import *
#import matplotlib.pyplot

dim = 8

def random_genome():
    return([randrange(-1,2,1) for z in range(dim)])

def toInt(genome):
    i=0
    sum = 0
    for bit in genome:
        sum += 2**i*bit
        i+=1
    return sum
        
def make_weight_matrix():
    matrix = []
    for i in range(dim):
        row = [None for x in range(dim)]
        row[i]=randrange(-1,2,1)
        if i>0:
            row[i-1]=randrange(-1,2,1)
        else:
            row[dim-1]=randrange(-1,2,1)
            
        if i<dim-1:
            row[i+1]=randrange(-1,2,1)
        else:
           row[0]=randrange(-1,2,1)
           
        matrix.append(row)
        
    return matrix


def fitness(genome,weights):
    f=0
    for row in range(dim):
        row_fitness=0
        for column in range(dim):
            if weights[row][column] is not None:
                row_fitness += genome[row]*weights[row][column]
        f+=row_fitness
        return f
    
        
g= random_genome()
w= make_weight_matrix()

print fitness(g,w)

writer = writer(open('genetic.csv', 'wb'))
for x in range(1000):
    g=random_genome()
    writer.writerow([toInt(g), fitness(g,w)])
    

        
        
        
        
        