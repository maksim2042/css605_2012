'''
Not sure how to implement this class.  Need to read chapters 28-30 of Learning Python to understand the
overloading, inheritance, and iterators.
'''

import player as p
import constants as c

class Referee():
    
    scorecard = {}
    
    def __init__(self):
        self.scorecard = {}
        
    def resetScore(self):
        self.scorecard = {}
        
    def playRound (self, p1, p2):
        move1 = p1.go()
        move2 = p2.go()
        
        result=list (c.PAYOFFS[move1, move2])
        p1.result(result,[move1, move2])
        self.scorecard[p1] = self.scorecard[p1] + result[0]
        result.reverse()
        
        p2.result(result, [move2, move1])
        self.scorecard[p2] = self.scorecard[p2] + result [0]
        
        p1 = p.RandomPlayer(id="Terrie")
        p2 = p.RandomPlayer()
        
    def playGame(self, p1, p2, numRounds):
        for player in {p1, p2} - set(self.scorecard.keys()):
            self.scorecard[player]=0
        for i in range (numRounds):
            self.playRound(p1, p2)
            
print "Type \"PlayRPS()\""

def PlayRPS():
    
    Ref = Referee()
    
    playerNameList = ["No Thanks"]
    playerList = []
    
    mainMenu = ['Play Rock-Paper-Scissors',
                'View Scorecard',
                'Reset Scorecard',
                'View Players',
                'Create a Player',
                'Delete a Player',
                'Quit']
    
    playerTypeMenu = ['Random Player',
                      'Stupid Player',
                      'Sequence Player',
                      'Tit4Tat Player',
                      'Human Player']
    
    def displayMenu(menu):
        print ''
        for i in range(len(menu)):
            print str(I+1) + ': ' + menu[i]
        print ''
        
        while True:
            option = raw_input('Enter your choice here...')
            try: int(option)
            except: continue
            if int(option) in range (1, len(menu) + 1):
                print ''
                return int(option)
            
    while True:
        print ''
        print "Let's play Rock-Paper-Scissors."
        print ''
        mainOption = displayMenu (mainMenu)
        
        if mainOption == 1:
            if len(playerList) == 0:
                print ''
                print 'You have to create a players before you can play.'
                print ''
                continue
            
            print ''
            print "It's show time."
            print 'Enter player one...'
            player1Choice = displayMenu(playerNameList)
            if player1Choice == len(playerNameList):
                continue
            print ''
            
            while True:
                gameLength = raw_input("Enter the number of rounds to play: ")
                try: int(gameLength)
                except: continue
                gameLength = int(gameLength)
                if gameLength > 0:
                    break
                
            print 'You have chosen', playerNameList[player1Chioce-1], 'and', playerNameList[player2Choice-1]
            Ref.playGame(playerList[player1Choice-1], playerList[player2choice-1], gameLength)

        elif mainOption ==2:
            print Ref.scorecard
            
        elif mainOption == 3:
            Ref.resetScore()
            
        elif mainOption == 4:
            print 'Here are the players currently available to play with...'
            print ''
            for i in range(len(playNameList)-1):
                print playerNameList[i]
            print ''
            
        elif mainOption == 5:
            print ''
            playerNameList.insert (0, raw_input ('Enter a name for your player...'))
            print ''
            print 'Now choose which player type you would like your player to be. '
            playerTypeOption == displayMenu(playerTypeMenu)
            if playerTypeOption == 1:
                playerList.insert(0, p.RandomPlayer())
            elif playerTypeOption == 2:
                playerList.insert (0, p.StupidPlayer())
            elif playerTypeOption == 3:
                playerList.insert (0, p.SequencePlayer())
            elif playerTypeOption == 4:
                playerList.insert ( 0, p.Tit4TatPlayer())
            elif playerTypeOption == 5:
                playerList.insert (0, p.HumanPlayer())
            elif playerTypeOption == 6:
                playerList.insert (0, p.MLPlayer())
            elif playerTypeOption == 7:
                playerList.insert (0, p.MarkovPlayer())
                
        elif mainOption == 6:
            if len(playerList) == 1:
                print "You have no players to delete."
                print ""
                
            else:
                print "Choose which player to delete."
                print ""
                delOption = displayMenu(playerNameList)
                if delOption == len(playerNameList):
                    pass
                else:
                    del playerList[delOption-1]
                    
        elif mainOption == 7:
                print "Thank you for playing Rock-Paper-Scissors"
                return
                
                
            
            
            
                               