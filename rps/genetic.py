import constants
from random import *
import Queue
import math

## generate 100 random genomes
def make_genome(length):
	return [randint(0,2) for x in range(length)]

def crossover(g1, g2):
	split=randint(0,min(len(g1),len(g2)))
	g3=list(g1[:split]) + list(g2[split:])
	g4=list(g2[:split]) + list(g1[split:])
	return g3, g4

def mutation(genome):
	p=mutation_prob
	for i in range(len(genome)):
		if random()<p: genome[i]=randint(0,2)
	
def fitness(genome):
	return math.sin(sum(genome))

def select_ind(new_population):
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

def population_fitness(population):
	return [(fitness(g), g) for g in population]
				
def round(population):
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
		
def run():
	mutation_prob=0.05
	selection_size=0.5
	num_rounds = 10000
	population_size=100
	genome_size=50
	
	population = population_fitness([make_genome(genome_size) for x in range(population_size)])
	
	#generations=[]
	for r in range(num_rounds):
		#generations.append(population)
		population = round(population)
		
		print sum([x[0] for x in population])/float(population_size)
	
	return population
	
	