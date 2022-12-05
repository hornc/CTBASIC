REM Loop 10 times, printing an asterisk followed by a space each time.
REM Currently does not terminate cleanly.


REM INIT:
REM Pad every post-end flag with 41 bits which are cleared every loop
REM This seems inefficient, but it might be possible to build this padded structure
REM by running an build-init-loop, before entering a main-loop state?
  BIN  110
  ZFILL 41
  BIN 0010 
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010
  ZFILL 41
  BIN 0010 
  ZFILL 41
  BIN 0011
  CLEAR 1

REM START string output:
  REM Start of text (STX, ASCII 02)
  DATA 1, CHR$(02), 0
  CLEAR 1

REM MAIN BLOCK, output:
  DATA 1, "*", 0, 1, " ", 0
  CLEAR 1


REM END string output:
  REM Newline (ASCII 10)
  DATA 1, CHR$(10), 0
  REM End of text (ETX, ASCII 03)
  DATA 1, CHR$(03), 0
  CLEAR 1
  CLEAR 41
