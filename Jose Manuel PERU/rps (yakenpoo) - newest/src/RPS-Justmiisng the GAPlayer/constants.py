'''
Created on Oct 11, 2012
@author: josemagallanes
'''
ROCK='ROCK'
PAPER='PAPER'
SCISSORS='SCISSORS'
STATES={}
CHOICES=(ROCK, PAPER, SCISSORS)

PAYOFFS={}

for c in CHOICES:
    PAYOFFS[(c,c)]=(0,0)

PAYOFFS[(ROCK, PAPER)]=(-1,1)
PAYOFFS[(ROCK, SCISSORS)]=(1,-1)
PAYOFFS[(PAPER, SCISSORS)]=(-1,1)
PAYOFFS[(PAPER, ROCK)]=(1,-1)
PAYOFFS[(SCISSORS, ROCK)]=(-1,1)
PAYOFFS[(SCISSORS, PAPER)]=(1,-1)

STATES={(ROCK,ROCK):PAPER,(ROCK,PAPER):SCISSORS, (ROCK,SCISSORS):ROCK,
        (PAPER,ROCK):PAPER, (PAPER,PAPER):SCISSORS, (PAPER,SCISSORS):ROCK,
        (SCISSORS,ROCK):PAPER, (SCISSORS,SCISSORS):ROCK, (ROCK,ROCK):PAPER,(SCISSORS,PAPER):SCISSORS}

SEQUENCE=[PAPER, PAPER, ROCK, SCISSORS, ROCK]