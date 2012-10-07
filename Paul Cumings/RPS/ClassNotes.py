

class Node():
    def __init__(self, id):
        self.id = id
        self.neighbors = {}
       
    def addNeighbor(self, n, condition):
        self.neighbors[condition]=n
        
        
start = Node('Start')

r = Node('R')
p = Node('P')
s = Node('S')

start.addNeighbor(r,'R')
start.addNeighbor(p,'P')
start.addNeighbor(s,'S')

r.addNeighbor(r,'R')
r.addNeighbor(p,'P')
r.addNeighbor(s,'S')

p.addNeighbor(r,'R')
p.addNeighbor(p,'P')
p.addNeighbor(s,'S')

s.addNeighbor(r,'R')
s.addNeighbor(p,'P')
s.addNeighbor(s,'S')

 

class fsm(object):
    def __init__(self):
        self.current_state = start
    
    def go( self ):
        while self.current_state.id != 'Stop':
            print self.current_state.id, '->>' 
            input = raw_input('Move!')
            
            try:
                self.current_state = self.current_state[input]  
            except KeyError:
                print "invalid state transition"
                self.current_state = stop
                
            print self.current_state.id
        

monster = fsm()    
monster.go()