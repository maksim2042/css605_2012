'''
Created on Oct 18, 2012
@author: josemagallanes
'''
import constants as c 
import player as p
import random
        
def rps(players,pointsToWin):
    p1,p2=players
    r1,r2=(0,0) #HERE WE STORE THE PARTIAL RESULTS OF PLAYER ONE
    while r1<pointsToWin and r2<pointsToWin: #WE FINISH THE GAME WHEN ONE GETS THREE POINTS!!
        recentMoves=[p.strategy() for p in players]   #WE GET THE CHOICE OF PLAYER one_instr_line
        movep1,movep2=recentMoves        
        print "%s chose %s AND %s chose %s" %(p1.playerID, movep1,p2.playerID, movep2)
        payoffRecentMoves=list(c.PAYOFFS[movep1,movep2]) #WE STORE THE CHOICES IN A LIST
        updating(payoffRecentMoves,p1,p2,movep1,movep2)
        printPartials(payoffRecentMoves,players)
        r1,r2 = (p.myScore for p in players)
    print ['Winner of the Tournament is %s'%p.playerID for p in players if p.myScore == pointsToWin] 

def updating(ps,p1,p2,m1,m2):
    p1.updatePlayersHistory(ps[0],[m1,m2]) # WE PASS THE RESULT, PLAYER ONE WILL KNOW RESULT - IN choice[0] IS THE SCORE
    p2.updatePlayersHistory(ps[1],[m2,m1]) # WE PASS THE RESULT, PLAYER ONE WILL KNOW RESULT
    
def printPartials(pmoves,(p1,p2)):
    if pmoves==[1,-1]: 
        print "%s won (accumulating %d points) " %(p1.playerID, p1.myScore)
        print "%s lost (accumulating %d points) " %(p2.playerID, p2.myScore)
    elif pmoves==[0,0]:
        print "%s drew (accumulating %d points)" %(p1.playerID, p1.myScore)
        print "%s drew (accumulating %d points)" %(p2.playerID, p2.myScore)
    else:
        print "%s lost (accumulating %d points) " %(p1.playerID, p1.myScore)
        print "%s won (accumulating %d points) " %(p2.playerID, p2.myScore)

#+++++++++++++++++++++++
oponents= 5#random.randint(0,5)
if oponents==0:
    players = (p.RandomPlayer('Tom'), p.RandomPlayer('Mary'))
elif oponents==1:
    players = (p.HumanPlayer('YOU'),p.RandomPlayer('Mary'))
elif oponents==2:
    players = (p.HumanPlayer('YOU'),p.StupidPlayer('Mary'))
elif oponents==3:
    players = (p.tftPlayer('Jim'),p.RandomPlayer('Lidia'))
elif oponents == 4:
    players = (p.SequencePlayer('Pepe'),p.tftPlayer('Mary'))      
elif oponents == 5:
    players = (p.SequencePlayer('Pepe'),p.GAPlayer('Mary'))
else :
    players = (p.RandomPlayer('Jim'),p.StupidPlayer('Lidia'))      

#+++++++++++++++++++++++    
rps(players,pointsToWin=10)
#**************