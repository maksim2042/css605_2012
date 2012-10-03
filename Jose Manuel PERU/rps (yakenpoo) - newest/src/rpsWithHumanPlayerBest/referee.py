'''
Created on Sep 28, 2012
0 is for ROCK, 1 is for PAPERS, 2 is for SCISSOR
@author: josemagallanes
'''
import players as p
import constants as c

class Game(object):
    players=[]
    def __init__(self, players,payoffmat=c.PAYOFFS):
        # initialize instance attributes
        self.players = players
        self.payoffmat = payoffmat
        self.moveHistory = list()
        self.scoreHistory = list()
        
    def run(self, game_iter=2):
        player1,player2=players
        for iteration in range(game_iter):
            move1,move2 = ( player1.strategy(),player2.strategy())
            print '%s: %s and %s: %s ' %(player1.name, move1, player2.name,move2)
            self.moveHistory.append((move1,move2))
        
        player1.record(); player2.record() # prompt players to record the game played (i.e., 'self')

    def payoff(self):
        payoffs = (c.PAYOFFS[move1,move2] for (move1,move2) in self.moveHistory) # generate a payoff pair EACH ITER
        payoffs1, payoffs2 = zip(*payoffs)
        player1,player2=players
        return {player1:payoffs1, player2:payoffs2}
# create and run the game
players = [p.PlayerRandom('JIM'), p.PlayerHuman()] 
game = Game(players)
game.run(4)
# retrieve and print the payoffs
payoffs = game.payoff()
player1, player2=players
print "%s obtained %s which totals %d" %(player1.name, payoffs[player1],sum(payoffs[player1])) 
print "%s obtained %s which totals %d" %(player2.name, payoffs[player2], sum(payoffs[player2])) 

