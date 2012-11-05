"""
Defines a simple Referee class so that players have someone to play with
"""
import constants as c
import player as p
import random
from math import *
import Queue

def playRound(p1, p2):
	move1=p1.go()
	move2=p2.go()
	result=list(c.PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])

"""
Player 2 is FSMPlayer
"""

def playGame():
	for i in range(10):
		playRound(p1, p2)

	if p2.current_state == None:
		print "P2 is in the middle of nowhere"
	elif p2.current_state in p.sm.F:
		print " P2 is in the State:",current_state.__name__
	else:
		print " P2 is not in the State:",current_state.__name__

def GG():
	for g in p2.genomes:
		g = p2.move_value
		playGame()
		fit()
	
	pop_fit(p2.genomes)
	return pop_fit(p2.genomes)

def pop_fit(genomes):
	zipped = zip(t_score, genomes)
	return zipped

gen_score = []
def score():
	abc = [e[0] for e in p2.score_history]
	v = sum(abc)
	gen_score.append(v)

t_score=[]
def fit():
	score()

	for i in range(len(gen_score)):
		if i == 0:
			t = gen_score[i]
		else:
			t = gen_score[i] - gen_score[i - 1] 
		t_score.append(t)	

# g1=p2.genomes[0]
# g2=p2.genomes[1]

def crossover(g1, g2):
	split=randint(0,min(len(g1),len(g2)))
	g3=list(g1[:split]) + list(g2[split:])
	g4=list(g2[:split]) + list(g1[split:])
	return g3, g4


def mutation(genome):
	p=mutation_prob
	for i in range(len(genome)):
		if random.random() < p: genome[i]=randint(0,2)

def select_ind(new_population):
	weights = [f for f,g in new_population]
	s=float(sum(weights))+0.0001
	new_weights = [w/s for w in weights]
	prob = [sum(new_weights[:i+1]) for i in range(len(new_weights))]
	
	r1=random.random()
	for i in range(len(new_population)):
		if i==0: 
			if r1<prob[i]:
				return new_population[i]
		else:
			if r1>prob[i-1] and r1<prob[i]:
				return new_population[i]
	return new_population[-1:][0]

def population_fitness(population):
	zip_pop = zip(t_score, population)
	return zip_pop
				
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
		
		kid1, kid2  = crossover(mommy,daddy)
		
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
	p2.g=100
	genome_size=10
	
	population = pop_fit([p2.make_genome(genome_size) for x in range(p2.g)])
	
	#generations=[]
	for r in range(num_rounds):
		#generations.append(population)
		population = round(population)
		
		print sum([x[0] for x in population])/float(p2.g)
	
	return population		


"""
def pop_fit(genomes):
	for i in range(p2.g):
		return [ (fit(), g) for g in genomes]
def fit():
	abc = [e[0] for e in p2.score_history]
	v = sum(abc)
	return v
def pop_fit(genomes):
	for i in range(p2.g):
		return [ gen_score[i], g) for g in genomes]
def fit(g):
	for g in p2.genomes:
		abc = [e[0] for e in p2.score_history]
		v = sum(abc)
		return v
		del abc[:]
gen_score = []
def pop_fit(genomes):
	for i in range(p2.g):
		return [ (gen_score[i], g) for i in gen_score, for g in genomes ]
def fit():
	for i in range(p2.g):
		if i <1:
			abc = [e[0] for e in p2.score_history]
			v = sum(abc)
			gen_score.append(v)
		else:
			abc = [e[0] for e in p2.score_history if len(p2.score_history) >= (i * 10) ] # and len(p2.score_history) < ((i * 10) + 9)
			v = sum(abc)
			gen_score.append(v)
		# del abc[:]
def fit(g):
	for g in p2.genomes:
		abc = [e[0] for e in p2.score_history]
		v = sum(abc)
		gen_score.append(v)

def fit():
	for i in range(p2.g):
		gen_score.append(p2.myScore)

def fit():
	abc = [e[0] for e in p2.score_history]
	v = sum(abc)
	return v
"""





"""
ignore
oppmove = [e[0] for e in p2.move_history]	

"""