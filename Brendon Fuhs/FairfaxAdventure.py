# FairfaxAdventure.py
#
# A less than epic adventure in downtown Fairfax, VA
# created 9-13-2012 by Brendon Fuhs
##

import random

# Each location in the world map has associated with it
# a description, a designator of whether it's intact (LocationCondition),
# and possible directions one may head away from the location
WorldMap = {}
WorldMap [(0,1)] = ["Sager Ave and Chain Bridge Rd",0,{"N","E"}]
WorldMap [(0,2)] = ["Sager Ave and University Dr",0,{"N","E","W"}]
WorldMap [(0,3)] = ["Sager Ave and East St",0,{"N","W"}]
WorldMap [(1,0)] = ["Main St and West St",0,{"N","E"}]
WorldMap [(1,1)] = ["Main St and Chain Bridge Rd",0,{"N","S","E","W"}]
WorldMap [(1,2)] = ["Main St and University Dr",0,{"N","S","E","W"}]
WorldMap [(1,3)] = ["Main St and East St",0,{"N","S","W"}]
WorldMap [(2,0)] = ["North St and West St",0,{"S","E"}]
WorldMap [(2,1)] = ["North St and Chain Bridge Rd",0,{"S","E","W"}]
WorldMap [(2,2)] = ["North St and University Dr",0,{"S","E","W"}]
WorldMap [(2,3)] = ["North St and East St",0,{"S","W"}]

LocationCondition = ["Everything looks like peaches and cream here.",
                        "You are standing amidst smoldering ruins."]

class character():
    _location_ = () # location in WorldMap
    direction = "Q" # direction of the next move
    def setLocation(self,possibleLocations):    # for initial setting of location
        self._location_ = random.choice(list(possibleLocations))
    def move(self):
        if (self.direction == "E"):
            self._location_ = (self._location_[0],self._location_[1]+1)
        if (self.direction == "W"):
            self._location_ = (self._location_[0],self._location_[1]-1)
        if (self.direction == "N"):
            self._location_ = (self._location_[0]+1,self._location_[1])
        if (self.direction == "S"):
            self._location_ = (self._location_[0]-1,self._location_[1])

Player = character()    # Our hero, you.
Clown = character()     # The evil villain

# Generate initial Player locations
Player.setLocation(WorldMap.keys())

# To generate the initial Clown location, I made sure that it wasn't in the same place as the Player,
# and then I also ran into a weird graph-theoretric problem where they apparently never meet if they're
# placed wrong, so I think making sure the coordinates of their locations sum to the same parity gets
# me around that problem.
while True:
    Clown.setLocation(WorldMap.keys())
    if ( (Clown._location_ != Player._location_) and
         (Clown._location_[0]+Clown._location_[1])%2 == (Player._location_[0]+Player._location_[1])%2 ):
        break

# Set the scene.
print "You are a superhero tasked with saving Fairfax, Virginia."
print "There is is a clown eating town."
print "You realize this is a good thing."
print "All those brick sidewalks and condos pretending to be townhouses..."
print "Really, you should be helping the clown, but unfortunately, "
print "the line between superhero and supervillain is a matter of "
print "public perception rather than objective truth."
print "Just try to avoid the clown as long as possible without leaving downtown."

# Game Loop
while True:

    ### Can test stuff here
    # print Player._location_
    # print Clown._location_

    # First, clown destroys stuff where it's at
    WorldMap[Clown._location_][1] = 1

    # Give description of Player's location
    print "You are at "
    print WorldMap[Player._location_][0]

    # Tell us whether it's still intact
    print LocationCondition[WorldMap[Player._location_][1]]

    if (Clown._location_ == Player._location_):
        break

    # prompt for Player.direction
    while True:
        print "You may go any of the following directions..."
        print WorldMap[Player._location_][2]
        direction = raw_input("Enter the direction you wish to head...")
        if direction in WorldMap[Player._location_][2]:
            Player.direction = direction
            break
    # set clown direction
    Clown.direction = random.choice( list( WorldMap[Clown._location_][2] ) )

    Player.move()
    Clown.move()

# Now we see how much the clown managed to destroy
destructionAmount=0
for x in WorldMap.keys():
    if (WorldMap[x][1]==1):
        destructionAmount = destructionAmount+1

destructionPercentage = float(destructionAmount)/11.0 * 100.0

print "The Clown is here."
print "You reluctantly apprehend The Clown, who is trying to make you laugh."
print "Your procrastination successfully enabled the destruction of "
print destructionPercentage
print "% of Fairfax's historic downtown."
