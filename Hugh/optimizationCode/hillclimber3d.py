'''
the hill-climber
'''
import random

class hillclimber(object):
    def __init__(self,initialx,initialy,landscape):
        self.landscape = landscape
        self.history = [[initialx,initialy,landscape[initialx][initialy]]] #initial location
        self.search = []
        self.goodmove = 0
    
    def searchPeak(self,max_x):
        #record new search position
        temp = [0,0]
        self.search = []
        temp[random.randint(0,1)] = random.choice([-1,1])
        #calculate new parcel
        for i in range(2):
            if temp[i]+self.history[-1][i] < 0:
                self.search.append(0)
            elif temp[i]+self.history[-1][i]>(max_x-1):
                self.search.append(max_x-1)
            else:
                self.search.append(temp[i]+self.history[-1][i])
        
        self.search.append(self.landscape[self.search[0]][self.search[1]])
    
    def evaluate(self):
        if self.search[2] >= self.history[-1][2]:
            self.goodmove = 1
        else:
            self.goodmove = 0
    
    def move(self):
        if self.goodmove == 1:
            self.history.append(self.search)