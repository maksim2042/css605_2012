'''
/Users/hjm/GoogleDrive/1_ABM/code/working
makes a rugged 3d landscape for testing
a random number of peaks are selected and then placed
in random locations on the 2-d board. then the gradients
are put in based on those peaks. a sin wave function is used
'''
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import parcel3d
import hillclimber3d
reload(parcel3d)
reload(hillclimber3d)
from parcel3d import *
from hillclimber3d import *

class landscape3d(object):
    def __init__(self):
        self.parcels = [] #the list of parcels x*y
        self.heat = [] #the heat map
        self.landscape = [] #the landscape the hillclimber is moving around
    
    def makeLandscape(self,maxx,maxy,peaks):
        self.initlandscape(maxx,maxy)
        self.initPeaks(maxx,maxy,peaks)
        self.peakNeighbors(maxx,maxy)
        self.createHeatpoints2D(maxx,maxy)
        
        return self.landscape #send the landscape to the optimization object
    
    def initlandscape(self,x,y):
        for i in range(x):
            temp = []
            for j in range(y):
                temp.append(parcel(i,j))
            self.parcels.append(temp)
        
    def initPeaks(self,maxx,maxy,peaks):
        for i in range(peaks): #not checking for duplicates, if it happens, that's OK
            x = random.randint(0,maxx-1)
            y = random.randint(0,maxy-1)
            self.parcels[x][y].peak = 1 #set as peak
            self.parcels[x][y].heat = random.uniform(0.5,1.0) #initialize heat to max

    def peakNeighbors(self,maxx,maxy):
        for i in range (1,20,1):
            #go through each parcel and then color the neighbors
            temp = []
            temp = [self.parcels[j][k] for j in range(maxx) for k in range(maxy) if self.parcels[j][k].peak == i]
            for peak in temp:
                self.initNeighbors(peak.xD,peak.yD,maxx,maxy)

    def initNeighbors(self,refX,refY,maxx,maxy):
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if i ==0 and j ==0:
                    heat = 0
                elif (refX+i) >= 0 and (refY+j) >= 0:
                    if (refX+i)<=(maxx-1) and (refY+j)<=(maxy-1):
                        if self.parcels[refX+i][refY+j].peak == 0:
                            #random degrees lead to numerous local maximums
                            heat = self.parcels[refX][refY].heat * 0.90 #random.uniform(0.5,0.95)
                            self.parcels[refX+i][refY+j].heat = heat
                            self.parcels[refX+i][refY+j].peak = 1 + self.parcels[refX][refY].peak

    def createHeatpoints3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(0, MAX_X, 1)
        Y = np.arange(0, MAX_Y, 1)
        X, Y = np.meshgrid(X, Y)
        
        self.heat = []
        for i in range(MAX_X):
            temp = []
            for j in range(MAX_Y):
                temp.append(self.parcels[j][i].heat)
            self.heat.append(temp)
        surf = ax.plot_surface(X, Y, self.heat)
        plt.show()
    
    def createHeatpoints2D(self,maxx,maxy):
        self.landscape = []
        for i in range(maxx):
            temp = []
            for j in range(maxy):
                temp.append(self.parcels[i][j].heat)
            self.landscape.append(temp)