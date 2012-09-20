import types as t
import interface as i
import random

def start():
	i.interface()
	if t.new_game == 'y':
		game()
	else:
		score()

class Player_1():
	player_type = 'none'
	move = 'none'
	seq = 1
	wins = 0
        		
class Player_2():
	player_type ='none'
	move = 'none'
	seq = 1
	wins = 0

def game():
	referee()
	winner()
	choices()
		

def choices():
	again = raw_input('\n\
        Would you like to...\n\
        play again <p>, \n\
        check scores <s>, \n\
        or choose a different strategy <c>)?')
	if again == 'p':
		game()
	elif again == 's':
		score()
	elif again == 'c':
		start()
	else:
		choices()
			
        
def referee():
	p = ['rock','paper','scissors']
	
	if t.p1_type == 'q':
		if Player_1.seq % 3 == 1:
			Player_1.move = 'rock'
		elif Player_1.seq % 3 == 2:
			Player_1.move = 'paper'
		else:
			Player_1.move = 'scissors'		
			
	elif t.p1_type == 'r':
		Player_1.move = random.choice(p)
		
	elif t.p1_type == 's':
		if Player_1.seq == 1:
			Player_1.move = random.choice(p)
		else:
			Player_1.move = Player_1.move
			
	else:
		print 'done'
	
	Player_1.seq = Player_1.seq + 1
		
	if t.p2_type == 'q':
		if Player_2.seq % 3 == 1:
			Player_2.move = 'rock'
		elif Player_2.seq % 3 == 2:
			Player_2.move = 'paper'
		else:
			Player_2.move = 'scissors'
			
	elif t.p2_type == 'r':
		Player_2.move = random.choice(p)
	
	elif t.p2_type == 's':
		if Player_2.seq == 1:
			Player_2.move = random.choice(p)
		else:
			Player_1.move = Player_1.move
			
	else:
		print 'done'
	
	Player_2.seq = Player_2.seq + 1
	
	print '\n\
	'
	print 'Player 1 throws',Player_1.move
	print 'Player 2 throws',Player_2.move
	print '--------------'
	
def winner():
	if Player_1.move == Player_2.move:
		w = 'draw!'
	elif Player_1.move == 'rock' and Player_2.move == 'scissors':
		w = 'player 1 wins!'
	elif Player_1.move == 'paper' and Player_2.move == 'rock':
		w = 'player 1 wins!'
	elif Player_1.move == 'scissors' and Player_2.move == 'paper':
		w = 'player 1 wins!'
	else:
		w = 'player 2 wins!'
	print w
	if w == 'player 1 wins!':
		Player_1.wins = Player_1.wins + 1
	if w == 'player 2 wins!':
		Player_2.wins = Player_2.wins + 1

def score():
	print '\n\
	'
	if Player_1.wins == 1:
		print 'Player 1 has',Player_1.wins,' win'
	else:
		print 'Player 1 has',Player_1.wins,' wins'
	if Player_2.wins == 1:
		print 'Player 2 has',Player_2.wins,' win'
	else:
		print 'Player 2 has',Player_2.wins,' wins'
	reset_scores = raw_input('Do you want to reset your scores?')
	if reset_scores == 'y':
		reset()
	else:
		choices()

def reset():
	Player_1.wins = 0
	Player_2.wins = 0
	Player_1.seq = 1
	Player_2.seq = 1
	print 'Player 1 has',Player_1.wins,' wins'
	print 'Player 2 has',Player_2.wins,' wins'
	choices()
