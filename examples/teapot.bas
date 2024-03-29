REM Utah Teapot

REM Created using the original patch data shown at:
REM https://www.sjbaker.org/wiki/index.php?title=The_History_of_The_Teapot
REM Taking only the 2D X, and Z bezier patch corners,
REM using a control point from the lid because it looks better,
REM and scaling for the Tektronix 1024 x 780 display.

PRINT "Utah teapot X, Z patch corners:"

REM Rim
PLOT 691, 624
DRAW -179, 0
DRAW 0, 0
DRAW 192, 0
DRAW -13, 0

REM Body
PLOT 704, 624
DRAW -384, 0
DRAW -64, -147
DRAW 512, 0
DRAW -64, 147
PLOT 768, 477
DRAW -512, 0
DRAW 64, -73
DRAW 384, 0
DRAW 64, 73

REM Lid
PLOT 512, 697
DRAW 57, 0
DRAW -32, -44
DRAW -50, 0
DRAW -32, 44
DRAW 57, 0
PLOT 537, 653
DRAW -50, 0
DRAW -141, -29
DRAW 332, 0
DRAW -141, 29

REM Handle
PLOT 307, 587
DRAW 13, 22
DRAW -192, -44
DRAW 38, 0
DRAW 141, 22
PLOT 166, 565
DRAW -38, 0
DRAW 140, -117
DRAW -12, 29
DRAW -90, 88

REM Spout
PLOT 729, 528
DRAW 0, -80
DRAW 205, 176
DRAW -77, 0
DRAW -128, -96
PLOT 857, 624
DRAW 77, 0
DRAW -13, 0
DRAW -51, 0
DRAW -13, 0

END
