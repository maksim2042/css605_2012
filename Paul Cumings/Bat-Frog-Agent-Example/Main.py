
# get sys for os current directory
import sys
import os
import copy

#get os directory
cwd = os.getcwd()
 
#import classes
from AgentLoader import *  
from Agent import *

#Loads the agent data
class Main:
    def __init__(self): 
        self.FrogList = {}
        self.BatList = {}
  
    def Start(self):
        #spawn agents
        self.agentLoader = AgentLoader()
        self.agentLoader.LoadAgentData()  
        
        numFrogs = 1
        numBats = 1
        
        #create frog instances
        for ch in self.agentLoader.returnAgentList:
            if isinstance(ch, Frog):
                for i in range(numFrogs):
                    copyItem = copy.copy(ch)
                    self.FrogList[i] = copyItem
                  #make me two bats
            elif isinstance(ch, BlueTailedBat):
                for i in range(numBats):
                    copyItem = copy.copy(ch)
                    self.BatList[i] = copyItem        
                    
    #global update for the main class                 
    def Update(self):
         
        someAliveFrog = False
        #doing generic update function
        for frogKey in self.FrogList.iterkeys():
           frog =  self.FrogList[frogKey]         
           for batKey in self.BatList.iterkeys():
               bat =  self.BatList[batKey]
               #update each
               frog.Update(bat)
               bat.Update(frog)
               
               #if there's still an alive frog keep going
               if frog.Health >=0:
                   someAliveFrog = True
               
        return someAliveFrog
      
#main class update/start                   
MainClass = Main()
MainClass.Start()

while True:
    if MainClass.Update() == False:
      break
