import re


MATCH = re.compile(r'PLOT|DRAW|INK')
COORDS = re.compile(r'(-?\d+)\s*,\s*(-?\d+)')

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
CLS_BOTH = f'{RIS}{ESC}{FF}{CAN}'  # 5 bytes long
CLS = CLS_BOTH


def match(line):
    return bool(MATCH.match(line))


def tekpoint(x, y):
    """
    Converts an x, y coordinate into 4 byte Tek 401x coord.
    x range: 0 to 1023
    Visible y range: 0 to 779
    Origin 0, 0 is at bottom-left corner.
    """
    hX = (x & 0xffe0) >> 5
    lX = x & 0x1f
    hY = (y & 0xffe0) >> 5
    lY = y & 0x1f
    #print(f'X: {hX} {lX} , {hY} {lY}')
    return ''.join([chr(v) for v in [hY + 32, lY + 96, hX + 32, lX + 64]])


class Graphics:
    def __init__(self):
        self.output = GS
        self.plotpos = (0, 0)
        self.last = None

    def coords(self, line):
        """Returns a tuple [a, b] of statement arguments."""
        return [int(v) for v in COORDS.search(line[4:]).groups()]

    def parse(self, line):
        if line.startswith('CLS'):
            self.plotpos = (0, 0)
            self.output += CLS

        if line.startswith('PLOT'):
            a, b = self.coords(line)
            if self.last == 'PLOT':
                self.output += tekpoint(*self.plotpos) + US + GS
            self.plotpos = (a, b)
            self.output += tekpoint(a, b)
            self.last = 'PLOT'
        elif line.startswith('DRAW'):
            a, b = self.coords(line)
            x, y = self.plotpos
            self.plotpos = (x + a, y + b)
            self.output += tekpoint(*self.plotpos)
            self.last = 'DRAW'
        elif line.startswith('INK'):
            c = int(line[3:].strip())
            inks = '`abcdhijkl'
            self.output += f'{ESC}{inks[c]}'

    def append(self, line):
        self.parse(line)

    def end(self):
        return self.output
