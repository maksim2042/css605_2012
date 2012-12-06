import random as r



class Environment():
    
    def __init__(self,dim,max_features=5):
        self.dim=dim
        self.feature_types = 'el,food,radiation'.split(',')  
        self.max_features = 5
        self.gradient = 0.2
        #self.obstacles=0.1
        self.env=[[{'el':0}for x in range(self.dim)] for x in range(self.dim)]
        self.make_landscape()

    def wrap(self,x):
        if x<0: return(self.dim+x)
        if x>self.dim-1: return(x-self.dim)
        return x
        

    def getFOV(self,x,y,radius):
        fov=[]
        x_range = set([self.wrap(i) for i in range(x - radius, x + radius +1)])
        y_range = set([self.wrap(i) for i in range(y - radius, y + radius +1)])


        for x in x_range:
            row = []
            for y in y_range:
                row.append(self.env[x][y])
            fov.append(row)

        return fov

    
    def putAgent(self,agent):
        if 'agents' not in self.env[agent.x][agent.y]:
            self.env[agent.x][agent.y]['agents']={}
        self.env[agent.x][agent.y]['agents'][agent.id]=agent
        
    def removeAgent(self,agent):
        try:
            self.env[agent.x][agent.y]['agents'].pop(agent.id)
        except KeyError:
            print "this really shouldn't happen unless Agent code is screwed up"
        
    def moveAgent(self,agent,to_x,to_y):
        from_el=self.env[agent.x][agent.y]['el']
        from_x=agent.x
        from_y=agent.y
        self.removeAgent(agent)
        agent.x=to_x
        agent.y=to_y
        to_el=self.env[agent.x][agent.y]['el']
        self.putAgent(agent)
        return(abs(from_x-to_x)+abs(from_y-to_y)+abs(from_el-to_el))
        

    def make_obstacle(self,x,y):
        self.env[x][y]['X']=1

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
        for x in range(self.dim):
            for y in range(self.dim):
                if r.random()<0.01: self.make_obstacle(x,y)
        
        for t in self.feature_types:
            for x in range(self.max_features):
                self.make_feature(r.randint(0,self.dim-1),r.randint(0,self.dim-1),t)
        
