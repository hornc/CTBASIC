REM Loop 10 times, printing an asterisk followed by a space each time.
REM Currently does not terminate cleanly.

REM state flag: 10 = 1
REM state flag: 01 = 0

REM INIT:
  BIN 0
  BIN   101001
  BIN 01011001 01011001 01011001 01011001 01011001 01011001 01011001 01011001 
  BIN 01011010
  CLEAR 2

REM START string output:
  REM Start of text (STX, ASCII 02)
  DATA 1, CHR$(02), 0
  CLEAR 2

REM MAIN BLOCK, output:
  DATA 1, "*", 0, 1, " ", 0
  CLEAR 2


REM END string output:
  REM Newline (ASCII 10)
  DATA 1, CHR$(10), 0
  REM End of text (ETX, ASCII 03)
  DATA 1, CHR$(03), 0
  CLEAR 2
