from simple_agent import SimpleAgent

 
#instantiate main, create 100 state variables
if __name__== "__main__":
    
    stateMachines = []
    for i in range(0,100):
        stateMachines.append(SimpleAgent())
          
    #run until all are dead
    while True:
        for i in range(0,100):
            stateMachines[i].run("move forward", "move left")
