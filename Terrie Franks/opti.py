'''
Terrie Franks
CSS 605, Fall 2012
October 24, 2012
'''

from random import *
from math import *
import exceptions
import matplotlib.pyplot as plot
import geneticAlgorithm as g

    
class Genetic(g.GA):
    def population_fitness(self, population):
        self.score = sum(self.population)
        
    def mutation(self, genome):
        self.genome = not self.genome


if __name__ == '__main__':
    
    g.run()
    plot.show()
    
    
    
        
