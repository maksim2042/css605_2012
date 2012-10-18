"""
building Nodes
"""

def START(a):
	if a == '0':
		return ROCK
	elif a == '1':
		return PAPER
	elif a == '2':
		return SCISSORS

def ROCK(a):
	if a == '0':
		return ROCK
	elif a == '1':
		return PAPER
	elif a == '2':
		return SCISSORS
	

def PAPER(a):
	if a == '0':
		return ROCK
	elif a == '1':
		return PAPER
	elif a == '2':
		return SCISSORS

def SCISSORS(a):
	if a == '0':
		return ROCK
	elif a == '1':
		return PAPER
	elif a == '2':
		return SCISSORS