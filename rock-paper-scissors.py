"""
This is an attempt to build a Rock-Paper-Scissors Game
The game is between two automatic players.
To start the game enter "game()" at the python prompt.
To check the score enter "score()" at the python prompt.
To reset the score enter "reset()" at the python prompt.
"""

class player_1():
	choice = "none"
	wins = 0

class player_2():
	choice = "none"
	wins = 0
	
def shoot():
	import random
	p = ['rock','paper','scissors']
	player_1.choice = random.choice(p)
	print 'player 1 throws',player_1.choice
	player_2.choice = random.choice(p)
	print 'player 2 throws',player_2.choice
	
def winner():
	if player_1.choice == player_2.choice:
		w = 'draw!'
	elif player_1.choice == 'rock' and player_2.choice == 'scissors':
		w = 'player 1 wins!'
	elif player_1.choice == 'paper' and player_2.choice == 'rock':
		w = 'player 1 wins!'
	elif player_1.choice == 'scissors' and player_2.choice == 'paper':
		w = 'player 1 wins!'
	else:
		w = 'player 2 wins!'
	print w
	if w == 'player 1 wins!':
		player_1.wins = player_1.wins + 1
	if w == 'player 2 wins!':
		player_2.wins = player_2.wins + 1
		
def game():
	shoot()
	winner()
	print '---------------'
	score()

def score():
	if player_1.wins == 1:
		print 'player 1 has',player_1.wins,' win'
	else:
		print 'player 1 has',player_1.wins,' wins'
	if player_2.wins == 1:
		print 'player 2 has',player_2.wins,' win'
	else:
		print 'player 2 has',player_2.wins,' wins'

def reset():
	player_1.wins = 0
	player_2.wins = 0
	print 'player 1 has',player_1.wins,' wins'
	print 'player 2 has',player_2.wins,' wins'
