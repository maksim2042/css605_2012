import nk
import agent as a
import random as r
from collections import defaultdict
import networkx as net
import numpy as num
import environment as env
import DeathBunny as db


numagents=10
max_time=100
dim=256

#weights=nk.make_weight_matrix(0.1, dim)
e=env.Environment(dim)
agents = [db.DeathBunny(e) for i in range(numagents)]
#aa=a.Agent(e)
#db1=db.DeathBunny(e)
#db2=db.DeathBunny(e)
#db3=db.DeathBunny(e)
##
##def locate(agent):
##        print agent.x,agent.y
##
##def locateDB():
##        print db1.x,db1.y
##        print db2.x,db2.y
##        print db3.x,db3.y
##
##def colocate(agent1,agent2):
##        agent1.x=agent2.x+1
##        agent1.y=agent2.y+1
##        print agent1.x,agent1.y
##        print agent2.x,agent2.y
##
##def vitals(agent):
##        print agent.x,agent.y,"  ",agent.energy
##
##def vitalsDB():
##        print db1.x,db1.y,"  ",db1.energy
##        print db2.x,db2.y,"  ",db2.energy
##        print db3.x,db3.y,"  ",db3.energy
##        
###agents = [db.DeathBunny(e) for i in range(numagents)]
###agentGenomes = [[db.DeathBunny(e).genome,db.DeathBunny(e).id] for i in range(numagents)]

def run():
        trajectories = defaultdict(list)
        for time in range(max_time):
                agents=e.agents.values()
                for agent in r.sample(agents,len(agents)):
                        if agent.alive==True:
                                out=agent.run()
                                trajectories[agent.id].append(out)
        return trajectories
