"""
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program has
several bugs in it. Run through the program a few times to find the bugs
that keep the program from working correctly

This is a bit different. It's not a program that can be considered "complete"
I'll post what I did with my logging module, but yours may be different.
I tried to add comments on the parts of the code I added, but since there is no
"solution", your code will look different.
"""
# While initially running the code, it turns out the user always loses.
# Let's set up a logging sequence.

import random
import logging  # was not in original code
# logging.disable(logging.CRITICAL)  # STOPS ALL ERRORS

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - '
                '%(levelname)s - %(message)s')  # was not in original code

logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess')  # was not in original code
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()

logging.debug('Start of coin toss')  # was not in original code
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# we need to convert heads/tails to 0/1, or visa versa
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')  # not in original code

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
