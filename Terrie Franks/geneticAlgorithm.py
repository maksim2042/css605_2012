'''
Terrie Franks
CSS 605, Fall 2012
Genetic Algorithm using Max's code from 10-11-12 and activestate.com recipe as reference
'''


import Queue
from random import *
from math import *
import exceptions
import matplotlib.pyplot as plot

class GA(object):  
    #dim = 10
    #inc = 0.01
    #stop_delta = 0.01
    #weights = [randint(-100,100) for x in range (dim)]
    
    def __init__(self, dim=10, inc=0.01, stop_delta=0.01):
        self.dim = dim
        self.inc = inc
        self.stop_delta = stop_delta
        
    weights = [randint(-100,100) for x in range (dim)]
    
    def fitness(x):
        if len(x)!= dim: raise Exception('wrong dimension on x')  #check dim same length
        
        sum=0
        for i in range(dim):
            sum+=sin(weights[i]*x[i])  #change from linear to logr
    
        return sum
    
    def random_x():
        return([random() for z in range(dim)])
    
       
    def crossover (g1, g2):
        split = randint(0, min(len(g1), len(g2)))
        g3 = list(g1[:split]) + list (g2[split:])
        g4 = list (g2[:split]) + list (g1[split:])
        return g3, g4
        
    def mutation(genome):
        p=mutation_prob
        for i in range (len(genome)):
            if random()<p: genome[i]=randint(0,2)
    
    def select_ind(new_population):
        weights = [f for f, g in new_population]
        s= float(sum(weights))+0.0001
        new_weights = [w/s for w in weights]
        prob = [sum(new_weights[:i+1]) for i in range (len(new_weights))]
    
        r1 = random()
        for i in range (len(new_population)):
            if i==0:
                if r1<prob[i]:
                    return new_population[i]
            else:
                if r1>prob[i-1] and r1<prob[i]:
                    return new_population[i]
       
        return new_population[-1:][0]
    
    def population_fitness(population):
        return[(fitness(g), g) for g in population]
    
    def round(population):
        cutoff = int(len(population)*selection_size)
        new_population = list(sorted(population)[:cutoff])
    
    #create mating pairs and mate them; save the kids
        for i in range(int(len(new_population)/2)+1):
            mommy = select_ind(new_population)
            daddy = select_ind(new_population)
    
            mommy = mommy[1]
            daddy = daddy[1]
               
            kid1, kid2 = crossover(mommy, daddy)
            
            mutation(kid1)
            mutation(kid2)
                
            new_population.append((fitness(kid1), kid1))
            new_population.append((fitness(kid2), kid2))
            
        
        return new_population
    
def run():

    start = ()
    x = start
    
    while True:
        x, f =function(x)
        print x,f
           
'''
    mutation_prob=0.05
    selection_size=0.5
    num_rounds = 10000
    population_size = 100
    genome_size = 50

    population = population_fitness([make_genome(genome_size) for x in range(population_size)])

    for r in range(num_rounds):
        population = round(population)
    
        print sum([x[0] for x in population])/float(population_size)

    return population
'''

print 'testing geneticAlgorithm'
     
if __name__ == '__main__':
    plot.show()
    #run() 
   # fitness(random_x)



 


