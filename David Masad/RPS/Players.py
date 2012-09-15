'''
CSS 605 - Autumn 2012
David Masad

Rock Paper Scissors (Hawk Dove Collaborate Defect Spock Lizard...)
Player Classes

All players have at least the following methods:

__init__(self, action_list) -- Instantiate the player with the allowed actions.
go(self) -- Make a move
receive_score(self, score) -- Receive the results of a round and do something with them.
'''

import random

class Player(object):
    '''
    Base class for the game player.
    '''

    def __init__(self, action_list):
        '''
        Instantiate a new player with a list of allowable actions.
        Args:
            action_list: the list of actions from the Game object
        '''
        self.action_list = action_list

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

    def __init__(self, action_list, fixed_choice = None):
        '''
        Instantiate a new fixed player.

        Args:
            action_list: The list of actions from the game object
            fixed_choice: If given, the choice the player will always play
        '''
        self.action_list = action_list
        if fixed_choice is None or fixed_choice not in self.action_list:
            self.fixed_choice = random.choice(self.action_list)
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

    def __init__(self, action_list):
        '''
        Instantiate a RandomPlayer player.

        Args:
            action_list: The list of actions from the game object
        '''
        self.action_list = action_list

    def go(self):
        '''
        Pick an action at random.
        '''
        action = random.choice(self.action_list)
        return action

    def receive_score(self, score):
        '''
        Doesn't care, won't change.
        '''
        pass


