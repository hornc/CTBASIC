REM Display the various line styles.

REM Draw zig-zag lines in different INKs
PLOT 50, 400
DRAW 50, 250
INK 1
DRAW 50, -250
INK 2
DRAW 50, 250
INK 3
DRAW 50, -250
INK 4
DRAW 50, 250
INK 5
DRAW 50, -250
INK 6
DRAW 50, 250
INK 7
DRAW 50, -250

REM Some more normal mode zig-zags
REM for potentially testing other drawing styles later.
INK 0
DRAW 50, 250
DRAW 50, -250
DRAW 50, 250
DRAW 50, -250
DRAW 50, 250

CLEAR 10 
