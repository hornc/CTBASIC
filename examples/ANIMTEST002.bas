REM Test Tek4010 animation
REM Uses CTBASIC graphics commands

PRINT "Tektronix 4010 animation in cyclic tag.";
BIN 1
CLEAR 421

REM Vertical line
PLOT 500, 500
DRAW 0, -200
BIN 1
CLEAR 161

CLS
BIN 1
CLEAR 81

PRINT "Tektronix 4010 animation in cyclic tag.";
BIN 1
CLEAR 421

REM Horizontal line
PLOT 400, 400
DRAW 200, 0
BIN 1
CLEAR 161

CLS
BIN 1
CLEAR 81
