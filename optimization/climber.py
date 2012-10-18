from random import *
from math import *
import exceptions

dim=10
inc = 0.1
stop_delta=0.01
temperature=1
anneal_rate=0.001

weights=[randint(-100,100) for x in range(dim)]

def fitness(x):
	if len(x)!=dim: raise Exception('wrong dimensions on X')
	
	sum=0
	for i in range(dim):
		sum+=sin(weights[i]*x[i])
	#print sum
	return sum
		
def random_x():
	return([random() for z in range(dim)])
	
	

def anneal(x):
	""" make a small move in a direction that results in improvement in fitness"""
	global temperature

	index = randint(0,dim-1)
	x1 = list(x)
	x2 = list(x)
	x1[index]+=inc
	x2[index]-=inc
	f=fitness(x)
	f1=fitness(x1)
	f2=fitness(x2)

	temperature-=temperature*anneal_rate
	

	if f>f1 and f>f2: 
		if random()<temp: 
			x1[randint(0,dim-1)]+=2*inc
			return(x1,fitness(x1))
		else:
			return x,f
	elif f1>f2: 
		return x1,f1
	else:
		return x2,f2


def hillclimb(x):
	""" make a small move in a direction that results in improvement in fitness"""
	
	index = randint(0,dim-1)
	x1 = list(x)
	x2 = list(x)
	x1[index]+=inc
	x2[index]-=inc
	f=fitness(x)
	f1=fitness(x1)
	f2=fitness(x2)
	
	if f>f1 and f>f2: 
		return x,f
	elif f1>f2: 
		return x1,f1
	else:
		return x2,f2
		
def run(function):
	global temperature
	temperature = 1
	start = random_x()
	x=start
	
	
	surface = []
	
	while True:
		x,f=function(x)
		surface.append(f)
		print x,f
		if temperature < 0.1:
			delta=abs(surface[-1]-surface[-4])
			if delta < 1:
				return surface, x
			
		
	