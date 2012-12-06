from gridworld import Patch
from parameters import params
from random import uniform

class Cell(Patch):
    max_produce = params['cell_max_produce']
    supply = params['cell_initial_supply']
    
    def produce(self):
        self.supply += uniform(0, self.max_produce)
    def provide(self, amount):
        amount = min(self.supply, amount)
        self.supply -= amount
        return amount

