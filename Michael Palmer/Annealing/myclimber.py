from random import *
from math   import *

dimensions = 10

def random_genome(size = dimensions, lowrange = 0.0, maxrange = 1.0):
    return [uniform(lowrange,maxrange) for x in range(size)]

def random_weights(size = dimensions, lowrange = -100, maxrange = 100):
    return [randint(lowrange,maxrange) for x in range(size)]

def sinfitness(x,weights):
    if len(x)!=len(weights): raise Exception('wrong dimensions')
    return sum([sin(weights[i] * x[i]) for i in range(len(x))])
	
def anneal(x,fitness,weights, inc =0.1, anneal_rate=0.001):    
	global temperature

	index = randint(0,len(x)-1)
	x1 = list(x)
	x2 = list(x)
	x1[index]+=inc
	x2[index]-=inc
	f=fitness(x,weights)
	f1=fitness(x1,weights)
	f2=fitness(x2,weights)

	temperature-=temperature*anneal_rate
	

	if f>f1 and f>f2: 
		if random()<temperature: 
			x1[randint(0,len(x)-1)]+=2*inc
			return(x1,fitness(x1,weights))
		else:
			return x,f
	elif f1>f2: 
		return x1,f1
	else:
		return x2,f2


def run_annealing(fitness,weights,size=dimensions):
	global temperature
	temperature = 1
	start = random_genome(size)
	x=start
		
	surface = []
	
	while True:
		x,f=anneal(x,fitness,weights)
		surface.append(f)

		if temperature < 0.1:
			delta=abs(surface[-1]-surface[-4])
			if delta < 1:
				return surface, x
