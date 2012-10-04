import networkx as net
from collections import deque
import random as rnd
import uuid


class fsm(object):
	def __init__(self):
		self.state_table=net.Graph()
		
		states=['Start R R', 'Start P P', 'Start S S','R R R', 'R P P', 'R S S'
				'P R R', 'P P P', 'P S S','S R R', 'S P P', 'S S S']
		for state in states:
			st=state.split()
			self.state_table.add_edge(st[0],st[1],c=st[2])
		self.current_state='Start'
	
	
	def random_strategy(self, depth=3):
		qq = deque()
		qq.append(('Start',depth))
		moves='R P S'.split()
		
		while True:
			if len(q)==0: break

			x = qq.popleft()
			for z in range(rnd.randint(0,2)):
				source=x[0]
				d=x[1]
				if d >= 0:
					target=str(uuid.uuid4())
					self.state_table.add_edge(source,rnd.choice(moves),c=target)
					qq.append((target,d-1))
		
	def go(self, input):
		print self.current_state, '->>'
		try:
			self.current_state=self.state_table[self.current_state][input]['c']
		except KeyError:
			print "Invalid state transition, don't know what to do with "+input
			self.current_state=stop
		print self.current_state

	
	