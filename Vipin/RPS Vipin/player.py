# Problems: self.name, player count

import constants as c
import random

class Player(object):

    __PlayerCount=0


    def __init__(self, id):
        self.myname=id
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
            print self.myname,'I won', self.myScore
        elif res[0]==0:
            self.myScore+=0
            print self.myname, 'draw', self.myScore
        elif res[0]==-1:
            self.myScore+=-1
            print self.myname,'I lost', self.myScore


class RandomPlayer(Player):

    def __init__(self, id):
        Player.__init__(self,id)
        self.myname='RandomPlayer'

    def go(self):
        choice=int(random.uniform(0,3))
        return(c.CHOICES[choice])


class RockPlayer(Player):
    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='RockPlayer'

    def go(self):
        return c.ROCK



class Tit4Tit(Player):
    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='Tit4Tit'

    def go(self):
        if len(self.move_history) <=0:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            lastplay=self.move_history[len(self.move_history)-1]
            herlastplay=lastplay[1]
            return herlastplay


class Tit4Tat(Player):
    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='Tit4Tat'

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

ManyRandoms(5)

# this player first generates a finite random series; and then repeats it infinitely

class PatternPlayer(Player):

    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='PatternPlayer'

    def go(self):
        length=len(self.move_history)
        adjustedLength=length%5
        return(c.CHOICES[RandomList[adjustedLength]])


class SimplePatternPlayer(Player):
    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='SimplePatternPlayer'
    def go(self):
        length=len(self.move_history)
        if length%3 == 0:
            return c.ROCK
        if length%3 == 1:
            return c.PAPER
        if length%3 == 2:
            return c.SCISSORS

# the way the MachineLearnerPlayer detects pattern is the following:
# (1)she assumes that the opponent will repeat his move, if she wins she continues by the assumption
# (2) if she loses, she assumes that the opponent will repeat his last two moves, if she wins she continues by the assumption
# (3) if she loses, she assumes that the opponent will repeat his last three moves,if she wins she continues by the assumption, and so on....



class MachineLearnerPlayer(Player):

    def __init__(self,id):
        Player.__init__(self,id)
        self.myname='MachineLearnerPlayer'


    def go(self):

        length=len(self.move_history)
        if length<=0:
            choice=int(random.uniform(0,3))
            return(c.CHOICES[choice])
        else:
            lastresult=self.score_history[length-1]
            mylastresult=lastresult[0]
            if mylastresult!=1:
                pattern=[]
                for i in range(0,length):
                    x=self.move_history[i][1]
                    pattern.append(x)
                    if pattern[0] == c.ROCK:
                        return c.PAPER
                    elif pattern[0] == c.PAPER:
                        return c.SCISSORS
                    elif pattern[0] == c.SCISSORS:
                        return c.ROCK

# how do I get pattern to be a list that can be accessed below

            else:
                    if len(pattern)==0:
                        choice=int(random.uniform(0,3))
                        return(c.CHOICES[choice])
                    else:
                        y=length%len(pattern)
                        if pattern[y] == c.ROCK:
                            return c.PAPER
                        elif pattern[y] == c.PAPER:
                            return c.SCISSORS
                        elif pattern[y] == c.SCISSORS:
                            return c.ROCK




# can write a recursive program for a pattern detecting player, just has to call onto itself to find a pattern;
# and have a point at which it gives up and plays random