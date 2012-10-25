from random import *
from math import *
import exceptions
from graphics import *

dim=10
inc = 0.001
stop_delta=0.1
temperature=1
anneal_rate=0.001
 

#set scale of graph
scale_x_graph = 20
scale_y_graph = 40

#set the normal distribution graph start points
range_startX = 30
range_startY = 80  

#graph width and height
Width = 500
Height = 500
 
#graphwin
win = GraphWin()

weights=[randint(-100,100) for x in range(dim)]

def fitness(x):
	if len(x)!=dim: raise Exception('wrong dimensions on X')

	sum=0
	for i in range(dim):
		sum+=sin(weights[i]*x[i])
	#print sum
	return sum

def random_x():
	return([random() for z in range(dim)])



def anneal(x):
	""" make a small move in a direction that results in improvement in fitness"""
	global temperature

	index = randint(0,dim-1)
	x1 = list(x)
	x2 = list(x)
	x1[index]+=inc
	x2[index]-=inc
	f=fitness(x)
	f1=fitness(x1)
	f2=fitness(x2)

	temperature-=temperature*anneal_rate

	# says if new functions are not as good, randomly choose one
	if f>f1 and f>f2: 
		if random()<temperature: 
			x1[randint(0,dim-1)]+=2*inc
			return(x1,fitness(x1))
		else:
			return x,f
	elif f1>f2: 
		return x1,f1
	else:
		return x2,f2


def hillclimb(x):
	""" make a small move in a direction that results in improvement in fitness"""

	index = randint(0,dim-1)
	x1 = list(x)
	x2 = list(x)
	x1[index]+=inc
	x2[index]-=inc
	f=fitness(x)
	f1=fitness(x1)
	f2=fitness(x2)

	if f>f1 and f>f2: 
		return x,f
	elif f1>f2: 
		return x1,f1
	else:
		return x2,f2

def run(function):
	global temperature
	temperature = 1
	start = random_x()
	x=start

	surface = []
	while True:
		x,f=function(x)
		surface.append(f)
		print x,f
		draw_items.Draw(f)
		if temperature < 0.1:
			delta=abs(surface[-1]-surface[-4])
			if delta < 1:
				draw_items.Draw(f)
				return surface, x


class DrawItems(object):
	def __init__(self):
		self.counter = .01
		self.draw_counter = 0
		self.point2 = Point(0,0)		

	def Close(self):
		#close the device context
		win.getMouse()
		win.close()	 
		
	def Draw(self, value):
		
		if self.draw_counter % 20 == 0:
			point1 = Point(self.counter*scale_x_graph + range_startX, 
				                                       value*scale_y_graph+range_startY)
			if self.counter == 0:
				self.point2 = point1	    
			p = Line(point1, self.point2)
			self.point2 = point1 
			p.draw(win)
			
		self.counter += .01
		self.draw_counter += 1
		 
	
	def DrawChart(self):
		 
		#set window coordinates and start positions
		win.setCoords(0,0,500,500) 
		
		#draw graph coords
		t = Text(Point(range_startX-7,range_startY), "0.0")
		t.draw(win)   
		t = Text(Point(range_startX-7,scale_y_graph+range_startY), "1.0")
		t.draw(win)     
		
		
		#draw height markers 
		for i in range(0,Height):
			if i % 20 == 0:
			    p = Line(Point(range_startX,range_startY+i), Point(range_startX-1,
				                                 range_startY+i))
			    p.draw(win)
			    
			    t = Text(Point(range_startX-12, range_startY+i), i/(1.0*Height))
			    t.draw(win) 		
		
		
		#draw width markers
		for i in range(0,Width):
			if i % 40 == 0:
			    p = Line(Point(range_startX+i,range_startY), Point(range_startX+i,
				                                 range_startY-5))
			    p.draw(win)
			    
			    t = Text(Point(range_startX+i, range_startY-10), i/(1.0*Width))
			    t.draw(win) 
			    
			    #draw items
		p = Line(Point(range_startX,range_startY), Point(range_startX+Width,
			                                                         range_startY))
		p.draw(win)
		p = Line(Point(range_startX,range_startY), Point(range_startX,
			                                                         range_startY+Height))
		p.draw(win)    		
	   

 
draw_items = DrawItems()
draw_items.DrawChart()			
run(anneal)
draw_items.Close()


