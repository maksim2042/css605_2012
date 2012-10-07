
from statemachine import StateMachine

#simple agent class containing state machine
class SimpleAgent:
    def __init__(self):
        self.stateMachine = FiniteStateMachine()
        move_states = ["Forward","Reverse", "Left", "Right"]
        active_states = ["Hit", "Walk", "Surrender", "Die"]
        conjunction_state = ["and", "or", "not" ]
      
        #run the action on the state machine
    def Run(self, action1, action2):
        self.stateMachine.run(action1, action2)
    
        #check transitions
    def transitions(txt, state):
        splitted_txt = txt.split(None,1)
        word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
        if state == "Start":
            if word == "Go":
                newState = "move_states"
            else:
                newState = "error_state"
            return (newState, txt)
        elif state == "move_states":
            if word == "is":
                newState = "is_state"
            else:
                newState = "error_state"
            return (newState, txt) 
        elif state == "conjunction_state":
            if word == "not":
                newState = "not_state"
            elif word in move_states:
                newState = "move_state"
            elif word in active_states:
                newState = "active_state"
            else:
                newState = "error_state"
            return (newState, txt)
        elif state == "not_state":
            if word in move_states:
                newState = "move_state"
            elif word in active_states:
                newState = "active_state"
            else:
                newState = "error_state"
            return (newState, txt)
            
