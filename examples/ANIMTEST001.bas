REM Test Tek4010 animation
REM Works WITHOUT CTBASIC graphics commands.

PRINT "Tektronix 4010 animation in bitwise cyclic tag.";
BIN 1
CLEAR 491

REM Vertical line
PRINT CHR$ 29 + ")b0@/j0@" + CHR$ 31;
BIN 1
CLEAR 121

PRINT CHR$ 27 + CHR$ 12;
BIN 1
CLEAR 41

PRINT "Tektronix 4010 animation in bitwise cyclic tag.";
BIN 1
CLEAR 491

REM Horizontal line
PRINT CHR$ 29 + ",f,R,f3N" + CHR$ 31;
BIN 1
CLEAR 121

PRINT CHR$ 27 + CHR$ 12;
BIN 1
CLEAR 41

