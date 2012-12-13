# Standard library imports:
from collections import defaultdict
from datetime import timedelta
import random
# Tornado imports:
import tornado.websocket
import tornado.ioloop
import tornado.web
# Model imports:
#from animals import make_wolf, 
from genomelife import Rabbit, Wolf
from environment import Environment



PATH = "/Users/dmasad/Programming/CSS605/css605_2012/David Masad/alife_visualization/static/"


class ALife_Model(object):

    def __init__(self, environment, agent_list, max_time = 1000):
        self.environment = environment
        self.agent_list = agent_list
        for agent in self.agent_list:
            self.environment.putAgent(agent)

        self.max_time = max_time
        self.species_list = list(set([agent.species for agent in self.agent_list]))
        self.time = 0

        self.latest_state = None


    def run(self):
        trajectories = defaultdict(list)
        for time in range(self.max_time):
            for agent in random.sample(self.agent_list, len(self.agent_list)):
                if agent.alive:
                    out = agent.run()
                    trajectories[agent.id].append(out)
                else:
                    self.agent_list.remove(agent)
        return trajectories

    def tick(self):
        agent_locations = {}
        for agent in random.sample(self.agent_list, len(self.agent_list)):
            if agent.alive:
                new_coords = agent.run()
                agent_locations[agent.id] = new_coords

        self.latest_state = self.agent_data()
        self.time += 1


    def env_only(self):
        '''
        Returns the current environment only, without agents
        for serializing and sending to the visualization.
        '''
        clean_env = []
        for row in self.environment.env:
            new_row = []
            for cell in row:
                new_cell = {}
                for key, value in cell.items():
                    if key != 'agents': new_cell[key] = value
                new_row.append(new_cell)
            clean_env.append(new_row)
        return clean_env
    
    def agent_data(self):
        '''
        Get the agent data in dictionary format.
        '''

        all_agents = []
        for agent in self.agent_list:
            agent_dict = {}
            agent_dict['id'] = agent.id
            agent_dict['species'] = agent.species
            agent_dict['x'] = agent.x
            agent_dict['y'] = agent.y
            all_agents.append(agent_dict)
        return all_agents


class ModelSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print "Socket open!"
        self.send_environment()
        self.send_species()
        self.send_agents()

        self.ticker = tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=1), self.update_model)

    def on_message(self,message):
        print message

    def on_close(self):
        tornado.ioloop.IOLoop.instance().remove_timeout(self.ticker)
        print "Socket closed!"


    def update_model(self):
        self.send_environment()
        self.send_agents()
        self.ticker = tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=1), self.update_model)


    def send_environment(self):
        '''
        Send the environment to the client
        '''
        env_data = MODEL.env_only()
        message = {"header": "environment", "contents": env_data}
        self.write_message(message)

    def send_species(self):
        species_list = MODEL.species_list
        message = {"header": "species", "contents": species_list}
        self.write_message(message)

    def send_agents(self):
        agent_list = MODEL.latest_state
        message = {"header": "agent_update", "contents": agent_list}
        self.write_message(message)


def launch_model():
   ev = Environment(12)
   #wf = make_wolf(ev)
   #rb = make_rabbit(ev)
   '''
   wolves = [Wolf(ev) for _ in range(2)]
   rabbits = [Rabbit(ev) for _ in range(4)]
   agents = wolves + rabbits
   for agent in agents:
       agent.x = random.randint(0,11)
       agent.y = random.randint(0,11)
   model = ALife_Model(ev, agents)
   return model
   '''
   wf = Wolf(ev)
   rb = Rabbit(ev)
   rb.debug = True
   rb.x = 1
   rb.y = 1
   wf.x = 2
   wf.y = 2
   #model = ALife_Model(ev, [wf, rb])
   model = ALife_Model(ev,[rb])
   return model

app = tornado.web.Application([(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": PATH}),
    ("/websocket", ModelSocket) ])
if __name__ == "__main__":
    MODEL = launch_model()
    app.listen(8888)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(MODEL.tick, 500).start()
    instance.start()
