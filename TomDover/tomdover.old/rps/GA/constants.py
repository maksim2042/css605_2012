ROCK='ROCK'
PAPER='PAPER'
SCISSORS='SCISSORS'

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