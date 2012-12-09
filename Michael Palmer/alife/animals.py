from environment import Environment
from genomeagent import *
from math        import sqrt
from clock       import run


RABBIT = [ 10,
            9,
            9,
            5,
            1,
            1,
            1,
            1,
            1,
            2,
            10]

WOLF   = [ 10,
           36,
            9,
           20,
           20,
            1,
            9,
           20,
            2,
            1,
           20]




def test_rabbit():
   ev = Environment(10)
   rb = Rabbit(ev)
   ev.putAgent(rb)
   rb.run()

def test_wolf():
   ev = Environment(10)
   wf = Wolf(ev)
   ev.putAgent(wf)
   wf.run()

def test_moveforfood():
   ev = Environment(10)
   rb = Rabbit(ev)
   rb.x = 1
   rb.y = 1   
   ev.putAgent(rb)
   return run(ev)

   
def test_chase():
   ev = Environment(10)
   wf = Wolf(ev)
   rb = Rabbit(ev)
   rb.x = 1
   rb.y = 1
   wf.x = 3
   wf.y = 3
   ev.putAgent(rb)
   ev.putAgent(wf)
   return run(ev)

def test_movetosame():
   ev = Environment(10)
   rb = Rabbit(ev)
   rb1= Rabbit(ev)
   rb.x = 1
   rb.y = 1
   rb1.x = 3
   rb1.y = 3
   ev.putAgent(rb)
   ev.putAgent(rb1)
   return run(ev)

class Rabbit(GenomeAgent):
      def __init__(self,env,genome=RABBIT,species = 'rabbit'):
        super(Rabbit,self).__init__(env,genome,species)
      def no_food(self):
        if self.env.env[self.x][self.y].has_key('food') and self.env.env[self.x][self.y]['food'] > 0: return False
        return True
      def eat_grass(self):
        if self.env.env[self.x][self.y].has_key('food') and self.env.env[self.x][self.y]['food'] > 0:
           food_consumed = self.consumption_rate
           if self.env.env[self.x][self.y]['food'] < self.consumption_rate:
              food_consumed = self.env.env[self.x][self.y]['food']
           self.energy += food_consumed 
           self.env.env[self.x][self.y]['food']-=food_consumed
            
        return self.env.env[self.x][self.y]['food']   
      def avoid_predators(self,movement):
         # Allows the rabbit to react to a new, closer predator
         # Does not stop the rabbit from running back towards a previous predator
         while (self.visible_predators() and movement > 0):
              closest = self.find_closest_predator(self.getFOV())
              if closest != []:
                 x_move,y_move = self.get_directionaway(closest[0][1],closest[0][2])
                 self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                 movement -= 1
         return movement
      def move_to_mate(self,movement):
         while (movement > 0 and self.visible_same_species > 0):
            closest = self.find_closest_same_species(self.getFOV())
            if closest != [] and closest[0] > 0:
               x_move, y_move = self.get_directiontoward(closest[0][1],closest[0][2])
               self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
               movement -= 1
         return movement              
      
      def move_towards_food(self,movement):
         while (movement > 0 and self.no_food()==True):
            closest = self.find_closest_food(self.getFOV())
            if closest != []:
               x_move, y_move = self.get_directiontoward(closest[0][1],closest[0][2])
               self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
               movement -= 1
         return movement

      def mate(self):
        print 'in mate'
        miniFOV=self.env.getFOV(self.x,self.y,1)
        neighbors = self.get_neighbors(fov=miniFOV)
        for n in neighbors:
            if n[2].species == self.species and n[2].id !=self.id:
                print 'attempting to mate'
                self.mate_with_agent(n[2])
                return
      def mate_with_agent(self,agent):
        baby=self.__class__(self.env,self.genome,[self,agent])
        self.env.putAgent(baby)
        self.expend_energy(self.energy_mating_delta+self.energy_childbirth_delta)
      
      def run(self):
          movement = self.movement_rate

          self.age += 0.1

          self.eat_grass()
          
          if self.visible_predators():
             print 'avoid predators'
             movement = self.avoid_predators(movement)

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)         

          if self.no_food() and movement > 0:
             print 'move to food'
             movement = self.move_towards_food(movement)

          self.eat_grass()

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)          

          if self.visible_same_species() and movement >0 :
             print 'move to same'
             movement = self.move_to_mate(movement)
             self.mate()

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)

          
         

          print 'rabbit %s %s %s %s \n'%(self.id,self.x,self.y,self.energy)
          return (self.x,self.y)

          
class Wolf(GenomeAgent):
      def __init__(self,env,genome=WOLF,species = 'wolf'):
        super(Wolf,self).__init__(env,genome,species)   
      def chase_prey(self,movement):
         #
         # If a prey gets ahead of the wolf through activation order a new prey may actually be closer
         #
         while (self.visible_prey() and movement > 0):
            closest = self.find_closest_prey(self.getFOV())
            if closest != []:
                 x_move,y_move = self.get_directiontoward(closest[0][1],closest[0][2])
                 self.expend_energy(self.env.moveAgent(self,self.env.wrap(self.x + x_move),self.env.wrap(self.y + y_move)))
                 movement -= 1
         return movement
      def run(self):
          movement = self.movement_rate

          self.age += 0.1
          
          if self.visible_prey():movement = self.chase_prey(movement)

          if self.shoulddie() :
             self.die()
             return (self.x,self.y)
          
          print 'wolf %s %s \n'%(self.x,self.y)
          return (self.x,self.y)
