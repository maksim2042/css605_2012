
from random import shuffle
from gridworld import Agent, moore_neighborhood
from parameters import params

class Bunny(Agent):

    def initialize(self):
        self.energy = params['agent_initial_energy']
        self.display(shape='circle', shapesize=(0.25,0.25))
        self.change_color()
        self.max_extract = self.world.agent_max_extract
        
    def move(self):
        choice = self.choose_location()
        self.position = choice
        
    def choose_location(self):
        old_position = self.position
        patchesInVision = moore_neighborhood(radius=4, center=old_position)
        shuffle(patchesInVision)
        for patch in patchesInVision:
            if  self.world.is_empty(patch):
                return patch
        return old_position
    
    def change_energy(self):
        self.energy += self.extract()
        self.change_color()
        
    def extract(self):
        mytake = self.patch.provide(self.max_extract)
        return mytake
    
    def change_color(self):
        g = b = max(0.0, 1.0 - self.energy/10)
        self.display(fillcolor=(1.0, g, b))

