REM Test Tek4010 animation
REM Uses CTBASIC graphics commands

REM Each loop:
REM * Only run INIT on first pass
REM * print TITLE TEXT every pass
REM * Output Vertical line on even passes
REM * Output Horizontal line on odd passes

REM INIT
BIN 110
CLEAR 1

REM TITLE TEXT
CLS
PRINT "Tektronix 4010 animation in bitwise cyclic tag."
BIN 1
CLEAR 1

REM Vertical line
PLOT 500, 500
DRAW 0, -200
BIN 0101
CLEAR 1

REM Horizontal line
PLOT 400, 400
DRAW 200, 0
BIN 0110
CLEAR 1

CLEAR 681
