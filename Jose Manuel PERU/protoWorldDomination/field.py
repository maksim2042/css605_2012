from gridworld import Patch
from parameters import params
   
def read_celldata(filename):
    location2value = dict()
    maxx, maxy = 0, 0
    fh = open(filename, 'r')
    for _ in range(3): #discard 3 lines
        trash = next(fh)
    for line in fh:
        x, y, prodrate = line.split()
        x, y, prodrate = int(x), int(y), float(prodrate)
        location2value[(x,y)] = prodrate
        maxx, maxy = max(x,maxx), max(y,maxy)
    location2value['shape'] = (maxx+1, maxy+1)
    return location2value

class Cell(Patch):
    max_produce = params['cell_max_produce']
    supply = params['cell_initial_supply']
    def initialize(self):
        self.change_color()
    def produce(self):
        self.supply += self.max_produce #no longer random
        self.change_color()
    def provide(self, amount):
        amount = min(self.supply, amount)
        self.supply -= amount
        return amount
    def change_color(self):
        r = b = 0
        g = min(2*self.supply, 1.0)
        self.display(fillcolor=(r, g, b))