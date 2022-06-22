REM Loop 10 times, printing an asterisk followed by a space each time.
REM Currently does not terminate cleanly.


REM INIT:
  BIN  110
  BIN 0010 0010 0010 0010 0010 0010 0010 0010 
  BIN 0011
  CLEAR 1

REM START string output:
  BIN 1 00000010 0
  CLEAR 1

REM MAIN BLOCK, output:
  DATA 1, "*", 0, 1, " ", 0
  CLEAR 1

REM END string output:
  BIN 1 00000011 0
  CLEAR 1
