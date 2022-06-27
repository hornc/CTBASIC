import re

MATCH = re.compile(r'PLOT|DRAW')
COORDS = re.compile(r'(-?\d+)\s*,\s*(-?\d+)')

plotpos = (0, 0)

def match(line):
    return bool(MATCH.match(line))


def tekpoint(x, y):
    hX = (x & 0xffe0) >> 5
    lX = x & 0x1f
    hY = (y & 0xffe0) >> 5
    lY = y & 0x1f
    #print(f'X: {hX} {lX} , {hY} {lY}')
    return ''.join([chr(v) for v in [hY + 32, lY + 96, hX + 32, lX + 64]])


def parse(line):
    global plotpos
    a, b = [int(v) for v in COORDS.search(line[4:]).groups()]
    if line.startswith('PLOT'):
        plotpos = (a, b)
        return chr(29) + tekpoint(a, b) * 2 + chr(31)
    if line.startswith('DRAW'):
        x, y = plotpos
        plotpos = (x + a, y + b)
        return chr(29) + tekpoint(x, y) + tekpoint(*plotpos) + chr(31)

