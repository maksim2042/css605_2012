import random as r
import constants as c


def build_rpspopulation(number,states,moves):
    return [build_randomrpsfsm(states,moves) for x in range(number)]

def build_randomrpsfsm(statecount,moves):
    movecount = len(moves)
    states = range(statecount)
    randomfsm = [[x, r.choice(moves), r.choice(states), r.choice(states),r.choice(states) ] for x in states]
    return randomfsm


def single_point(pone,ptwo,pcross = 0.7):
        cross = r.uniform(0,1)
        print cross
        cone = list(pone)
        ctwo = list(ptwo)
        if cross <= pcross:            
           pos = r.randint(1,len(pone) -1)
           print pos
           cone[0:pos] = pone[0:pos]
           cone[pos:len(pone)+1] = ptwo[pos:len(pone)+1]
           ctwo[0:pos] = ptwo[0:pos]
           ctwo[pos:len(pone)+1] = pone[pos:len(pone)+1]
        return cone,ctwo    
    
def mutate_rpsfsm(fsm, mutation_rate=0.015,moves=c.CHOICES):
      newfsm = []
      for x in fsm:
          mutate = r.uniform(0,1)
          if mutate <= self.mutation_rate:
             changespot = r.choice(range(1,5))
             if changespot == 1:
                 x[changespot] = r.choice(moves)
             else:
                 x[changespot] = r.choice(range(len(fsm)))
          newfsm.append(x)
      return newfsm