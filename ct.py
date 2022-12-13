#!/usr/bin/env python

ABOUT = """
Simple (unobfuscated) Cyclic Tag interpreter.
With output encoding method taken from
https://github.com/hornc/abctag
"""

import argparse
import re
from time import sleep
from CTBASIC.graphics import CLS_TEK as CLS

CT = '01;'
STX = '1000000100'
ETX = '1000000110'
OUTPUT = re.compile(STX + r'(1[01]{8}0)*' + ETX + r'$')
R_STX = STX[::-1]
R_ETX = ETX[::-1]
R_OUTPUT = re.compile(r'^' + R_ETX + r'(0[01]{8}1)*?' + R_STX)


def output(s):
    if not s.endswith(ETX):
        return
    m = R_OUTPUT.search(s[::-1])
    if m:
        t = m.group(0)[-11:9:-1]
        return ''.join([chr(int(t[i+1:i+9], 2)) for i in range(0, len(t), 10)])


def main(args=None):
    parser = argparse.ArgumentParser(description=ABOUT)
    parser.add_argument('source', help='CT source file to process.', type=argparse.FileType('r'))
    parser.add_argument('input', help='Input (binary string). Defaults to "1".', nargs='?', default='1')
    parser.add_argument('--debug', '-d', help='Program-string and Data-string output (tab separated).', action='store_true', default=False)
    parser.add_argument('--hold', help='Hold delay before clearing screen (CLS), in ms.', type=float, default=0)
    args = parser.parse_args()

    datastring = args.input
    code = args.source.read()

    pos = 0
    while len(datastring):
        c = code[pos]
        if args.debug:
            print('\t'.join([code[pos:].strip() + code[:pos], datastring]))
        pos = (pos + 1) % len(code)
        if c not in CT:
            continue
        if c == ';':
            datastring = datastring[1:]
        elif datastring[0] == '1':
            datastring += c
            o = output(datastring)
            if o and not args.debug:
                if args.hold and CLS in o:
                    sleep(args.hold / 1000)
                print(o, end='', flush=True)


if __name__ == '__main__':
    main()
