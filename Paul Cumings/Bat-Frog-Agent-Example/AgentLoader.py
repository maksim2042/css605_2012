#!/usr/bin/env python
import xml.etree.cElementTree as et
from Agent import *
 
   
#parse the song information
def ParseFloats( stringData ):
    floats = [float(x) for x in stringData.split()]
    return floats
    
#Loads the agent data
class AgentLoader:
    def __init__(self): 
        self.loaded = False
        self.returnAgentList = [] 
     
     #load agent data from xml file, store as agent list      
    def LoadAgentData(self):
        
        inFile = "Agents.xml" 
        tree = et.parse(inFile) #etree.parse() opens and parses the data        
 
        newAgent = None
        #get agent item from xml
        for el in tree.findall('agent'):
            for ch in el.getchildren():
                if ch.tag  == "Type":
                    if ch.text == "Frog":
                    #create a new frog agent
                        newAgent = Frog()  
                    else:
                        newAgent = BlueTailedBat() 
                    self.returnAgentList.append(newAgent)
                     
                    # get spectrum data         
                if ch.tag  == "Spectrum":    
                    floats = ParseFloats(ch.text)
                    for element in floats:
                        #Add a testining state to see where we are
                        newAgent.Spectrum.frequencyList[element] = EvaluationState() 
                        
                        # get name       
                    if ch.tag  == "Name":         
                        newAgent.Name = ch.text
                         
                         #get predator data
                    if ch.tag  == "Predator":         
                        newAgent.Predator = bool(ch.text) 

     
            Loaded = True
        

 