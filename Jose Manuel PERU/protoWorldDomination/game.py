from gridworld import GridWorldGUI
from world import World
from peruvian import Peruvian
from american import American
from field import Cell



class GUI(GridWorldGUI):
    def gui(self):
        self.add_clickmonitor('American', American, 'energy')
        self.add_clickmonitor('Peruvian', Peruvian, 'energy')
        self.add_clickmonitor('Cell', Cell, 'supply')
        self.add_slider('Population per country', 'n_agents', 10, 500, 10)
        self.add_slider('Agent Max Extract', 'agent_max_extract', 0.0, 2.0, 0.1)
        self.add_button('Set Up', 'setup')
        self.add_button('Run', 'run')
        self.add_button('Stop', 'stop')
        
        def number_living1():
            world = self.subject
            return len(world.get_agents(world.AgentType1)) 
        def number_living2():
            world = self.subject
            return len(world.get_agents(world.AgentType2)) 
        
        self.add_plot('Peruvian Alive', number_living1)
        self.add_plot('American Alive', number_living2)


if __name__ == '__main__':                   #setup and run the simulation    
    myworld = World(topology=None)
    myobserver = GUI(myworld)
    myobserver.mainloop()