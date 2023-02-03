# Character codes and control sequences

STX = '\x02'
ETX = '\x03'

# ASCII Character codes, and Tektronix 401x effect.
FF = chr(12)   # As second character after ESC: clear screen.
ESC = chr(27)  # Terminal "arming" character.
GS = chr(29)   # Sets terminal to Graph Mode.
US = chr(31)   # Resets terminal from Graph to Alpha Mode.

# Character and control codes used for clearing screen in various terminal modes:
CAN = chr(24)  # ASCII cancel, used as a NOP padding character in the combined ANSI control / Tek4010 CLS
ANSI_HOME = f'{ESC}[H'
ANSI_CLEAR = f'{ESC}[J'
RIS = f'{ESC}c'  # ANSI control Reset to Initial State (does not work on TEK4010)
CLS_TEK = f'{ESC}{FF}'  # Tektronix 4010 clear screen
CLS_ANSI = f'{ANSI_HOME}{ANSI_CLEAR}'  # ANSI control clear screen
CLS_BOTH = f'{CLS_TEK}c{CLS_TEK}{CAN}'  # 6 bytes long, combination ANSI RIS and TEK CLS
CLS = STX + CLS_BOTH + ETX

