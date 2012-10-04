'''
Terrie Franks
CSS 605, Fall 2012
Finite State Machine
added getNextValue and , but not working
'''

import constants as c
#import player as p
import random as randint


class Node():
    
    neighbors = {}
    
    def __init__(self):
        self.id = id
        self.neighbors = {}
    
    def addNeighbor(n, condition):
        self.neighbors[condition] = n
    
    r = Node('R')
    p = Node('P')
    s = Node('S')
    
    r.addNeighbors(r,'R')
    r.addNeighbors(p,'P')
    r.addNeighbors(s,'S')
    p.addNeighbors(r,'R')
    p.addNeighbors(s,'S')
    p.addNeighbors(p, 'P')
    s.addNeighbors(r,'R')
    s.addNeighbors(p,'P')
    s.addNeighbors(s,'S')
    
  
            
    
class fsm(object):
    def __init(self):
        self.current_state=start
        
    def fsm(input):
        print current_state(id), '>>',
        self.current_state=current_state.neighbors[input]
        print self.current_state.id

    state = None

    def getNextValue(self, state, input):
        if state == 'R':
            nextState = 'P'
        elif state == 'P':
            nextState = 'S'
        else:
            nextState = 'R'
            
    transitions = {
        condition, target
    }
    
p= Node()

p.transitions = {
    'r':'P',
    'P':'S',
    'S':'R'
    }
    
state = {
'S':Node,
'P':Node,
'R':Node,
}