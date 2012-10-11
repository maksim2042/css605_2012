
'''
A Rock-Paper-Scissors-playing evolving finite state machine.
Probably generalizable, but written specifically for RPS for now.
'''
# -- Standard Library imports
from __future__ import division
import random
import copy

# -- Package imports --
import constants as c
from player import *
from referee import *

class FSM_Node(object):
    '''
    A single node in the finite state machine.
    Contains:
        Probabilities of playing Rock, Paper and Scissors
        Probabilities of transitioning to each other node on win
        Probabilities of transitioning to each other node otherwise
    '''

    def __init__(self, node_count):
        '''
        node_count: the constant number of nodes in the machine.
        '''
        self.node_count = node_count

        # Set initial probabilities as random:
        self.actions = [random.random() for choice in c.CHOICES]
        self.transition_win = [random.random() for node in range(self.node_count)]
        self.transition_lose = [random.random() for node in range(self.node_count)]

    
    def _weighted_choice(self, choice_weights):
        '''
        Chooses an index based on the weights in choice_weights
        '''

        total = sum(choice_weights)
        rand = random.random()*total
        counter = 0
        for index, weight in enumerate(choice_weights):
            if rand < counter + weight:
                return index
            else:
                counter += weight

    def get_action(self):
        '''
        Get the action randomly based on the node probabilities:
        '''
        choice = self._weighted_choice(self.actions)
        return c.CHOICES[choice]


    def mutate(self, mutation_probability, mutation_sd = 1):
        '''
        Iterate over each value, and mutate it with a certain probability.
        Args:
            mutation_probability: The probability of any given value being mutated
            mutation_sd: The standard deviation of the change in the random mutation
        '''

        for array in [self.actions, self.transition_win, self.transition_lose]:
            for i in range(len(array)):
                if random.random() < mutation_probability:
                    array[i] += array[i] * random.normalvariate(0, mutation_sd)

    def transition(self, win=True):
        '''
        Choose the index of the next node to transition to.
        Args:
            Win: Boolean; whether to use the transition_win or _lose probabilities.
        '''
        if win: transition = self.transition_win
        else: transition = self.transition_lose 
        return self._weighted_choice(transition)


class EvolvingFSM(object):
    '''
    A Finite State Machine capable of being evolved.
    '''

    def __init__(self, node_count):
        self.node_count = node_count
        self.nodes = [FSM_Node(node_count) for i in range(node_count)]
        self.current_node = random.choice(self.nodes)
        self.score = 0

    def go(self):
        return self.current_node.get_action()

    def result(self, result, move):
        self.score += result[0]
        if result[0] == 1: win = True
        else: win = False
        new_node = self.current_node.transition(win)
        self.current_node = self.nodes[new_node]

    def mutate(self, mutation_probability, mutation_sd = 1):
        '''
        Mutate all nodes
        '''
        for node in self.nodes:
            node.mutate(mutation_probability, mutation_sd)

    @staticmethod
    def crossover(agent1, agent2, crossover_point = None):
        '''
        Static class method for the one-point crossover of two agents.
        Args:
            agent1: The first EvolvingFSM agent to cross over
            agent2: the second EvolvingFSM agent to cross over
            crossover_point: number between 0, node_count designating where to cross
        Returns:
            Two children of the first generation, crossed over.
            e.g.:
                agent1: 0000|00
                agent2: 1111|11
                ---------------
                child1: 0000 11
                child2: 1111 00
        '''
        node_count = agent1.node_count
        child1 = EvolvingFSM(node_count)
        child2 = EvolvingFSM(node_count)

        if crossover_point is None:
            crossover_point = random.randint(0, agent1.node_count)

        for i in range(node_count):
            if i < crossover_point:
                child1.nodes[i] = copy.deepcopy(agent1.nodes[i])
                child2.nodes[i] = copy.deepcopy(agent2.nodes[i])
            else:
                child1.nodes[i] = copy.deepcopy(agent2.nodes[i])
                child2.nodes[i] = copy.deepcopy(agent1.nodes[i])
        return (child1, child2)

        

class EvolutionManager:
    '''
    God-class (no irony intended) to manage the evolution
    '''

    def __init__(self, evolving_agent_count, node_count, baseline_players):
        '''
        Args:
            evolving_agent_count: How many agents per generation
            node_count: nodes per agent
            baseline_players: a list of non-evolving player objects
                to compete against
        '''
        
        # Set evolutionary constants:
        # TODO: Tweak, and make dynamic
        self.GAMES_PER_GEN = 100 # Iterations per generation
        self.GENERATION_COUNT = 10 # Number of generations
        self.BASE_MUTATION_RATE = 0.2

        self.node_count = node_count
        self.generation = 0
        self.fitness_history = []
        self.current_generation = [EvolvingFSM(node_count) for i in range(evolving_agent_count)]
        self.baseline_players = baseline_players

    def run_generation(self):
        '''
        Runs the simulation for the current generation
        '''

        for i in range(self.GAMES_PER_GEN):
            opponent = random.choice(self.baseline_players)
            for player in self.current_generation:
                playRound(player, opponent)

    def advance_generation(self):
        '''
        Generate the next generation from the previous one.
        Keep all players that are above average, and then cross them at random.
        Then mutate.
        '''

        fitness = sum(player.score for player in self.current_generation)
        self.fitness_history.append(fitness)

        # Breed the agents:
        mean_score = fitness / len(self.current_generation)
        breeders = []
        next_generation = []
        for player in self.current_generation:
            if player.score > mean_score: breeders.append(player)
        
        while len(next_generation) < len(self.current_generation):
            parent1 = random.choice(breeders)
            parent2 = random.choice(breeders)
            child1, child2 = EvolvingFSM.crossover(parent1, parent2)
            next_generation.append(child1)
            next_generation.append(child2)
        self.generation += 1

        # ... and mutate:
        mutation_probability = self.BASE_MUTATION_RATE - self.generation / self.GENERATION_COUNT
        for player in next_generation:
            player.mutate(mutation_probability)
        self.current_generation = next_generation

    def evolve(self):
        while self.generation < self.GENERATION_COUNT:
            self.run_generation()
            self.advance_generation()






























