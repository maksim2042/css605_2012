'''
play the game - top level - execute this and it will output the path
'''
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import landscape3d
import parcel3d
import hillclimber3d
reload(landscape3d)
reload(parcel3d)
reload(hillclimber3d)
from landscape3d import *
from parcel3d import *
from hillclimber3d import *


MAX_X = 100
MAX_Y = 100
PEAKS = 20
ITERATIONS = 1000
POINT_SIZE = 50
CMAP = "jet"

class runOptimization(object):
    def __init__(self):
        self.hillclimber = []
    
    def iterateHC(self):
        for i in range(ITERATIONS):
            self.hillclimber[-1].searchPeak(MAX_X)
            self.hillclimber[-1].evaluate()
            self.hillclimber[-1].move()

    def createLandscape(self,maxx,maxy,peaks):
        temp = landscape3d()
        self.landscape = temp.makeLandscape(maxx,maxy,peaks)
    
    def createHillClimber(self):
        xpos = random.randint(0,MAX_X-1) #random x
        ypos = random.randint(0,MAX_Y-1) #random y
        self.hillclimber.append(hillclimber(xpos,ypos,self.landscape)) #create the hillclimber
    
    def plotting(self):
        x = []
        y = []
        #plot the landscape
        for i in range(MAX_X):
            temp = []
            for j in range(MAX_Y):
                temp.append(i)
            x.append(temp)
        
        temp = []
        temp = [i for i in range(MAX_Y)]
        y = [temp for i in range(MAX_Y)]
        
        plt.scatter(x,y, s=POINT_SIZE, c=self.landscape, marker='s',alpha=1,cmap=CMAP)
        
        #plot the path taken
        x=[]
        x=[self.hillclimber[-1].history[i][0] for i in range(len(self.hillclimber[-1].history))]
        y=[]
        y=[self.hillclimber[-1].history[i][1] for i in range(len(self.hillclimber[-1].history))]
        plt.plot(x,y,'r-')

        plt.show()


######
#run the optimization
######

opt = runOptimization()
opt.createLandscape(MAX_X,MAX_Y,PEAKS)
opt.createHillClimber()
opt.iterateHC()
opt.plotting()