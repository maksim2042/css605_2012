"""
This class implements a very stupid simple player for the RPS game
"""
import constants as c
import random
import itertools
import operator  

class Player(object):
	
	def __init__(self, id="noID"):
		self.myScore=0
		self.score_history=[]
		self.move_history=[]
		self.id=id
	
	def getID():
		return self.id
	
	def go(self):
		return c.ROCK

	def result(self, res, moves):
		self.score_history.append(res)
		self.move_history.append(moves)
		if res[0]==1: 
			self.myScore+=1
			print "I WON!!! ", self.myScore
		elif res[0]==0:
			print 'DRAW ', self.myScore
		else:
			self.myScore-=1
			print 'I LOST :((( ', self.myScore
		


class RandomPlayer(Player):
	def __init__(self, id="RandomPlayerID" ):
		Player.__init__(self, id)
	
	def go(self):
		choice=int(random.uniform(0,3))
		return(c.CHOICES[choice]) 

#tit for tat player
class TitforTatPlayer(Player):
    '''
     does last one's move
    '''
    def __init__( self, id="TitForTatID" ):
         Player.__init__(self, id)
         return
         
    def go(self):
     
        if len(self.move_history) == 0:
            return c.CHOICES[0]
    
        action = self.move_history[-1]
        return action

 
#sequence player
class SequencePlayer(Player):
    '''
     plays the same sequence over and over
    '''
    def __init__( self, id = "SequencePlayerID" ):
        Player.__init__(self, id) 
        self.location = 0
        self.sequence = []
        #choose random  list
        for i in range(0,5):
            self.sequence.append(c.CHOICES[random.randint(0, 2)])
         
    def go(self):
        '''
        Do the sequence list
        '''
        self.location += 1
        if self.location >= len(self.sequence):
            self.location = 0
            
        action =  self.sequence[self.location]
     
        return action
 
 
#human player
class HumanPlayer(Player):
    '''
     you are the player
    '''
    def __init__( self, id = "HumanPlayerID" ):
        Player.__init__(self, id) 
        self.location = 0
        self.sequence = []
        #choose random  list
        for i in range(0,5):
            self.sequence.append(c.CHOICES[random.randint(0, 2)])
         
    def go(self):
       
        while True:
            var = raw_input("Enter ROCK, PAPER, or SCISSORS: ")
            if var == "ROCK" or var == "PAPER" or var == "SCISSORS":
                action =  var
                break
     
        return action 
    
    
    #machine learning player
class MachineLearningPlayer(Player):
    '''
     plays based on probability distribution, some help from jsbueno
    '''
    def __init__( self ): 
	Player.__init__(self) 
        self.opponentPlays = [(c.ROCK,.01), (c.PAPER,.01), (c.SCISSORS,.01)]
        return
         
    #get the last opponent choice
    def result(self, res, moves):
	
       Player.result(self,res,moves)
       tupleList = []
       for item, probality in self.opponentPlays:
            if moves[1] == item:
                probality += .01
            tupleList.append((item,probality))
            
       self.opponentPlays = tupleList
       
    #sum total probabilities
    def w_choice(self, seq):
        
        total_prob = sum(item[1] for item in seq)
        chosen = random.uniform(0, total_prob)
        cumulative = 0

        '''
        get total probability and determine if next in 
        line has cumulative more than random value
        '''
        for item, probality in seq:
            cumulative += probality
            if cumulative > chosen:
                return item
                
    def go(self):
  
        item = self.w_choice(self.opponentPlays)
        return item   


#MarkovPlayer 
class MarkovPlayer(Player):
    '''
     sequence of items, what's the most likely next move
     eg: [R,P,S,S,R,R,R,S]
     stores every sequence of two, then the next move
     so should estimate possible next move
    '''

    def __init__( self, id = "MarkovPlayerID" ): 
	Player.__init__(self, id) 
        self.opponentPlays = []
        self.tableofItems = {} 
        return
    
    #http://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list
    #has to be an easier way in python
    def most_common(self, L):
      # get an iterable of (item, iterable) pairs
      SL = sorted((x, i) for i, x in enumerate(L))
      
      # print 'SL:', SL
      groups = itertools.groupby(SL, key=operator.itemgetter(0))
      # auxiliary function to get "quality" for an item
      def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
          count += 1
          min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
      # pick the highest-count/earliest item
      return max(groups, key=_auxfun)[0]    
         
     #get the last opponent choice
    def   result(self, res, moves):
      
        Player.result(self, res, moves)
        # clear previous
        self.tableofItems = {}
        play = []
        self.opponentPlays.append(moves[1]) 
        
        #take all these actions and make a table of n-ples
        counter = 0 
        for i in self.opponentPlays:
            play = self.opponentPlays[counter:counter+3]
            if len(play) >= 3:
                
                tpl = (play[0], play[1])
                gv = self.tableofItems.get(tpl)
                 
                if gv == None:
                    gv = [play[2]]
                else:
                    gv.append(play[2]) 
                      
                #table items
                self.tableofItems[tpl] = gv
                    
            counter +=1

 
 
    def go(self): 
        
      lastTwoPlays = self.opponentPlays[-2:]
      if len(lastTwoPlays) >=2:
          tuplev = (lastTwoPlays[0], lastTwoPlays[1])
          #length of item is 3
          if len(self.tableofItems):
              
              #gets the probability of the next move
              getNextMove = self.tableofItems.get(tuplev)
              if getNextMove != None:
                  if len(getNextMove) > 1:
		      #find all xs in ((x,x):(v,v)) and determine most commond v
                      nextMove = self.most_common(getNextMove) 
                  else:
                      nextMove = getNextMove[0]
                   
                  return nextMove

      choice=int(random.uniform(0,3))
      return(c.CHOICES[choice]) 
   
   
 