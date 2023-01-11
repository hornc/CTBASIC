REM Coin Flip interactive "game".


REM Intro:
PRINT "COIN FLIP"
PRINT "========="

PRINT "Let's play a game!"
PRINT "I have a coin, can you guess the result if I flip it?"
BIN 1
CLEAR 1011


REM Game loop:
PRINT "To guess HEADS enter: 10"
PRINT "To guess TAILS enter: 01"
CLEAR 541


PRINT "Ok, I'll flip the coin now...."
PRINT "TAILS"
BIN 1
CLEAR 1

PRINT "Ok, I'll flip the coin now...."
PRINT "HEADS"
BIN 1
CLEAR 1


PRINT "You lose, I win."
PRINT "Try again?"

ZFILL 281
BIN 1
CLEAR 1
