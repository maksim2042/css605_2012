class FSM():
	def __init__(self):
		self.handlers={}
		self.StartNode=None
		self.EndNode=None

	def AddNode (self, name, handler, end_state=0):
		self.handlers[name] = handler
		if end_state:
			self.EndNode.append(name)
		
	def SetStart (self, name):
		self.StartNode=name

	def run (self, content):
		if self.StartNode in self.handlers:
			handler = self.handlers[self.StartNode]
		else:
			raise "Error", "Please try again"	

		OldNode = self.StartNode
		while 1:
			(NewNode, content) = handler(content, OldNode)
			if NewNode in self.handlers:
				handler = self.handlers[NewNode]
			OldNode = NewNode