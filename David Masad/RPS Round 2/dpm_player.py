import constants as c
import random
from player import *
import inspect
import copy


class Saboteur(Player):
    '''
    Actively sabotages all other players.
    '''

    def no_go(self):
        return c.ROCK

    def go(self):
        '''
        Replaces each other player's go() method with no_go()
        '''

        frm = inspect.stack()[1]
        all_objects = frm[0].f_globals

        for obj_name, obj in all_objects.items():
            if isinstance(obj, Player):
                if obj is not self:
                    obj.go = self.no_go

        return c.PAPER


class SkinWalker(Player):
    '''
    Steals the rival player object and uses it.
    '''

    def __init__(self, id="noID"):
        Player.__init__(self, id)
        self.internal_player = None

    def go(self):
        '''
        Search through the parent space to find another player, and 
        create a copy of it to use.
        '''
        frm = inspect.stack()[1]
        all_objects = frm[0].f_globals

        best_object = None

        for obj_name, obj in all_objects.items():
            if isinstance(obj, Player):
                if obj is not self:
                    if best_object is None: 
                        best_object = obj
                    elif obj.myScore > best_object.myScore:
                        best_object = obj

        if best_object.myScore > self.myScore:
            self.internal_player = copy.deepcopy(best_object)

        return self.internal_player.go()

    def results(self, res, moves):
        self.myScore += res[0]
        self.internal_player.results(res, moves)

class GreyArea(Player):
    '''
    Creates a copy of the rival object and interrogates it
    to find the best move.

    
    '''

    def weighted_choice(self, item_dict):
        '''
        Randomly choose an item from the dictionary keys,
        with probability weights given in the dictionary values.

        Args:
            item_dict: a dictionary of the form:
                {Item: weight, Item: weight}
                where Item can be any key, and the weights are numeric.
        '''
        total = sum(item_dict.values())
        choice = random.random() * total
        counter = 0
        for key, wgt in item_dict.items():
            if choice < counter + wgt: 
                return key
            else: 
                counter += wgt

    def go(self):
        other_players = []
        interrogation_length = 1000
        simulated_moves = {c.ROCK: 0, c.PAPER: 0, c.SCISSORS: 0}

        frm = inspect.stack()[1]
        all_objects = frm[0].f_globals

        for obj_name, obj in all_objects.items():
            if isinstance(obj, Player):
                if obj is not self:
                    other_players.append(copy.deepcopy(obj))

        # Generate simulated outcomes:
        for i in range(interrogation_length):
            for p in other_players:
                simulated_moves[p.go()] += 1
        # Pick most-likely player move:
        expected_move = self.weighted_choice(simulated_moves)
        # Pick response:
        if expected_move == c.ROCK:
            return c.PAPER
        elif expected_move == c.PAPER:
            return c.SCISSORS
        else:
            return c.ROCK

            







