REM Test Tek4010 animation
REM Works WITHOUT CTBASIC graphics commands.

PRINT "Tektronix 4010 animation in cyclic tag.";
BIN 1
CLEAR 421

REM Vertical line
PRINT CHR$ 29 + ")b0@/j0@" + CHR$ 31;
BIN 1
CLEAR 131

PRINT CHR$ 27 + CHR$ 12;
BIN 1
CLEAR 51

PRINT "Tektronix 4010 animation in cyclic tag.";
BIN 1
CLEAR 421

REM Horizontal line
PRINT CHR$ 29 + ",f,R,f3N" + CHR$ 31;
BIN 1
CLEAR 131

PRINT CHR$ 27 + CHR$ 12;
BIN 1
CLEAR 51

