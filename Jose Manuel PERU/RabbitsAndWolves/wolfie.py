from random import shuffle, choice
from gridworld import Agent, moore_neighborhood
from parameters import params
from bunny import Bunny

class Wolf(Agent):
    def initialize(self):
        self.display(fillcolor='yellow', shapesize=(0.75,0.75))
    def hunt(self):
        huntVision = self.neighborhood('moore', radius=1, keepcenter=True)
        shuffle(huntVision)
        change_position = True
        for patch in huntVision:
            predators = patch.get_agents(Wolf)
            preys = patch.get_agents(Bunny)
            if predators and not self in predators:
                change_position = False
                break
            elif preys:
                preys.pop().die()
                self.position = patch.position
                change_position = False
                break
        if change_position: #encountered no gatherers nor hunters
            newcell = choice(huntVision)
            self.position = newcell.position