from random import *
from math import *
import matplotlib.pylab as plot

dim = 8
k=4
density=float(k)/(dim-1)

def random_genome():
	return ([randrange(-1,2,1) for z in range(dim)])

def toInt(genome):
	i=0
	sum=0
	for bit in genome:
		sum+=2**i*bit
		i+=1
	return sum	

def make_weight_matrix():
	matrix=[]
	for i in range(dim):
		row=[None for x in range(dim)]
		for j in range(dim):
			if random() < density:
				row[j]=randrange(-1,2,1)		
		matrix.append(row)
	return matrix

"""
		row=[None for x in range(dim)]
		row[i]=randrange(-1,2,1)
		if i>0:
			row[i-1] = randrange(-1,2,1)
		else:
			row[dim-1] = randrange(-1,2,1)

		if i < dim - 1:
			row[i+1]=randrange(-1,2,1)
		else:
			row[0]=randrange(-1,2,1)
		matrix.append(row)
	return matrix
"""

w=make_weight_matrix()
			
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

fitness(g,w)


x=[]
y=[]

for i in range(1000):
	g=random_genome()
	x.append(toInt(g))
	y.append(fitness(g,w))

plot.scatter(x,y)
plot.show()	


import csv
writer=csv.writer(open('genetic.csv', 'wb'))
for x in range(1000):
	g=random_genome()
	writer.writerrow(toInt(g), fitness(g,w))