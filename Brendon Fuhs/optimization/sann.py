'''
Simulated Annealing
sann.py
10-24-12 Brendon Fuhs

usage: enter "optimize(testFitnessFun)"

I still need a slick way to deal with fitness functions that have non-infinite domains
'''

import random as r
import math as m

DIM = 10
WEIGHTIES = [r.random()*100 for i in range(DIM)]


# This is a test fitness function.
def testFitnessFun(x, sumulator=0):
    
    fitnesses = [  -( (x[i]+WEIGHTIES[i])**2 ) + WEIGHTIES[i] for i in range(len(x)) ]
    return sum(fitnesses)


# called by optimize. Using hotness to temper the mutation. This may or may not be a good idea.
def mutate(x, hotness):
    
    return [ r.gauss(a,m.log(1.01+hotness)) for a in x] 


# initGuess should be a list of floating point numbers
# fitnessFun should be a fitness functions that returns a scalar for guesses of the same form as initGuess
def optimize(fitnessFun, initGuess=None):

    if initGuess==None:
        initGuess = [r.random() for i in range(DIM)]
    hotness = 3 # This is tweakable
    
    bestGuess = lastGuess = initGuess
    lastFitness = bestFitness = fitnessFun(bestGuess)
    
    while True:
        thisGuess = mutate(lastGuess, hotness)
        thisFitness = fitnessFun(thisGuess)

        # Gives a chance to go downhill if hotness is hot or fitnesses are still close.
        if (thisFitness>lastFitness) or (r.random() < m.exp((thisFitness-lastFitness)/hotness)):
            lastGuess = thisGuess
            lastFitness = thisFitness
        
        hotness *= 0.999
        
        if (thisFitness > bestFitness):
            bestGuess = thisGuess
            bestFitness = thisFitness

        if hotness<=0.00000001: # Use temperature as stopping criteria
            return bestGuess




