import constants
import player as p
from random import *
import Queue
import math


class GeneticPlayer(p):

    def __init__(self, id = "no_ID"):
        Player.__init__(self, id)
        self.mutation_prob=0.05
        self.selection_size=0.5
	self.num_rounds = 10000
	self.population_size=100
	self.genome_size=50


    ## generate 100 random genomes
    def make_genome(self, length):
        return [randint(0,2) for x in range(length)]

    def crossover(self, g1, g2):
	split=randint(0,min(len(g1),len(g2)))
	g3=list(g1[:split]) + list(g2[split:])
	g4=list(g2[:split]) + list(g1[split:])
	return g3, g4

    def mutation(self, genome):
        p=self.mutation_prob
	for i in range(len(genome)):
		if random()<p: genome[i]=randint(0,2)

    def fitness(genome):
	return math.sin(sum(genome))

    def select_ind(self, new_population):
	weights = [f for f,g in new_population]
	s=float(sum(weights))+0.0001
	new_weights = [w/s for w in weights]
	prob = [sum(new_weights[:i+1]) for i in range(len(new_weights))]

	r1=random()
	for i in range(len(new_population)):
		if i==0: 
			if r1<prob[i]:
				return new_population[i]
		else:
			if r1>prob[i-1] and r1<prob[i]:
				return new_population[i]
	return new_population[-1:][0]

    def population_fitness(self, population):
	return [(fitness(g), g) for g in population]

    def round(self, population, selection_size):
	cutoff = int(len(population)*selection_size)
	new_population = list(sorted(population)[:cutoff])


	### now create mating pairs and mate them; save the kids
	for i in range(int(len(new_population)/2)+1):
		mommy = select_ind(new_population)
		daddy = select_ind(new_population)
		#print mommy,daddy
		mommy=mommy[1]
		daddy=daddy[1]

		kid1,kid2  = crossover(mommy,daddy)

		mutation(kid1)
		mutation(kid2)

		##print kid1

		new_population.append((fitness(kid1), kid1))
		new_population.append((fitness(kid2), kid2))

	return new_population

    def go(self):
	population = population_fitness([make_genome(self.genome_size) for x in range(self.population_size)])

	#generations=[]
	for r in range(self.num_rounds):
		#generations.append(population)
		population = round(population, self.selection_size)

		print sum([x[0] for x in population])/float(self.population_size)

	return population[self.population_size-1][1]


        
