

class Node():
	def __init__(self,id):
		self.id=id
		self.neighbors={}
	
	def addNeighbor(self,n,condition):
		self.neighbors[condition]=n
		
	def run():
		pass


start=Node('Start')
stop=Node('Stop')
r=Node('R')
p=Node('P')
s=Node('S')

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
		self.current_state=start
		
	def go(self, input):
		print self.current_state.id, '->>'
		try: 
			self.current_state=self.current_state.neighbors[input]
		except KeyError:
			print "Invalid state transition, don't know what to do with "+input
			self.current_state=stop
		print self.current_state.id
	
	
	