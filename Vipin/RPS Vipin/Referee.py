import constants as c
import player as p

#This function tells the referee what to do. The way this works is that the refereee asks the players to play a move, the player respond, then the referee tells them who has won

# the go function is defined in each player. If the referee tells the player to go, the players return a move
def playRound(p1,p2):
    move1=p1.go()
    move2=p2.go()
    result=list(c.PAYOFFS[move1,move2])

    #this allows both players to recieve both moves and the numbers assosciated with the moves

    p1.result(result,[move1,move2])
    result.reverse()
    p2.result(result,[move2,move1])

p1 = p.SimplePatternPlayer(id)
p2 = p.MachineLearnerPlayer(id)


def playGame():
    for i in range(100):
        playRound(p1,p2)

playGame()


