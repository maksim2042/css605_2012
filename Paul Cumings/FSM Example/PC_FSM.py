"""
This class implements a very stupid simple FSM for moving and creating actions
"""

class SimpleFSM:
    def __init__(self):
        self.handlers = {}
        self.endStates = []
        self.startState = None
        
        
    def add_state_element(self, name, handler, end_state=0):
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_beginning(self, name):
        self.startState = name

    def run(self, content):
        if self.startState in self.handlers:
            handler = self.handlers[self.startState]
        else:
            raise "Error", ".set_start() has to be called before .run()"
        if not self.endStates:
            raise  "Error", "at least one state must be an end_state"

        oldState = self.startState
        while 1:
            (newState, content) = handler(content, oldState)
            if newState in self.endStates:
                print "state hit ", newState, "which is an end state"
                break 
            else:
                handler = self.handlers[newState]
            oldState = newState