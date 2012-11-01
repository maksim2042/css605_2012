'''
/Users/hjm/GoogleDrive/3_EconABM/ZZ_TermProject/ModelCode/working
makes a rugged 3d landscape for testing
a random number of peaks are selected and then placed
in random locations on the 2-d board. then the gradients
are put in based on those peaks. a sin wave function is used
'''
import random
import matplotlib.pyplot as plt
import numpy as np

class parcel(object): #landscape is composed of parcels
    def __init__(self,x,y):
        self.xD = x #X-dimension
        self.yD = y #Y-dimension
        self.heat = 0 #heat signature
        self.peak = 0 #is it a peak?
        