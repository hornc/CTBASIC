import re

MATCH = re.compile(r'PLOT|DRAW|CLS')
MATCH = re.compile(r'PLOT|DRAW')
COORDS = re.compile(r'(-?\d+)\s*,\s*(-?\d+)')

plotpos = (0, 0)

# ASCII Character codes, and Tektronix 401x effect.
FF = chr(12)   # As second character after ESC: clear screen.
ESC = chr(27)  # Terminal "arming" character.
GS = chr(29)   # Sets terminal to Graph Mode.
US = chr(31)   # Resets terminal from Graph to Alpha Mode.


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


def parse(line):
    global plotpos
    if line.startswith('CLS'):
        plotpos = (0, 0)
        return ESC + FF


class Graphics:
    def __init__(self):
        self.output = GS
        self.plotpos = (0, 0)
        self.last = None

    def parse(self, line):
        if line.startswith('CLS'):
            self.plotpos = (0, 0)
            self.output += ESC + FF

        a, b = [int(v) for v in COORDS.search(line[4:]).groups()]
        if line.startswith('PLOT'):
            if self.last == 'PLOT':
                self.output += tekpoint(*self.plotpos) + US + GS
            self.plotpos = (a, b)
            self.output += tekpoint(a, b)
            self.last = 'PLOT'
        if line.startswith('DRAW'):
            x, y = self.plotpos
            self.plotpos = (x + a, y + b)
            self.output += tekpoint(*self.plotpos)
            self.last = 'DRAW'

    def append(self, line):
        self.parse(line)

    def end(self):
        return self.output
