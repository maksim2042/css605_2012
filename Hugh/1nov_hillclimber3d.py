'''
the hill-climber
'''
import random

class hillclimber(object):
    def __init__(self,initialx,initialy,heat):
        self.last = [-1,-1,0] #x-pos,y-pos,heat
        self.search = [-1,-1,0]
        self.current = [initialx,initialy,heat] #initial location
        self.history = [[initialx,initialy,heat]] #track the path
        self.record = [[initialx,initialy,heat]]
        self.goodmove = 0
    
    def searchPeak(self,x):
        dimension = random.randint(0,1) #0 = x, 1 = y
        direction = random.choice([-1,1])
        #record new search position
        self.search = self.current
        self.search[dimension] = self.search[dimension]+direction
        if self.search[dimension] <= 0:
            self.search[dimension] = 0
        elif self.search[dimension] >= x-1:
            self.search[dimension] = x-1
    
    def evaluate(self,landscape):
        if self.current[2] <= landscape[self.search[0]][self.search[1]]:
            self.goodmove = 1
        else:
            self.goodmove = 0
    
    def move(self):
        if self.goodmove == 1:
            self.current = self.search
            self.history.append(self.current)
            print 'move'
        else:
            self.record.append(self.search)
            print 'stay'
        
        
        