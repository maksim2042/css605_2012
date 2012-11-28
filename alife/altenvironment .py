import random as r



class Environment(object):    
    def __init__(self,dim,max_features=5):
        self.dim=dim
        self.feature_types = 'el,food,radiation'.split(',')  
        self.max_features = 5
        self.gradient = 0.2
        self.env=[[{'el':0}for x in range(self.dim)] for x in range(self.dim)]
        self.make_landscape()
        self.agents = set()

    def getVisibleAgents(self,x,y,radius):
        if self.agents == []: return []
        visiblecells = self.getVisibleCells(x,y,radius)
        visibleagents = [ agt for agt in self.agents if (agt.x,agt.y) in visiblecells]
        return visibleagents

    def getVisibleCells(self,x,y,radius):
        if x > self.dim -1 or x < 0 : return []
        if y > self.dim -1 or x < 0 : return []
        if radius > self.dim : return []
        #Have to account for the square the agent is standing on
        # and that the agent may be able to view the whole board
        x_range = set([self.wrap(i) for i in range(x - radius, x + radius +1)])
        y_range = set([self.wrap(i) for i in range(y - radius, y + radius +1)])

        visible_cells = [ (x,y) for x in x_range for y in y_range]

        return visible_cells

    def wrap(self,x):
        if x<0: return(self.dim+x)
        if x>self.dim-1: return(x-self.dim)
        return x

    def make_feature(self,x,y,type):
        self.env[x][y][type]=r.randint(0,self.dim)
        self.do_gradient(x,y,1,self.gradient,type)
    
    def do_gradient(self,x,y,radius,rate,type):
        val=self.env[x][y][type]*(1 - (rate*radius))
        #print radius, val
        if val<=1: return 0
        for xx in range(x-radius,x+radius):
            xx=self.wrap(xx)   
            self.env[xx][self.wrap(y+radius)][type]=val
            self.env[xx][self.wrap(y-radius)][type]=val
            #print xx, self.wrap(y+radius), val
        for yy in range(y-radius,y+radius):
            yy=self.wrap(yy)          
            self.env[self.wrap(x-radius)][yy][type]=val
            self.env[self.wrap(x+radius)][yy][type]=val
            #print self.wrap(x+radius), yy, val
        return self.do_gradient(x,y,radius+1,rate,type)
    
    def make_landscape(self):
        for t in self.feature_types:
            for x in range(self.max_features):
                self.make_feature(r.randint(0,self.dim-1),r.randint(0,self.dim-1),t)
        
