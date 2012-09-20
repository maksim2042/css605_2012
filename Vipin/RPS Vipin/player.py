# Problems: self.name, player count

import constants as c
import random

class Player(object):

    __PlayerCount=0

    def __init__(self):
        #self.name=name
        self.myScore=0
        self.score_history=[]
        self.move_history=[]
        Player.__PlayerCount+=1

    def get_PlayerCount():
        return Player._PlayerCount

    def go(self):
        return c.ROCK

    def result(self, res, moves):
        self.score_history.append(res)
        self.move_history.append(moves)
        if res[0]==1:
            self.myScore+=1
            print 'I won', self.myScore
        elif res[0]==0:
            self.myScore+=0
            print 'draw', self.myScore
        elif res[0]==-1:
            self.myScore-=0
            print 'I lost', self.myScore


class RandomPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])


class RockPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def go(self):
        return c.ROCK



class Tit4Tit(Player):
    def __init__(self):
        Player.__init__(self)

    def go(self):
        if len(self.move_history) <=0:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            lastplay=self.move_history[len(self.move_history)-1]
            herlastplay=lastplay[1]
            return herlastplay


class Tit4Tat(Player):
    def __init__(self):
        Player.__init__(self)

    def go(self):
        length=len(self.move_history)

        if length<=0:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            lastplay=self.move_history[length-1]
            herlastplay= str(lastplay[1])
            if herlastplay == c.ROCK:
                return c.PAPER
            elif herlastplay == c.PAPER:
                return c.SCISSORS
            elif herlastplay == c.SCISSORS:
                return c.ROCK


# generates a list of random numbers

RandomList=[]

def ManyRandoms(n):
    if n>0:
        x=int(random.uniform(0,3))
        RandomList.append(x)
        ManyRandoms(n-1)



# this player first generates a finite random series; and then repeats it infinitely

class PatternPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def go(self):
        ManyRandoms(5)
        length=len(self.move_history)
        adjustedLength=length%5
        movenumber=4-length
        return(c.CHOICES[RandomList[movenumber]])


# the way the MachineLearnerPlayer detects pattern is the following:
# (1)she assumes that the opponent will repeat his move, if she wins she continues by the assumption
# (2) if she loses, she assumes that the opponent will repeat his last two moves, if she wins she continues by the assumption
# (3) if she loses, she assumes that the opponent will repeat his last three moves,if she wins she continues by the assumption, and so on....


pattern=[]

class MachineLearnerPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def go(self):
        length=len(self.move_history)
        if length<=0:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            lastresult=self.score_history[length-1]
            mylastresult=lastresult[0]
            if mylastresult!=1:
                firstplay=self.move_history[0]
                herfirstplay=str(firstplay[1])
                if herfirstplay == c.ROCK:
                    return c.PAPER
                elif herfirstplay == c.PAPER:
                    return c.SCISSORS
                elif herfirstplay == c.SCISSORS:
                    return c.ROCK

                for i in range(0,length):
                    x=self.move_history[i][1]
                    pattern.append(x)

            else:
                if len(pattern)==0:
                    choice=int(random.uniform(0,3))
                    return(c.CHOICES[choice])
                else:
                    y=length%len(pattern)
                    return pattern[y-1]





# can write a recursive program for a pattern detecting player, just has to call onto itself to find a pattern;
# and have a point at which it gives up and plays random