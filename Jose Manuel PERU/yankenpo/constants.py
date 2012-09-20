'''
Created on Sep 13, 2012
you need to use yankenpo
to see how the game run!!!
@author: josemagallanes
'''


CHOICES=('ROCK', 'PAPER', 'SCISSORS')

PAYOFFS={ ('ROCK', 'PAPER'): (-1, 1), ('PAPER', 'PAPER'): (0, 0), ('SCISSORS', 'PAPER'): (1, -1),
         ('ROCK', 'ROCK'): (0, 0), ('SCISSORS', 'SCISSORS'): (0, 0), ('PAPER', 'SCISSORS'): (-1, 1), 
         ('PAPER', 'ROCK'): (1, -1), ('SCISSORS', 'ROCK'): (-1, 1), ('ROCK', 'SCISSORS'): (1, -1) }