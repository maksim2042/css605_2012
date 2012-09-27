'''
This file contains the various player methods.  Read chapters 14-27 of Learning Python to try iterators, how to test,
and printing strings.


'''
import constants as c
import random
import shelve
from random import randint
from time import sleep

class Player(object):
    
    def __init__(self, id="noID"):
        self.myScore = 0
        self.score_history=[]
        self.move_history=[]
        self.id = id
    
    def getID():
        return self.id
    
    def go(self):
      return c.ROCK
    
    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        
        if res[0]==1:
            self.myScore+=1
            print 'iwon'
        elif res[0] == 0:
            print 'draw'
        else:
            self.myScore-=1
            print 'I lost'
        
class RandomPlayer(Player):
        def __init__(self):
            Player.__init__(self)
            
        def go(self):
            choice=int(random.uniform(0,3))
            return (c.CHOICES[choice])
        
class StupidPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        
        self.same = c.CHOICES[int(random.uniform(0,3))]
    def go(self):
        return(self.same)
    
#    def __str__(self):
#       return '[StupidPlayer: %s]' % (self.samePlay)
    
        
class SequencePlayer (Player):
    def __init__(self):
        Player.__init__(self)
        self.SEQUENCELENGTH = 42
        self.sameSequence = [" "]*self.SEQUENCELENGTH
        
        for i in range(self.SEQUENCELENGTH):
            self.sameSequence[i] = c.CHOICES[int(random.uniform(0,3))]
        self.moveNum = 0
       
    def go(self):
        return(self.sameSequence[self.moveNum % self.SEQUENCELENGTH])
    
        
    
#    def __str__(self):
#        return '[SequencePlayer: %s]'  %(self.playOne, self.playTwo, self.playThree)
        
class Tit4TatPlayer (Player):
    def __init__ (self):
        Player.__init__(self)
        self.moveNum = -1
       
    def go(self):
        self.moveNum +=1
        if self.moveNum == 0:
            return(c.CHOICES[int(random.uniform(0,3))])
        else:
            return(self.move_history[self.movNum-1][1])
        
class HumanPlayer (Player):
    def __init__(self):
        Player.__init__(self)
        self.firstTime = True
        self.playerName = "Paul"
    
    def go(self):
        if self.firstTime == True:
            self.playerName = raw_input("What is your name?")
            print "Time to play ", self.playerName
            self.firstTime = False
            
        print "Dear ", self.playerName," , "
        while True:
            input = raw_input("Type ROCK, PAPER, or SCISSORS and hit enter...")
            if input in c.CHOICES:
                return input
            
    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append (moves)
        
        if res[0]==1:
            self.myScore+=1
            print "You won. Your total score is ", self.myScore
        elif res[0]== 0:
            print "You lost.  Your total score is ", self.myScore
        else:
            self.myScore -=1
            print "It's a draw.  Your total score is ", self.myScore
            
#This is an extremely simple machine learning that adds the number of time
#the other player chooses rock, paper or scissors, and plays the one w/ highest #.

class MLPlayer (Player):
    def __init__(self):
        Player.__init__(self)
        
    def checkTotalMoves (self, totalMoves):
        self.totalMoves = totalMoves
        totalMoves = (Player.move_history (moves))
                    
 #tried using the built-in dbase, but decided not needed
 #       db=shelve.open ('movedb')
 #       for object in (p2.move_history):
 #           db[object.move] = object
 #       db.close ()
    
    def checkTotal (self, totalRock, totalPaper, totalScissors):        
        self.totalRock = totalRock
        self.totalPaper = totalPaper
        self.totalScissors = totalScissors
        
        totalRock = t.count ('rock')
        totalPaper = t.count ('paper')
        totalScissors = t.count ('scissors')
        
        for i in range (self.move_history):
            self.move_history[i] = c.CHOICES[int(random.uniform(0,3))]
            self.move_history = 0
            
            if 'totalRock' > 'totalPaper':
                if 'totalPaper'>'totalScissors':
                    return 'rock'
                
            if totalPaper > totalRock:
                if totalRock > totalScissors:
                    return 'paper'
                
            if totalScissors > totalPaper:
                if totalPaper > totalRock:
                    return 'scissors'
                
            if totalRock == totalPaper:
                if totalScissors > totalRock:
                    return 'scissors'
                
            if totalScissors == totalPaper:
                if totalRock > totalScissors:
                    return 'rock'
                
            if totalRock == totalScissors:
                if totalPaper > totalRock:
                    return 'paper'
                
    #this will use a random number generator to pick the moves, in case the other player
    #tries to analyze my move pattern 
   
    class spinMove (Player):
         def __init__(self):
            Player.__init__(self)
            
            choice = randint(1,3)
            
    #this is a cheater class that uses sleep, which gives a 2 second delay
    #for the computer to choose a winning response
    
    class delay(Player):
        def __init__(self):
            Player.__init__ (self)
            
        if p2 == 'rock':
            sleep (2)
            return 'paper'
        
        elif p2 == 'paper':
            sleep (2)
            return 'scissors'
        
        else:
            sleep (2)
            return 'rock'
            
            
            
       
        

        
        

'''
    if __name__ == '__main__':
        same = StupidPlayer()
        print(same)
 
    if __name__ == '__main__':  
        seq = SequencePlayer()
        print (seq)
'''  
    
    
    
        
        
        
    
        
        