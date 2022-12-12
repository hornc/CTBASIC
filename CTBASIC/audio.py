"""
Very experimental attempt to emulate ZX Spectrum audio
via BEEP and piping terminal output to aplay...
"""
import re


ARGS = re.compile(r'(\.?\d+)\s*,\s*(-?\d+)')


def match(line):
    return line.startswith('BEEP')


def parse(line):
    duration, pitch = ARGS.search(line[4:]).groups()
    duration = float(duration)
    pitch = int(pitch)
    #print('DEBUG:', duration, pitch)
    return 'ccccc\n'
