REM Output an asterisk between 0 and 10 times based on input
REM INPUT: Unary encode a number between 1 and 10
REM e.g. for 5:
REM INPUT: 11111
REM OUTPUT: "* * * * *"

REM Pad input to be at least 10 bits
ZFILL 10

PRINT "* ";

REM Decrement our unary counter by one
CLEAR 1

REM Do this up to nine more times:
PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

PRINT "* ";
CLEAR 1

REM Make sure we clear the entire maximum possible datastring up to this point to halt
CLEAR 510
