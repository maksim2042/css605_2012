from random import *
from math import *

dim = 8

def random_genome():
	return([randrange(-1,2,1) for z in range(dim)])
	
def toInt(genome):
	i=0
	sum=0
	for bit in genome:
		sum+=2**i*bit
		i+=1
	return sum
	
def make_weight_matrix(density,d):
	global dim
	dim=d
	matrix=[]
	for i in range(dim):
		row=[None for x in range(dim)]
		for j in range(dim):
			if random() < density:
				row[j]=randrange(-1,2,1)
		matrix.append(row)
	return matrix
		
def fitness(genome,weights):
	f=0
	for row in range(dim):
		row_fitness=0
		#print genome[row],weights[row]
		for column in range(dim):
			if weights[row][column] is not None:
				row_fitness+=genome[row]*weights[row][column]
		#print row_fitness
		f+=row_fitness
	return f
	
			