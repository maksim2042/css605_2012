'''
CSS 605 - Autumn 2012
David Masad

Rock Paper Scissors (Hawk Dove Collaborate Defect Spock Lizard...)
Player Classes

All players have at least the following methods:

__init__(self, action_list) -- Instantiate the player with the allowed actions.
go(self) -- Make a move
receive_score(self, score) -- Receive the results of a round and do something with them.

TODO: Edit the players so they have access to the payoff matrix and 
can figure out which move beats which.

TODO: Add the following players: SequencePlayer, Tit4Tat, Human, ML, Markov
'''

import random

class Player(object):
    '''
    Base class for the game player.
    '''

    def __init__(self, game):
        '''
        Instantiate a new player with a list of allowable actions.
        Args:
            action_list: the list of actions from the Game object
        '''
        self.game = game

    def go(self):
        '''
        Make a move.
        '''
        pass
    
    def receive_score(self, score):
        '''
        Get round result.
        '''
        pass

class FixedPlayer(Player):
    '''
    A player which picks a given action and then plays it always.
    '''

    def __init__(self, game, fixed_choice = None):
        '''
        Instantiate a new fixed player.

        Args:
            action_list: The list of actions from the game object
            fixed_choice: If given, the choice the player will always play
        '''
        self.game = game
        if fixed_choice is None or fixed_choice not in self.game.action_list:
            self.fixed_choice = random.choice(self.game.action_list)
        else:
            self.fixed_choice = fixed_choice

    def go(self):
        '''
        Always plays the same move.
        '''
        return self.fixed_choice

    def receive_score(self, score):
        '''
        Doesn't care, won't change.
        '''
        pass

class RandomPlayer(Player):
    '''
    A player who acts randomly every move.
    '''

    def __init__(self, game):
        '''
        Instantiate a RandomPlayer player.

        Args:
            game: A game object.
        '''

        self.game = game

    def go(self):
        '''
        Pick an action at random.
        '''
        action = random.choice(self.game.action_list)
        return action

    def receive_score(self, score):
        '''
        Doesn't care, won't change.
        '''
        pass

class SequencePlayer(Player):
    '''
    A player who plays a fixed sequence of actions.
    '''

    def __init__(self, game, cycle_length = 3):
        '''
        Args:
            cycle_length: The lenght of the player's fixed action sequence.
        '''
        self.game = game
        self.cycle = [random.choice(self.game.action_list) for i in range(cycle_length)]
        self.counter = 0

    def go(self):
        '''
        Pick the next action in the sequence. 
        '''
        action = self.cycle[self.counter % len(self.cycle)]
        self.counter += 1 
        return action

    def receive_score(self, score):
        '''
        Don't care, won't change.
        '''
        pass


class MLPlayer(Player):
    '''
    A player that uses simple learning to make the next move.
    '''

    def __init__(self, game):
        self.game = game
        self.action_outcomes = {}
        for action in self.game.action_list:
            self.action_outcomes[action] = 1

    def go(self):
        '''
        Choose an action based on the assigned weights
        '''
        action_list = []
        for action, weight in self.action_outcomes.items():
            for _ in range(weight): action_list.append(action)
        action = random.choice(action_list)
        self.last_action = action
        return action
    
    def receive_score(self, score):
        '''
        Modify action weights by score
        '''
        self.action_outcomes[self.last_action] += score

class HumanPlayer(Player):
    '''
    Interface for letting a human play.
    '''

    def __init__(self, game):
        self.game = game
        print "Welcome New Player"
        print "The available actions are: "
        print self.game.action_list
        print "The payoff matrix is: "
        for key, payoff in self.game.payoff_matrix.items():
            print "\t" + str(key) + ": " + str(payoff)

    def go(self):
        print "Your move!"
        while True:
            move = raw_input("Enter your action\n")
            if move not in self.game.action_list:
                print "Invalid move. Available moves are: "
                print self.game.action_list
            else:
                break
        return move

    def receive_score(self, score):
        print "Your score for the round is " + str(score)






