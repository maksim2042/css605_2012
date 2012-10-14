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
	self.population_size=100
	self.genome_size=100 #interested to see if we can keep genome size small	
	self.count_next = 0	
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
	
	if len(self.score_history) == 0:
	    return 0
	
	curScore = 0
	# for now legs just measure wins
	for i in self.score_history:
	    if i[1] == 1:
		curScore += 1
	    
	if curScore != 0:
	    debug = curScore
	
	return curScore/(len(self.score_history)*1.0)
	 

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
	 
	dict = {0:'ROCK', 1:'PAPER', 2:'SCISSORS'}
	dict_inv = {'ROCK':0, 'PAPER':1, 'SCISSORS':2}
	
	self.population = self.round(self.population)
	population_sorted = list(sorted(self.population))
	#print sum([x[0] for x in self.population])/float(self.population_size)
	pop_end =  population_sorted[-1][-1]
	 
	if len(self.move_history) == 0:
	    return dict[0]
	else:
	    #start over from the beginning of the genome
	    if self.count_next >= len(pop_end): 
		self.count_next = 0
		'''
		# do some debugging
		 moves = []
		 for r in self.move_history:
		   moves.append(dict_inv[r[1]])
		 print moves
		 print pop_end
		'''	    # lets compare
 
	    return_next_move = next_rps_value = pop_end[self.count_next]
	    self.count_next+=1
	    return dict[return_next_move]
  
     #return population

	
 