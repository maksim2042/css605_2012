import random as r
import constants as c
import fsmv2 as f
import player as p
import referee as ref

def test():
   res = ga(300,50,8,10,f.fsmplayerfactory(f.TITFORTATPLAYER))
   res.sort()
   return res

def ga(generations,population,genomesize,rounds,fsmplayer):
    randompop = build_rpspopulation(population,genomesize,c.CHOICES)
    scored    = [ (getscore(x,fsmplayer,rounds),x) for x in randompop]
    for x in range(generations):
       scored.sort()
       scored.reverse()
       newpop = []
       newpop[0:population/2] = scored[0:population/2]
       while len(newpop) < population:
           p1 = select_ind(scored)[1]
           p2 = select_ind(scored)[1]
           p1,p2 = single_point(p1,p2)
           p1 = mutate_rpsfsm(p1)
           p2 = mutate_rpsfsm(p2)
           newpop.append((getscore(p1,fsmplayer,rounds),p1))
           newpop.append((getscore(p2,fsmplayer,rounds),p2))
       scored = newpop
       scores = sum( [x[0] for x in scored])
       print scores
           
    return scored

def select_ind(new_population):
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

def tournamentselect(population):
   p1 = r.choice(population)
   p2 = r.choice(population)
   choosebetter = r.uniform(0,1)
   better = [p1,p2]
   better.sort()
   if choosebetter < .98:
      return better[1][1]
   else:
      return better[0][1]

def getscore(genome,fsmplayer,rounds):
    gfsm = f.finitestatemachinev2()
    gfsm.addStates(0,genome)
    gplayer = f.FSMPlayer(gfsm)
    
    ref.playGame(gplayer,fsmplayer,rounds)
    return gplayer.myScore
    
def build_rpspopulation(number,states,moves):
    return [build_randomrpsfsm(states,moves) for x in range(number)]

def build_randomrpsfsm(statecount,moves):
    movecount = len(moves)
    states = range(statecount)
    randomfsm = [[x, r.choice(moves), r.choice(states), r.choice(states),r.choice(states) ] for x in states]
    return randomfsm


def single_point(pone,ptwo,pcross = 1):
        cross = r.uniform(0,1)
        cone = list(pone)
        ctwo = list(ptwo)
        if cross <= pcross:            
           pos = r.randint(1,len(pone) -1)
           cone[0:pos] = pone[0:pos]
           cone[pos:len(pone)+1] = ptwo[pos:len(pone)+1]
           ctwo[0:pos] = ptwo[0:pos]
           ctwo[pos:len(pone)+1] = pone[pos:len(pone)+1]
        return cone,ctwo    
    
def mutate_rpsfsm(fsm, mutation_rate=0.009,moves=c.CHOICES):
      newfsm = []
      for x in fsm:
          mutate = r.uniform(0,1)
          if mutate <= mutation_rate:
             changespot = r.choice(range(1,5))
             if changespot == 1:
                 x[changespot] = r.choice(moves)
             else:
                 x[changespot] = r.choice(range(len(fsm)))
          newfsm.append(x)
      return newfsm
