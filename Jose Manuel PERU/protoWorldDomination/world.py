from gridworld import GridWorld, RectangularGrid, describe, askrandomly
from peruvian import Peruvian
from american import American
from field import Cell, read_celldata
from parameters import params

class World(GridWorld):
    AgentType1=Peruvian
    AgentType2=American
    PatchType = Cell
    n_agents = params['n_agents']
    agent_max_extract = params['agent_max_extract']
    
    def sortkey(self, agent):
        return agent.energy

    def setup(self):
        self.setup_patches()
        self.setup_agents()
        self.header2logfile() # write header to logfile
    
    def header2logfile(self):
        with open(params['logfile'], 'w') as fout:
            fout.write('minimum, mean, maximum')
    
    def log2logfile(self):
        agents = self.get_agents(self.AgentType1)
        energys = list(agent.energy for agent in agents)
        stats = describe(energys)
        with open(params['logfile'], 'a') as fout:
            fout.write(params['logformat'].format(**stats))
    def setup_patches(self):
        celldata = read_celldata(params['cell_data_file'])
        shape = celldata.pop('shape')
        self.set_topology(RectangularGrid(shape=shape))
        patches = self.create_patches(self.PatchType)
        for (x,y), prodrate in celldata.items():
            patches[x][y].max_produce = prodrate

        
        
    def setup_agents(self):
        self.create_agents(Peruvian, number=self.n_agents)
        hunter_locations = self.random_locations(200)
        hunters = self.create_agents(American, locations=hunter_locations)
    
    def schedule(self):
        self.log2logfile()
        for patch in self.patches:
            patch.produce()
        agents = self.get_agents(Peruvian)
        agents.sort(key=self.sortkey, reverse=True)
        for agent in self.agents:
            if agent.shape=='circle':
                agent.move()
                agent.change_energy()
        if max(agent.energy for agent in self.agents if agent.shape=='circle') >= 100:  #from model 7
            self.log2logfile()    #log final agent state
            self.stop(exit=True)
        hunters = self.get_agents(American)
        askrandomly(hunters, 'hunt')
        
        
        
