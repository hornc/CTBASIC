REM Loop 10 times, printing an asterisk followed by a space each time.

REM State: init, output, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10A
REM Program loop:
REM   Destructively read state, fixed width output, append next state, clear all current state, clear last output. 

REM INIT:
  BIN  11000000000
  CLEAR 1

REM OUTPUT:
  REM Start of text (STX, ASCII 02)
  DATA 1, CHR$(02), 0
  DATA 1, "*", 0, 1, " ", 0
  REM End of text (ETX, ASCII 03)
  DATA 1, CHR$(03), 0
  CLEAR 1

REM STATE TRANSITIONS:
REM 1:
  BIN 010100000000
  CLEAR 1
REM 2:
  BIN 010010000000
  CLEAR 1
REM 3:
  BIN 010001000000
  CLEAR 1
REM 4:
  BIN 010000100000
  CLEAR 1
REM 5:
  BIN 010000010000
  CLEAR 1
REM 6:
  BIN 010000001000
  CLEAR 1
REM 7:
  BIN 010000000100
  CLEAR 1
REM 8:
  BIN 010000000010
  CLEAR 1
REM 9:
  BIN 010000000001
  CLEAR 1
REM 10:
  BIN 000000000001
  CLEAR 1

REM CLEAR FIXED OUTPUT
  CLEAR 40
