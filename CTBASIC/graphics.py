import re
from CTBASIC.chars import ESC, GS

MATCH = re.compile(r'PLOT|DRAW|INK')
COORDS = re.compile(r'(-?\d+)\s*,\s*(-?\d+)')


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
    return ''.join([chr(v) for v in [hY + 32, lY + 96, hX + 32, lX + 64]])


class Graphics:
    def __init__(self):
        self.output = GS
        self.plotpos = (0, 0)

    def coords(self, line):
        """Returns a tuple [a, b] of statement arguments."""
        return [int(v) for v in COORDS.search(line[4:]).groups()]

    def parse(self, line):
        if line.startswith('PLOT'):
            a, b = self.coords(line)
            self.plotpos = (a, b)
            self.output += GS + tekpoint(a, b) * 2
        elif line.startswith('DRAW'):
            a, b = self.coords(line)
            x, y = self.plotpos
            self.plotpos = (x + a, y + b)
            self.output += tekpoint(*self.plotpos)
        elif line.startswith('INK'):
            c = int(line[3:].strip())
            inks = '`abcdhijkl'
            self.output += f'{ESC}{inks[c]}'

    def append(self, line):
        self.parse(line)

    def end(self):
        return self.output
