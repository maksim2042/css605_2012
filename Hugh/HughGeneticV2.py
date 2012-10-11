###############
'''
CSS605 RPS Strategy Game
Hugh McFarlane
This version reads in a string that has the state transitions
The string is converted to a dict
After n-rounds, the strategy is evaluated based on total net score
The next round, the most successful strategy is mutated and then tested
if the mutation scores higher, it becomes the new source for the next mutation

Thus, this implementation only hill climbs based on finding the next best
option.

A more robust version tests several mutations, compares them and
then selects the best as the seed for the next round of mutations.

'''

import random
import matplotlib.pyplot as plt
import numpy as np

###############
#define globals
###############

GAME_MUTATIONS = 100 #number of mutations to try
GAME_ITERATIONS = 100 #number of games to play with each mutation
GAME_ROUNDS = 100 #number of time to play RPS in each game
NUM_MUTATIONS = 1 #number of alleals to change each mutation

START_STRATEGY_W = 'rrprpsrspprsppspsrsrpsprssr' #winner
START_STRATEGY_L = 'rrsrpsrspprspprpsrsrpsprssp' #loser
START_STRATEGY_OPP = 'rrrrpprssprrppppsssrrsppsss' #sequential
#rrs rps rsp prs ppr psr srp spr ssp
ROCK='r'
PAPER='p'
SCISSORS='s'

CHOICES=(ROCK, PAPER, SCISSORS)

####################
#define the payoffs
####################

PAYOFFS={}

for c in CHOICES:
	PAYOFFS[(c,c)]=(0,0)

PAYOFFS[(ROCK, PAPER)]=(-1,1)
PAYOFFS[(ROCK, SCISSORS)]=(1,-1)
PAYOFFS[(PAPER, SCISSORS)]=(-1,1)
PAYOFFS[(PAPER, ROCK)]=(1,-1)
PAYOFFS[(SCISSORS, ROCK)]=(-1,1)
PAYOFFS[(SCISSORS, PAPER)]=(1,-1)

#################################
# this is the basic player class
#################################

class Player(object):

	def __init__(self,initStrategy,id="noID"):
		self.myScore=0
		self.score_history=[]
		self.move_history=[]
		self.id=id
		self.strat = Strategy(initStrategy)

	def getID():
		return self.id

	def result(self, res, moves):
		self.move_history.append(moves)
		if res[0]==1: 
			self.myScore+=1
		elif res[0]==0:
			self.myScore+=0
		else:
			self.myScore-=1

	def go(self,lastPlay,lastOppPlay): #returns the next move based on strategy
		return self.strat.strategyDict[lastPlay][lastOppPlay]

##########
#This class holds the player strategies and records outcomes
##########

class Strategy(object):

	def __init__(self,startStrategy):
		self.strategyDict = {} # the dict with the current strategy
		self.states = [] #the possible states of the system
		self.transitions = [] #the triples with all transition info
		self.strategyRecord = [] #the record of top strategies and outcomes
		self.mutantRecord = [] #temporary record of the mutations tried
		self.topStrategy = startStrategy
		self.currentStrategy = startStrategy #the current strategy string
		self.currentScore = 0

	def makeStrategy(self):
	#Strategies are made from the current strategy string
	#returns dict of state transitions stored in triples:
	#d1 = current state/player's last move; 
	#d2 = opponent's last move
	#d3 = player's next move (next state)
		
		#clear the current strategy dict
		self.strategyDict.clear()
		
		#transitions = the 3 digit strings for each transition
		for i in range(len(self.currentStrategy)/3):
			self.transitions.append(self.currentStrategy[(i*3):(i*3)+3])

		#state = pull all the possible states out of the strings
		for i in range(len(self.transitions)): # go through each triple
			if self.transitions[i][0] not in self.states:
				self.states.append(self.transitions[i][0]) #add the state if not already recorded

		#start the strategy dict with the possible states
		for i in range(len(self.states)): # first put in the states and initialize them
			self.strategyDict[self.states[i]] = {}

		# add the transitions to possible states and complete the dict
		for i in range(len(self.transitions)): 
			self.strategyDict[self.transitions[i][0]].update({self.transitions[i][1]:self.transitions[i][2]})

	def mutateStrategy(self,numMutations): 
	#create a new strategy string by mutating the current best strategy
	#Only change the 3rd position (next state) in each triple
		self.currentStrategy = '' #clear out the current strategy
		changes = [] # a list of the alleals to mutate
		
		#mutate the reigning top strategy
		listStrat = list(self.topStrategy) #break apart the string
		
		#Get the alleals to mutate
		position=(random.randint(0,8)) #position = index to change
		changes.append(position) #first one assigned
		for i in range(numMutations): #get the rest
			while position in changes: #test to make sure its a different alleal
				position=(random.randint(0,8)) #keep getting numbers
			changes.append(position) #add the new alleal index to the list
		
		#Get the new states for the alleals and assign them
		for i in range(numMutations):
			mutation = random.choice(self.states) #get the first try
			while mutation == listStrat[(changes[i]*3)+2]: #test if it changed
				mutation = random.choice(self.states) #try again if no change
			listStrat[(changes[i]*3)+2] = mutation #record the change to the alleal

		#record the new strategy
		for i in range(len(listStrat)):
			self.currentStrategy += listStrat[i]
	
	def evaluatePerformance(self,mutNum):
		#looks for a more successful strategy than the current best
		#mutNum = the mutation number.
		numFail = 0 # count the intervening tries prior to a new success
		#The initial strategy results
		if len(self.strategyRecord) == 0:
			#record: 0 string, 1 score, 2 mutation#, 3 mutations since last success
			self.strategyRecord.append([self.currentStrategy,self.currentScore,1,1])
		
		#all the rest of the mutations. save the mutation,score, and mutation number
		else:
			if self.currentScore > self.strategyRecord[len(self.strategyRecord)-1][1]:
				numFail = (mutNum - self.strategyRecord[len(self.strategyRecord)-1][2])
				self.topStrategy = self.currentStrategy
				self.strategyRecord.append([self.currentStrategy,self.currentScore,mutNum,numFail])

