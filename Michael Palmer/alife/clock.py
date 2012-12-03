import nk
import agent as a
import random as r
from collections import defaultdict
import networkx as net
import numpy as num
import environment as env


numagents=100
max_time=1000
dim=256

#weights=nk.make_weight_matrix(0.1, dim)
e=env.Environment(dim)
agents = [a.Agent(e) for i in range(numagents)]

def run(agents):
	trajectories = defaultdict(list)
	for time in range(max_time):
		for agent in r.sample(agents,len(agents)):
		    if agent.alive==True:
		        out=agent.run()
		        trajectories[agent.id].append(out)
		    else:
		        agents.remove(agent)
	return trajectories
