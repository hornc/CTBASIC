#!/usr/bin/env python

ABOUT = """
Simple (unobfuscated) Cyclic Tag interpreter.
With output encoding method taken from
https://github.com/hornc/abctag
"""

import argparse
import re

CT = '01;'
OUTPUT = re.compile(r'1000000100(1[01]{8}0)*1000000110$')


def output(s):
    if not s.endswith('1000000110'):
         return
    m = OUTPUT.search(s)
    if m:
        t = m.group(0)[10:-10]
        return ''.join([chr(int(t[i+1:i+9], 2)) for i in range(0, len(t), 10)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=ABOUT)
    parser.add_argument('source', help='CT source file to process', type=argparse.FileType('r'))
    parser.add_argument('input', help='Input (binary)', default='1')
    parser.add_argument('--debug', '-d', help='Datastring output', action='store_true', default=False)
    args = parser.parse_args()

    datastring = args.input
    code = args.source.read()

    pos = 0
    while len(datastring):
        c = code[pos]
        pos = (pos + 1) % len(code)
        if c not in CT:
            continue
        if c == ';':
            datastring = datastring[1:]
        elif datastring[0] == '1':
            datastring += c
            o = output(datastring)
            if o:
                print(o, end='', flush=True)
        if args.debug:
            print(datastring)
