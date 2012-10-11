'''
Terrie Franks
CSS 605, Fall 2012

references:
Sean Luke, "Essentials of Metaheuristics"
Slides at http://webhome.cs.uvic.ca/~mgbarsky/DM_LABS/LAB_6/Lab6_genetic_algorithm.pdf
ActiveState Code at http://code.activestate.com/recipes/199121-a-simple-genetic-algorithm/
'''

import player
import random

population = 30

class Parent(object):
    def __int__ (self, child, best):
        self.child = child      #new sequence
        self.best = best        #the best sequence
        
    def crossover(p1, p2):
        i = random.randint(1, target_length-2)
        return p1[0: i] +p2[i: ]
        
    def fitness(child):
        fitness = 0
        
        for i in range (0, target_length):
            fitness+= abs (ord (child [i])
                            - ord (TARGET_STRING [i]))
        return fitness

    def run(self):
        while not self._goal():
            self.step()
 
    def report(self):
        print "generation:", self.child
        print "best:", self.best
        
class genAlg (Parent):
    
    def optimize (population, fitness, best, crossover, maxiterations):
        firstPopulation = len(population)
        topBest = int (best*firstPopulation)
        
        for i in range (maxiterations):
            parent_scores = [ (fitness (v), v)
                for v in population]
            
            parent_scores.sort()
            ranked_parent=[v for (s, v) in child_scores]
            
            population = ranked_child [0:topBest]

        
#try this
    while len(population)<firstPopulation:
        if random.random () <crossover:
            
            c=random.randint (0, top_best)
            population.append( crossover (ranked_child[c]))
            
        else:
            c1=random.randit(0, top_best)
            c2= random.randing (0, top_best)
            
    if child_scores[0][0] ==0:
        #return child_scores [0][1]
#return child scores[0][1]


if __name__ == '__main__':
    x = genAlg ()
    x.run()
    
    while playerTypeOption == True:
                playerList.insert (0, p.SequencePlayer())
    