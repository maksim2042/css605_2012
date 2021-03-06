'''
nk model
4 bits
'''
import random
import matplotlib.pyplot as plt
import numpy as np

N = 5
K = 2
RUNS = 10000

def dependencyMatrix(n,k):
    #n = string length
    #k = interdependencies
    d = [] # d = dependency matrix
    
    for i in range(n):
        t=[]
        j=0
        while j < k:
            r = random.randint(0,n-1) #r = random bit choice
            if r not in t and r != i:
                t.append(r)
                j += 1
        t.sort()
        d.append(t)
    return d

def weightMatrix(dmatrix,n,k):
    w=[] #weight matrix
    for i in range(n): #for each bit in the string
        zero=[] #if state is zero
        one=[] #if state is 1
        for j in range(2**(k)): #for each dependency in each bit in the string
            zero.append(random.uniform(0,1))
            one.append(random.uniform(0,1))
        w.append([zero,one])
    return w

def fitnessMatrix(dmatrix,wmatrix,n,k):
    f=[]
    
    for i in range(2**n): #Go through all the possible bit combination and covert base10 to binary
        #convert to a bit string
        x=i
        ts=[] # a temp string to store the weights for each bit in the gene string
        t=[0 for j in range(n)] #initialize the bit string
        for j in range(n):
            if x - (2**((n-1)-j)) >= 0:
                t[j] = 1 #put in the bits for the base 10 string
                x = x - (2**((n-1)-j))
        #take the gene in binary and get the weights for each bit and then add to the fitness matrix        
        
        for j in range(n): #each bit in turn
            state = t[j] #state of the bit we care about
            s = [] #holds the states of the bits that are dependent on the bit we care about
            for m in range(k): #pick out the states of the bits that are dependent
                s.append(t[dmatrix[j][m]]) #make it into a string
            #convert to an index
            wi=0
            for m in range((k-1),-1,-1):
                wi += (2**m) * s[(k-1)-m]
            
            #add weight to a temp string
            ts.append(wmatrix[j][state][wi])
        f.append(np.mean(ts))
    return f

def walkLandscape(strat,fmatrix):
    #convert to index and then get fitness
    index = 0
    strat.reverse()
    for i in range(len(strat)):
        index += (2**i) * strat[i]
    strat.reverse()
    return fmatrix[index]
    
def changeStrategy(strat):
    t=[strat[i] for i in range(len(strat))]
    bit = random.randint(0,len(strat)-1)
    new = np.mod(strat[bit]+1,2)
    t[bit] = new
    return t
####
#main
####

depMatrix = dependencyMatrix(N,K)
wtMatrix = weightMatrix(depMatrix,N,K)
ftMatrix = fitnessMatrix(depMatrix,wtMatrix,N,K)

data=[] #collect the number of tries before local max
for j in range(RUNS):
    strategy = [random.randint(0,1) for i in range(N)]
    history=[]
    best = 0
    bestStrat = strategy
    result = 0
    for i in range(100): #number of tries for each run
        result = walkLandscape(strategy,ftMatrix)
        if result > best:
            best = result
            bestStrat = strategy
            history.append([bestStrat,best])
    
        #print strategy, result, bestStrat, best #debug
        strategy=changeStrategy(bestStrat)
    data.append(len(history))

#p1=[]
#p1=[history[i][1] for i in range(len(history))]
plt.hist(data) #plot histogram of tries
plt.show()
    