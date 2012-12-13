from random import *
from agent import Agent
from math import *
import exceptions
import uuid
from environment import Environment
from clock       import run
from genomeagent import *

class chris_Wolf(GenomeAgent):
      def __init__(self,env,genome=WOLF,species = 'wolf'):
        super(chris_Wolf,self).__init__(env,genome,species)   
      def chase_prey(self,movement):
         #
         # If a prey gets ahead of the wolf through activation order a new prey may actually be closer
         #
         while (self.visible_prey() and movement > 0):
            closest = self.find_closest_prey(self.getFOV())
            competitor = self.find_closest_predator(self.getFOV())
            if closest != [] and closest[0][0] > 0.5:
              if competitor != [] and (competitor[0][1] + competitor[0][2]) > 3:
                x_move,y_move = self.get_directiontoward(closest[0][1],closest[0][2])
                self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                movement -= 1
              if competitor != [] and self.identification(competitor[0][3]) == True and (competitor[0][1] + competitor[0][2]) <= 3:
                x_move,y_move = self.get_directiontoward(competitor[0][1],competitor[0][2])
                self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                self.attackcompetitor(competitor[0][3])
                movement -= 1
            else :
              self.attackprey(closest[0][3])
              movement -= 1
         return movement
      def attackprey(self,agent):
          ratio = ((agent.energy / 10.0) + agent.size) / (((agent.energy / 10.0) + agent.size) + ((self.energy / 10) + self.size))
          attack = uniform(0,1)
          if attack > max(ratio,.80):
              self.energy += agent.size
              agent.die()
          else:
              print 'attack failed!!'
      def attackcompetitor(self,agent):
          ratio = ((agent.energy / 100.0) + agent.size) / (((agent.energy / 100.0) + agent.size) + ((self.energy / 100.0) + self.size))
          attack = uniform(0,1)
          if attack > max(ratio,.80):
              self.energy += agent.size
              agent.die()
              print 'winner takes all!'

          else:
              print 'defeated'
      def identification(self,agent):
          if self.species != agent.species and agent.species != 'rabbit':
            return True


      def run(self):
          movement = self.movement_rate

          self.age += 0.1
          
          if self.visible_prey():movement = self.chase_prey(movement)

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)

          if self.visible_same_species() and movement >0 :
             movement = self.move_to_mate(movement)
             self.mate()

          if self.shoulddie() :
             self.die()
             return(self.x,self.y)

          if self.visible_prey() == False and self.visible_same_species() == False and movement > 0:
             movement = self.wander(movement,self.visible_prey)
             
          if self.shoulddie() :
             self.die()
             return(self.x,self.y)

          if self.energy > self.growth_energy_threshold: 
             self.size += self.size*self.growth_rate
          
          print 'wolf %s %s %s \n'%(self.id, self.x,self.y)
          return (self.x,self.y)
