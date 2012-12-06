from gridworld import TorusGrid, GridWorldGUI, GridWorld, ask, askrandomly
from bunny import Bunny
from parameters import params
from environment import Cell
from wolfie import Wolf


class World(GridWorld):
    AgentType = Bunny
    PatchType = Cell
    n_agents = params['n_agents']
    agent_max_extract = params['agent_max_extract']
    
    def schedule(self):
        ask(self.patches, 'produce')
        rabbits = self.get_agents(self.AgentType)
        askrandomly(rabbits, 'move')     #creates new entrants
        askrandomly(rabbits, 'change_energy')     #creates new entrants
        wolves = self.get_agents(Wolf)
        askrandomly(wolves, 'hunt')
        
    def setup(self):
        self.setup_patches()
        self.setup_agents()
        hunter_locations = self.random_locations(200)
        wolves = self.create_agents(Wolf, locations=hunter_locations)
        
    def setup_patches(self):
        self.create_patches(self.PatchType)
        
    def setup_agents(self):
        self.create_agents(self.AgentType, number=self.n_agents)
        
        

class GUIWORLD(GridWorldGUI):
    def gui(self):
        self.add_slider('Initial Rabbit Pop.', 'n_agents', 10, 500, 10)
        self.add_slider('Rabbit MaxExtract', 'agent_max_extract', 0.0, 2.0, 0.1)
        self.add_button('Set Up', 'setup')
        self.add_button('Run/continue', 'run')
        self.add_button('Stop/pause', 'stop')
        def get_agent_energy():
            agents = self.subject.get_agents(self.subject.AgentType)
            return list(agent.energy for agent in agents)
        self.add_histogram('Agent''s Energy', get_agent_energy, bins=range(11))
          
                       
worldGrid = TorusGrid(shape=params['world_shape'])
EnvWorld = World(topology=worldGrid)
observer = GUIWORLD(EnvWorld)
observer.mainloop()       # so windows does not close after maxiter is reached
 
