import constants as c

class State():
	def __init__(self,id):
		self.id=id
		self.newState={}
		self.run()
	
	def transition(self,state,move):
		self.newState[state]=move
		
	def run(self):
		for x in c.CHOICES:
			self.transition(x,self.id)
			

start=State('Start')
stop=State('Stop')
r=State('Rock')
p=State('Paper')
s=State('Scissors')

print 'start',start.newState
print 'stop',stop.newState
print 'r',r.newState
print 'p',p.newState
print 's',s.newState




