
'''
CSS 605 - Autumn 2012
David Masad

Rock Paper Scissors (Hawk Dove Collaborate Defect Spock Lizard...)
Referee Class

'''
import itertools
from collections import defaultdict
from Game import *
from Players import *


class Referee:
    '''
    The Referee class is used to actually manage the game.

    TODO: Allow more sophisticated player matchups.
    '''

    def __init__(self, game = None, number_of_rounds = 10):
        '''
        Instantiate a new referee object.

        Args:
            game: A Game object describing the game to be refereed.
            number_of_rounds: How many rounds to play.

        '''

        if game is None:
            self.game = Game()
        else:
            self.game = game

        self.players = []
        self.number_of_rounds = number_of_rounds

    def add_player(self, player):
        '''
        Add a player to the game.
        
        Args:
            player: a Player object
        '''

        self.players.append(player)

    def play_game(self):
        '''

        '''

        player_scores = defaultdict(int)

        for round in range(self.number_of_rounds):
            for player1, player2 in itertools.combinations(self.players, 2):
                results = self.game.resolve(player1.go(), player2.go())
                
                player1.receive_score(results[0])
                player2.receive_score(results[1])

                player_scores[player1] += results[0]
                player_scores[player2] += results[1]

        # Output scores:
        for i, score in enumerate(player_scores.values()):
            print "Player " + str(i) + ": " + str(score)







        

