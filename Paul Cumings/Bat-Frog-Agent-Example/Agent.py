
import math 

#create enumeration
class TestState:
    NotTesting, Testing, DoneTesting = range(3)
    
#testing evaluationstate
class EvaluationState:
    def __init__(self):
        self.state = TestState.NotTesting 
        
#frequency class that describes frequences of song over time
#frequencies is a dictionary, and is tested (hence bool)
class Frequencies:
    def __init__(self):
        self.frequencyList = {} 

         
#song spectrum of frequences      
class Song(Frequencies):
    def __init__(self):
        Frequencies.__init__(self)
        self.isPlaying = False
        
#audible spectrum of frequencies
class AudibleSpectrum(Frequencies):
    def __init__(self):
        Frequencies.__init__(self)
        self.isListening = False
        
        
#simple vector class
'''
 x = ax/|a|
 y = ay/|a|
 z = az/|a|
'''
class Vector:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
        
    #normalize vector
    
    def Normalize(self):
        length = sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z)) 
        self.x  = self.x/length
        self.y  = self.y/length
        self.z  = self.z/length
 
 #agent class
class Agent:
#Init constructor
  def __init__(self):
    self.Position = Vector()
    self.Orientation = Vector()
    self.Name = ""
    self.Predator = False
    self.Incrementor = 0 # value from 0-100
    self.TestingUp = 1 #testing values going up
    self.Iterations = 0 #numtesting iterations   
    self.Health = 100.0 #overall health
    self.LastHealth = 100.0
    
  def Update(self, Agent):
      return

  def Thwack(self):
      self.Health -= .001
      return

 
   #not finished yet, get dot product between me/him
  def WhereAmIComparedToHim(self, OtherAgent):
    v = Vector()
    v = self.Position - OtherAgent.Position
    v.Normalize()
 
#derived class agent   
class Frog(Agent):
    def __init__(self): 
        Agent.__init__(self) 
                       
        self.Spectrum = Song()
        self.InTact = 100.0
        self.LastChange=0
         
    #try to come up w/ a different frequency
    def ReviseFrequency(self):
        #check amount of change to self, if it's going down, moving in right direction
        #try some changes now and again 
        
        testing = False
        evalState = None 
        #find testing frequency
        for key in self.Spectrum.frequencyList.iterkeys(): 
            evalState = self.Spectrum.frequencyList[key]  
            #if there are no testing states set, set one
            if evalState == TestState.Testing:
                testing = True
                break
            
            #no frequency being tested
            if testing == False:
                for key in self.Spectrum.frequencyList.iterkeys(): 
                    evalState = EvaluationState()
                    evalState.state = TestState.Testing
                    self.Spectrum.frequencyList[key]=evalState
                    testing = True
                    break
                  
                   
        if testing == True:
            val = key
            #for now just up the pitch 
            
            #cycle up and down
            if self.Incrementor >= 100:
                self.Incrementor = 0 
                self.TestingUp = -self.TestingUp 
                self.Iterations += 1 # count number of iterations

            val += (self.TestingUp * .5)
          
            #remove old key
            del(self.Spectrum.frequencyList[key])
            self.Spectrum.frequencyList[val]=TestState.Testing
            self.Incrementor += 1
             
            return
     
    #do sing
    def SingToMate(self):
        return
    
    #derrived class
    def Update(self, Agent):
      
      #if this number changing faster than last iteration?  
      #state = self.LastChange - self.InTact
      self.SingToMate()
      
      if self.InTact > 0:
          self.ReviseFrequency()
      
#derived class agent   
class BlueTailedBat(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.Spectrum = AudibleSpectrum()
      
    #is the following frequency within range
    def CheckFrequencyIsWithinRange(self, frequency):
 
        #sort the list
        sorteditems = sorted(self.Spectrum.frequencyList.items())
        #do a frequency compare range
        low = sorteditems[0]
        high = sorteditems[1]
        if frequency > low and frequency < high:
            return True
        else: 
            return False

    #derrived class  
    def Update(self, agent):
        
        # get other agents audible spectrum
        spectrum = agent.Spectrum
     
        #check to see if the frequency is in audible range
        #if it is thwack the agent
        for key in spectrum.frequencyList.iterkeys(): 
            isAudible = self.CheckFrequencyIsWithinRange(key)
            if isAudible: 
                agent.Thwack()
        
        return    
       
       
  

