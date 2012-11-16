'''
Terrie Franks
CSS 605 Fall 2012
installed networkx and ran through tutorials
'''
import matplotlib.pyplot as plot
import networkx as net


#node_number=20
#initial_nodes = 3
b = net.barabasi_albert_graph(100, 3)

g=net.Graph()
g.add_node ("terrie")
g.add_edge(1,2)


class Graph (dict):
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)
        
        for e in es:
            self.add_edge(e)
            
    def add_vertex(self, v):
        self [v] = {}
        
    def add_edge(self, e):
        v, w=e
        self[v][w] = e
        self[w][v] = e


     
if __name__ == '__main__':
    
    print (g.nodes())
    print (g.edges())
    
    b = net.barabasi_albert_graph (100, 3)

    net.draw(b)
    
    plot.show(b)
          
    
