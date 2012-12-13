from random import *
from math import *
import exceptions
import nk
import uuid

class Edible_Amoeba(Agent):
    def __init__(self, env, x=None, y=None, Coords=None):
        Agent.__init__(self, id)
        self.energy_reproduce = 5
        self.food_source='all'

    def i_want_a_baby(self):
        baby1=self.__Edible_Amoeba__(self.env, x=self.x, y=self.y)
        baby2=self.__Edible_Amoeba__(self.env, x=self.x, y=self.y)
        self.env.putAgent(baby)
        self.expend_energy(self.energy_reproduce)

class Rabbit(Agent):
    def __init__(self, env, x=None, y=None, Coords=None):
        Agent.__init__(self, id)
        self.energy_reproduce = 8
        self.food_source='env'

    def i_want_a_baby(self):
        baby1=self.__Rabbit__(self.env, x=self.x, y=self.y)
        baby2=self.__Rabbit__(self.env, x=self.x, y=self.y)
        self.env.putAgent(baby)
        self.expend_energy(self.energy_reproduce)

class Wolf(Agent):
    def __init__(self, env, x=None, y=None, Coords=None):
        Agent.__init__(self, id)
        self.food_source='prey'

    def i_am_hungry(self):
        neighbors = self.get_neighbors()
        for n in neighbors:
            if n[2].food_source == 'prey':
                eat_critter(self,n)

class Fighter(Agent):
    def __init__(self, env, x=None, y=None, Coords=None):
        Agent.__init__(self, id)
        self.food_source='all'

    def fight(self):
        neighbors = self.get_neighbors()
        for n in neighbors:
            if n.size<self.size:
                eat_critter(self,n)
            elif n.size>self.size:
                self.die()
                env.removeAgent(self)
            else:
                self.die()
                env.removeAgent(self)
                n.die()
                env.removeAgent(n)
