#define three constants for our example:
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

from ComplexNetworkSim import NetworkAgent, Sim
from PyComplexSimCore import NetworkAgent, Sim
import networkx as nx

states[0] = INFECTED


nodes = 30 #we want a graph with 30 agents as a test.

# Network and initial states of agents
G = nx.scale_free_graph(nodes)
states = [SUSCEPTIBLE for n in G.nodes()]  #list of states corresponding to agent states


class SIRSimple(NetworkAgent):
    """ an implementation of an agent following the simple SIR model """

    def __init__(self, state, initialiser):
        NetworkAgent.__init__(self, state, initialiser)
        self.infection_probability = 0.05 # 5% chance
        self.infection_end = 5

    def Run(self):
        while True:
            if self.state == SUSCEPTIBLE:
                self.maybeBecomeInfected()
                yield Sim.hold, self, NetworkAgent.TIMESTEP_DEFAULT #wait a step
            elif self.state == INFECTED:
                yield Sim.hold, self, self.infection_end  #wait end of infection
                self.state = RECOVERED
                yield Sim.passivate, self #remove agent from event queue

    def maybeBecomeInfected(self):
        infected_neighbours = self.getNeighbouringAgentsIter(state=INFECTED)
        for neighbour in infected_neighbours:
            if SIRSimple.r.random() < self.infection_probability:
                self.state = INFECTED
                break
            

class myAgent(NetworkAgent):

    def __init__(self, state, initialiser):
        NetworkAgent.__init__(self, 0, initialiser)
        #other code goes here

    def Run(self):
        #further initialisation code may go here
        while True:
            #main agent logic goes here
            

            from ComplexNetworkSim import NetworkSimulation
            
            # Simulation constants
            MAX_SIMULATION_TIME = 25.0
            TRIALS = 2

def main():
    directory = 'test' #output directory

    # run simulation with parameters
    # - complex network structure
    # - initial state list
    # - agent behaviour class
    # - output directory
    # - maximum simulation time
    # - number of trials
    simulation = NetworkSimulation(G,
                                   states,
                                   SIRSimple,
                                   directory,
                                   MAX_SIMULATION_TIME,
                                   TRIALS)
    simulation.runSimulation()
