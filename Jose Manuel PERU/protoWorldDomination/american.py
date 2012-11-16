from random import shuffle, choice
from peruvian import Peruvian
from gridworld import Agent


class American(Agent):
    def initialize(self):
        self.display(fillcolor='yellow', shapesize=(0.75,0.75))
    def hunt(self):
        hunthood = self.neighborhood('moore', radius=1, keepcenter=True)
        shuffle(hunthood)
        change_position = True
        for patch in hunthood:
            hunters = patch.get_agents(AgentType=American)
            gatherers = patch.get_agents(Peruvian)
            if hunters and not self in hunters:
                change_position = False
                break
            elif gatherers:
                gatherers.pop().die()
                self.position = patch.position
                change_position = False
                break
        if change_position: #encountered no gatherers nor hunters
            newcell = choice(hunthood)
            self.position = newcell.position