class Game:
    '''
    The class that describes the rules of the game.

    Defaults to Rock Paper Scissors, but can be used to describe any game where:
        - Players simultaneously and independently choose an action to play.
        - Both players have the same fixed, constant set of actions.
        - Payoffs are resolved based on both actions.
        - Each round of the game is independent.
        - Probably some other critera as well.

    Other examples include Prisoners' Dilemma, Hawk and Dove, 
    and Rock Paper Scissors Lizard Spock.
    '''

    def __init__(self, action_list = None, payoff_matrix = None):
        '''
        Create a new game model; defaults to Rock Paper Scissors.

        Args:
            action_list: The list of actions each player may take.
            payoff_matrix: Dictionary with the form 
                {(action1, action2): (payoff1, payoff2), ....}
                If a pair of actions don't exist: 
                    If the inverse exists, use that (assume payoff is symmetric)
                    Otherwise, assume the payoff is (0,0)
        '''

        if action_list is None:
            self.action_list = ["R", "P", "S"]
        else:
            self.action_list = action_list

        if payoff_matrix is None:
            self.payoff_matrix = {
                ("R", "P"): (0, 1),
                ("P", "S"): (0, 1),
                ("S", "R"): (0, 1) }

        # Fill in missing elements:
        for action1 in self.action_list:
            for action2 in self.action_list:
                if (action1, action2) not in self.payoff_matrix:
                    if (action2, action1) in self.payoff_matrix:
                        p = self.payoff_matrix[(action2, action1)]
                        self.payoff_matrix[(action1, action2)] = (p[1], p[0])
                    else:
                        self.payoff_matrix[(action1, action2)] = (0, 0)

    def resolve(self, action1, action2):
        '''
        Return a payoff pair for action1, action2

        Args:
            action1: Player1 action
            action2: Player2 action
        Returns:
            (Player1 payoff, player2 payoff)
        '''
        if action1 not in self.action_list or action2 not in self.action_list:
            raise KeyError("Invalid Action!")

        return self.payoff_matrix[(action1, action2)]
