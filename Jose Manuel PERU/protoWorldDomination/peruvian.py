import random
from gridworld import Agent, maximizers
from parameters import params

class Peruvian(Agent):
    def initialize(self):
        self.energy = params['agent_initial_energy']
        self.display(shape='circle', shapesize=(0.25,0.25))
        self.change_color()
        self.max_extract = self.world.agent_max_extract #from the slider!
    def sortsupply(self, cell):
        return cell.supply
    def move(self):
        choice = self.choose_location()
        self.position = choice
        self.change_energy()
    def choose_location(self):
        MyType = self.__class__
        hood = self.neighborhood('moore', 4)  #get the neighboring cells
        available = [cell for cell in hood if not cell.get_agents(MyType)]
        available.append(self.patch)          #agent can always stay put
        best_cells = maximizers(self.sortsupply, available)
        if self.patch in best_cells:
            return self.position
        else:
            return random.choice(best_cells).position
    def change_energy(self):
        self.energy += self.extract()
        self.change_color()
    def extract(self):
        mytake = self.patch.provide(self.max_extract)
        return mytake
    def change_color(self):
        g = b = max(0.0, 1.0 - self.energy/10)
        self.display(fillcolor=(1.0, g, b))