'''
Created on Oct 10 at 3.45 am, 2012
@author: josemagallanes
'''
import constants as c 
import player as p
import random
        
def rps(players,target):
    p1,p2=players
    r1,r2=(0,0) #HERE WE STORE THE PARTIAL RESULTS OF PLAYER ONE
    while r1<target and r2<target: #WE FINISH THE GAME WHEN ONE GETS THREE POINTS!!
        recentMoves=[p.strategy() for p in players]   #WE GET THE CHOICE OF PLAYER one_instr_line
        movep1,movep2=recentMoves        
        print "%s chose %s AND %s chose %s" %(p1.playerID, movep1,p2.playerID, movep2)
        payoffRecentMoves=list(c.PAYOFFS[movep1,movep2]) #WE STORE THE CHOICES IN A LIST
        updating(payoffRecentMoves,p1,p2,movep1,movep2)
        printPartials(payoffRecentMoves,players)
        r1,r2 = (p.myScore for p in players)
    print ['Winner of the Tournament is %s'%p.playerID for p in players if p.myScore == target] 

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
oponents= random.randint(0,4)
if oponents==0:
    players = (p.RandomPlayer('Tom'), p.RandomPlayer('Mary'))
elif oponents==1:
    players = (p.HumanPlayer('YOU'),p.RandomPlayer('Mary'))
elif oponents==2:
    players = (p.HumanPlayer('YOU'),p.StupidPlayer('Mary'))
elif oponents==3:
    players = (p.tftPlayer('Jim'),p.RandomPlayer('Lidia'))      
else :
    players = (p.RandomPlayer('Jim'),p.StupidPlayer('Lidia'))      

#+++++++++++++++++++++++    


rps(players,3)
#**************