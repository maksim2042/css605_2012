from random import *
from math import *
import exceptions
import nk
import uuid



class Agent(object):
	
	def __init__(self, w):
		self.id=str(uuid.uuid4()).split('-')[4]
		self.dim=10
		self.inc = 0.1
		self.stop_delta=0.01
		self.temperature=1
		self.anneal_rate=0.001
		self.genome=self.random_x()

		#weights=[randint(-100,100) for x in range(dim)]
		self.weights=w

	"""
	def fitness(x):
		if len(x)!=dim: raise Exception('wrong dimensions on X')
	
		sum=0
		for i in range(dim):
			sum+=sin(weights[i]*x[i])
		#print sum
		return sum
	"""
	def fitness(self,x):
		return nk.fitness(x,self.weights)

		
	def random_x(self):
		return([random() for z in range(self.dim)])
	
	

	def anneal(self,x):
		""" make a small move in a direction that results in improvement in fitness"""
		
		index = randint(0,self.dim-1)
		x1 = list(x)
		x2 = list(x)
		x1[index]+=self.inc
		x2[index]-=self.inc
		f=self.fitness(x)
		f1=self.fitness(x1)
		f2=self.fitness(x2)

		self.temperature-=self.temperature*self.anneal_rate

		if f>f1 and f>f2: 
			if random()<temp: 
				x1[randint(0,dim-1)]+=2*self.inc
				return(x1,fitness(x1))
			else:
				return x,f
		elif f1>f2: 
			return x1,f1
		else:
			return x2,f2


	def hillclimb_agent(self):
		genome,fitness=self.hillclimb(self.genome)
		self.genome=genome
		return fitness
	
	def anneal_agent(self):
		genome,fitness=self.anneal(self.genome)
		self.genome=genome
		return fitness

	def hillclimb(self,x):
		""" make a small move in a direction that results in improvement in fitness"""
	
		index = randint(0,self.dim-1)
		x1 = list(x)
		x2 = list(x)
		x1[index]+=self.inc
		x2[index]-=self.inc
		f=self.fitness(x)
		f1=self.fitness(x1)
		f2=self.fitness(x2)
	
		if f>f1 and f>f2: 
			return x,f
		elif f1>f2: 
			return x1,f1
		else:
			return x2,f2


	def run(self,function):
		
		self.temperature = 1
		start = random_x()
		x=start	
		surface = []
		while True:
			x,f=function(x)
			surface.append(f)
			print x,f
			if self.temperature < 0.1:
				delta=abs(surface[-1]-surface[-4])
				if delta < 1:
					return surface, x
			
		
	