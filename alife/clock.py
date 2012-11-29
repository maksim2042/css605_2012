import nk
import climber as c
import random as r
from collections import defaultdict
import networkx as net
import numpy as num

numagents=100
max_time=1000
dim=256

#weights=nk.make_weight_matrix(0.1, dim)

agents = [c.Agent(weights) for i in range(numagents)]
g=net.barabasi_albert_graph(dim, 1, seed=None)
weights = net.to_numpy_matrix(g).tolist()

def run(agents):
	trajectories = defaultdict(list)
	for time in range(max_time):
		for agent in r.sample(agents,len(agents)):
			f=agent.anneal_agent()
			trajectories[agent.id].append(f)
	return trajectories
