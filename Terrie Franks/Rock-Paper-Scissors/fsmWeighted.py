'''
Terrie Franks
CSS 605, Fall 2012
Basic Finite State Machine
Experimenting with weighted edges and trees
'''

'''
edges with weights
'''
bid1, bid2, bid3, bid4, bid5 = range (5)

nodes = [
    {bid2:4, bid3:5, bid5:1 },
    {bid1: 2, bid2: 5},
    {bid4: 3, bid1:2},
    {bid5:3, bid1: 1, bid2: 1},
    {bid2: 6, bid3: 5 }
]
# want the edges to sum; not working
'''
s=0
for x in nodes:
    s += x
'''

#building a tree
class Tree:
    def __init__(self, nodes, next=None):
        self.nodes = self.value = nodes
        self.next = next

t = Tree (Tree("r", Tree("p",(Tree("s")))))
t.nodes.next.next.value

class Bunch(dict):
	def __init__(self, *args, **kwds):
		super (Bunch, self).__init__(*args, **kwds)
		self.__dict__= self

#tests are not working but tree is fine in Idle
'''
if __name__ == '__main__':
        checkIt = Tree()
        print(checkIt)
'''

if __name__ == '__main__':              
    b = Bunch (playerName="Terrie", play = "rock")
    b.playerName
 

        
    

