
'''
evolvotron3000.py

Brendon Fuhs
10-5-12

This is an interface and referee for running
Rock, Paper, Scissors games and evolving players.


'''


import random as r
import constants as c
import player as p
import playermachine as pm
import copy


# Select players to evolve against


def playGame(p1,p2):
    pass


def evolveAgainst(opponent):

    if type(opponent)=="type":
        opponent = opponent() # Instantiates an opponent if it's a player type
 
    MACHINENUM = 100 # Number of competing machines at any given time.
    MACHINESIZE = 100 ### Not sure if this is initial or if it will change
    ROUNDSPERGAME = 100
    GAMENUM = 100 ### Later on, change this to legit stopping criteria
    
    #### Not sure if "nodeNum=" should be in here
    machineList = [pm.FSM(nodeNum=MACHINESIZE)]*MACHINENUM

    for game in range(GAMENUM):
        # This is how to play a game with the machineList ##### Do I want Deep or Shallow copy?
        map( playGame, machineList, [copy.deepcopy(opponent)]*MACHINENUM )
    
        # Now all the machines have scores which I can use as fitness
        machineList = recombineMutateEtc(machineList)

    # Return fittest machine (Look at their scorecards ###########

def recombineMutateEtc(machineList):
    pass ########### Look up roulettes whatever









