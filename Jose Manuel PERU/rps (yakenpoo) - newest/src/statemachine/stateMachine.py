'''
Created on Oct 4, 2012

@author: josemagallanes
'''
from collections import Counter


class SM:
    startState = None
    def start(self):
        self.state = self.startState
        
    def step(self, inp):
        (s, o) = self.getNextMove(self.state, inp)
        self.state = s
        return o
    
    def play(self, inputs):
        self.start()
        out = [self.step(inp) for inp in inputs]
        data = Counter(out)
        return out,data.most_common()   # Returns all unique items and their counts

class PlayerTFT(SM):
    startState = 'r'
    def getNextMove(self, state, inp):
        ## r: (r:p,p:s,s:r), p: (p:s, r:p, s:r)
        if state == 'r' and inp == 'r':
            return ('p', 0)
        elif state == 'r' and inp == 'p':
            return ('s', -1)
        elif state == 'r' and inp == 's':
            return ('r', 1)
        elif state == 'p' and inp == 'p':
            return ('s', 0)
        elif state == 'p' and inp == 'r':
            return ('p', 1)
        elif state == 'p' and inp == 's':
            return ('r', -1)
        elif state == 's' and inp == 's':
            return ('r', 0)
        elif state == 's' and inp == 'r':
            return ('p', -1)
        elif state == 's' and inp == 'p':
            return ('s', 1)
        
player1 = PlayerTFT()
player2='s,r,r,r,r,s'
print player2, player2.split(',')
print player1.play(player2.split(','))