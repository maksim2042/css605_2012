import constants
import random as r
from player import *
import Queue
import math

 
class GeneticPlayer(Player):
  
    def __init__( self, id = "GeneticPlayer" ): 
	Player.__init__(self, id) 
	       
	self.mutation_prob=0.05
	self.selection_size=0.5
	#self.num_rounds = 10000
	self.population_size=100
	self.genome_size=100	
	
	#create initial population
	self.population = self.population_fitness([self.make_genome(self.genome_size) 
	                                      for x in range(self.population_size)])
	
	return  
	 
	 ## generate 100 random genomes
    def make_genome(self, length):
	return [r.randint(0,2) for x in range(length)]
	    
    def crossover(self, g1, g2):
	split=r.randint(0,min(len(g1),len(g2)))
	g3=list(g1[:split]) + list(g2[split:])
	g4=list(g2[:split]) + list(g1[split:])
	return g3, g4

    def mutation(self, genome):
	p=self.mutation_prob
	for i in range(len(genome)):
	      if r.uniform(0,1)<p: genome[i]=r.randint(0,2)
      
    #create a list that takes "RPS" and generates 0,2,1
    def rsp_to_int(self):
	dict = {'ROCK':0, 'PAPER':1, 'SCISSORS':2}
	myhistory = []
	for i in self.move_history:
	    v = dict[i[1]]
	    myhistory.append(v)
	
	return myhistory
      
	#generate genome fitness
    def fitness(self, genome):
	if len(self.move_history) == 0:
	    return 0
	else: 
	    myhistory = self.rsp_to_int()
	    count = 0
	    myRange = 0.01
	    for i in myhistory: 
		if i == genome[count]:
		    myRange += .01
		    
	    
	    return myRange
	 

	#select individual in new population
    def select_ind(self, new_population):
	 
	 weights = [f for f,g in new_population]
	 s=float(sum(weights))+0.0001
	 new_weights = [w/s for w in weights]
	 prob = [sum(new_weights[:i+1]) for i in range(len(new_weights))]
	 
	 r1=r.uniform(0,1)
	 for i in range(len(new_population)):
		if i==0: 
			if r1<prob[i]:
				return new_population[i]
		else:
			if r1>prob[i-1] and r1<prob[i]:
				return new_population[i]
			       
	 return new_population[-1:][0]
	
    #define population fitness
    def population_fitness(self, population):
	    return [(self.fitness(g), g) for g in population]
			    
    def round(self, population):
     cutoff = int(len(population)*self.selection_size)
     new_population = list(sorted(population)[:cutoff])

     ### now create mating pairs and mate them; save the kids
     for i in range(int(len(new_population)/2)+1):
	     mommy = self.select_ind(new_population)
	     daddy = self.select_ind(new_population)
	     #print mommy,daddy
	     mommy=mommy[1]
	     daddy=daddy[1]
	     
	     kid1,kid2  = self.crossover(mommy,daddy)
	     
	     self.mutation(kid1)
	     self.mutation(kid2)
	     
	     ##print kid1
	     
	     new_population.append((self.fitness(kid1), kid1))
	     new_population.append((self.fitness(kid2), kid2))
     
     return new_population
	    
    def go(self):
	 
	#generations=[]
	#for r in range(self.num_rounds):
	#generations.append(population)
	self.population = self.round(self.population)
	population_sorted = list(sorted(self.population))
	#print sum([x[0] for x in self.population])/float(self.population_size)
	pop_end =  population_sorted[-1][-1]
	
	if len(self.move_history) == 0:
	    return 'ROCK'
	else:
	    return 'SCISSORS'
 

     #return population

	
 