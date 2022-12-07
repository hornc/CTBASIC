REM Test Tek4010 animation
REM Uses CLS command

PRINT "Tektronix 4010 animation in bitwise cyclic tag."
BIN 1
CLEAR 491

REM Vertical line
PRINT CHR$(29) ")b0@/j0@" CHR$(31)
BIN 1
CLEAR 121

CLS
BIN 1
CLEAR 71

PRINT "Tektronix 4010 animation in bitwise cyclic tag."
BIN 1
CLEAR 491

REM Horizontal line
PRINT CHR$(29) ",f,R,f3N" CHR$(31)
BIN 1
CLEAR 121

CLS
BIN 1
CLEAR 71