####################
#Game Play Functions --- Turn this into a class ********************************
####################

def playRound(p1, p2, round):

	#Used if P1 is a finite state table player. Get last plays.
	if round == 0:
		move1 = CHOICES[random.randint(0,2)]
	else:
		p1Last = p1.move_history[len(p1.move_history)-1][0]
		p1OppLast = p1.move_history[len(p1.move_history)-1][1]
		move1=p1.go(p1Last,p1OppLast)
	
	#Used if P2 is a finite state table player. Get last plays.
	if round == 0:
		move2 = CHOICES[random.randint(0,2)]
	else:#fsm player
		p2Last = p2.move_history[len(p2.move_history)-1][0]
		p2OppLast = p2.move_history[len(p2.move_history)-1][1]
		move2=p2.go(p2Last,p2OppLast)
		#move2= CHOICES[random.randint(0,2)]
	#record results/scores
	result=list(PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])

def playGame(rounds,p1,p2):
	
	#initialize scores/moves for this game
	p1.myScore=0
	p1.move_history=[]
	
	p2.myScore=0
	p2.move_history=[]
	
	for i in range(rounds):
		playRound(p1,p2,i)

	p1.score_history.append(p1.myScore)

#############
#collect and plot data
#############

#subplot: numrows, numcols, fignum: 1 to numrows*numcols
def plotData(outcomes):
	means = []
	tries = []
	means = [outcomes[i][1] for i in range(len(outcomes))]
	tries = [outcomes[i][3] for i in range(len(outcomes))]

	plt.figure(1)
	
	plt.subplot(2,1,1)
    plt.xlabel('Strategy',fontsize = 10, color = 'blue')
    plt.ylabel('Winnings',fontsize = 10, color = 'blue')
    plt.title('Strategy Comparison')    
    x = np.arange(0,len(means),1)
    y = means
    plt.bar(x,y)
    
    plt.subplot(2,1,2)
    plt.xlabel('Num Inter Mutations',fontsize = 10, color = 'Red')
    plt.ylabel('Winnings',fontsize = 10, color = 'Red')
    plt.title('Punctuated EQ Analysis')    
    plt.hist(tries)
    
    plt.show()

###############
#Main Program: Play the game
###############

p1 = Player(START_STRATEGY_W,id="A") #Initialize the player with strategy string
p1.strat.makeStrategy() #Initialize strategy dict from string

p2 = Player(START_STRATEGY_L,id="B") #Initialize the opponent
p2.strat.makeStrategy() #Need to assign strategy ***************

#Play each mutation - make this a function *************************************
for runs in range(1):
	for i in range(GAME_MUTATIONS):
		for j in range(GAME_ITERATIONS): #Play n-iterations of the game
			playGame(GAME_ROUNDS,p1,p2) #Play n-rounds per game
	
		#Done testing strategy, record net winnings for all Iterations
		p1.strat.currentScore=np.sum(p1.score_history)
		#See if that was a new top strategy
		p1.strat.evaluatePerformance(i)
		#reset score history for next mutation
		p1.score_history=[] 
	
		#Mutate the top strategy and create dict
		p1.strat.mutateStrategy(NUM_MUTATIONS) #mutate NUM_MUTATIONS alleals
		p1.strat.makeStrategy() #create the new strategy dict

#plot outcomes
plotData(p1.strat.strategyRecord)