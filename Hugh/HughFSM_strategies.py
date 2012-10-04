import random
import matplotlib.pyplot as plt
import numpy as np

#define globals

GAME_ITERATIONS = 100

ROCK='ROCK'
PAPER='PAPER'
SCISSORS='SCISSORS'

CHOICES=(ROCK, PAPER, SCISSORS)

#define the payoffs
PAYOFFS={}

for c in CHOICES:
	PAYOFFS[(c,c)]=(0,0)

PAYOFFS[(ROCK, PAPER)]=(-1,1)
PAYOFFS[(ROCK, SCISSORS)]=(1,-1)
PAYOFFS[(PAPER, SCISSORS)]=(-1,1)
PAYOFFS[(PAPER, ROCK)]=(1,-1)
PAYOFFS[(SCISSORS, ROCK)]=(-1,1)
PAYOFFS[(SCISSORS, PAPER)]=(1,-1)

# this is the basic player object
class Player(object):

    def __init__(self, id="noID"):
        self.myScore=0
		self.score_history=[]
		self.move_history=[]
		self.id=id

	def getID():
		return self.id
	
	#def go(self):
		#return c.ROCK

	def result(self, res, moves):
		self.score_history.append(res)
		self.move_history.append(moves)
		if res[0]==1: 
			self.myScore+=1
			#print self.id, ":I WON!!! ", self.myScore
		elif res[0]==0:
			self.myScore+=0
			#print self.id, ':DRAW ', self.myScore
		else:
			self.myScore-=1
			#print self.id, ':I LOST :((( ', self.myScore

#This is the original player class - just plays random
class RandomPlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self, id)
	
	def go(self):
		choice=int(random.uniform(0,3))
		return(CHOICES[choice])

#This is the scissors only player
class constantPlayer(Player):
	def __init__(self, id="noID"):
		Player.__init__(self, id)
	
	def go(self):
		choice = 2 #scissors
		return(CHOICES[choice])

class fsPlayer(Player):

	def __init__(self, id="noID"):
		Player.__init__(self, id)

    def go(self,lastPlay,lastOppPlay):
        #each strategy reflect what the player played last
        #Each key is what the opponent played last
        #Each result is the players next play
        rockStrat = {'ROCK':PAPER,'PAPER':SCISSORS,'SCISSORS':PAPER}
        paperStrat = {'ROCK':SCISSORS,'PAPER':SCISSORS,'SCISSORS':ROCK}
        scissorStrat = {'ROCK':PAPER,'PAPER':ROCK,'SCISSORS':ROCK}

        if lastPlay == 'ROCK':
            return rockStrat[lastOppPlay]
        if lastPlay == 'PAPER':
            return paperStrat[lastOppPlay]
        if lastPlay == 'SCISSORS':
            return scissorStrat[lastOppPlay]

#Game Play Functions
def playRound(p1, p2, round):
    
    #Used if P1 is a finite state table player. Get last plays.
    if round == 0:
        move1 = ROCK #always start with rock
    else:
        p1Last = p1.move_history[len(p1.move_history)-1][0]
        p1OppLast = p1.move_history[len(p1.move_history)-1][1]
        move1=p1.go(p1Last,p1OppLast)
	
	move2=p2.go()
	result=list(PAYOFFS[move1,move2])
	p1.result(result,[move1,move2])
	result.reverse()
	p2.result(result,[move2,move1])

def playGame(rounds):
    for i in range(rounds):
        playRound(p1,p2,i)

#############
#collect and plot data
#############
def plotData(outcomes):
    plt.figure(1)
    #plt.subplot(2,1,2)
    plt.xlabel('Scores',fontsize = 10, color = 'green')
    plt.ylabel('Freq',fontsize = 10, color = 'green')
    plt.title('FSM_Strategy Results')
    plt.hist(outcomes)
    plt.show()
    
#Create Players
p1 = fsPlayer(id="A")
p2 = RandomPlayer(id="B")      

#Play the game
outcomes = []
for i in range(1000):
    playGame(GAME_ITERATIONS)
    outcomes.append(p1.myScore)

plotData(outcomes)

#Print Results
#print p1.myScore
#print p2.myScore
#print p1.move_history
#print p1.score_history

#print p2.move_history
#print p2.score_history

    
        