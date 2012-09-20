import types as t
player_types = {'s':'stupid','q':'sequence','r':'random','t':'tit4tat','h':'manual','m':'machine learning','v':'markov','u':'unknown'}

def interface():
	print '\n\
	Welcome to Rock-Paper-Scissors\n\
	Please define the strategy of each of the two players as\n\
        s = stupid\n\
        q = sequence\n\
        r = random\n\
        t = tit4tat\n\
        h = manual\n\
        m = machine learning\n\
        v = markov'
	t.p1_type = raw_input('Player 1:')
	t.p2_type = raw_input('Player 2:')
	print '--------------------------------------------------'
	print 'Player 1 will be playing a',player_types[t.p1_type],'strategy...'
	print 'Player 2 will be playing a',player_types[t.p2_type],'strategy...\n\
	'
	t.new_game = raw_input('Would you like to throw?')
	
