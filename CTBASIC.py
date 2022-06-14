#!/usr/bin/env python

ABOUT = """
Cyclic Tag BASIC compiler.

Compiles a reduced dialect of BASIC into CT or BCT.

Salpynx, 2022.
"""

import argparse
import json
import re
import sys

STX = '\x02'
ETX = '\x03'
ASM_CT = re.compile(r'^[01;]*$')
BIN = re.compile(r'^[01]*$')


def parse_clear(line):
    n = int(line[6:])
    return clear(n)


def clear(n):
    return ';' * n


def parse_data(line):
    d = json.loads('[' + line[5:] + ']')
    r = data(d)
    return r


def data(lst):
    output = ''
    for item in lst:
        if isinstance(item, str):
            output += ''.join([bin(ord(c))[2:] for c in item]).zfill(8)
        elif isinstance(item, int):
            output += bin(item)[2:]
    return output


def parse_print(line):
    r = []
    s = STX + line[6:].strip('"') + ETX
    for c in s:
        r += [1, c, 0]
    return data(r) # + clear(len(s) * 10)


def parse_asm(line):
    code = line[4:].replace(' ', '')
    assert ASM_CT.match(code)
    return code


def parse_bin(line):
    b = line[4:]
    assert BIN.match(b)
    return b


def compile_(source):
    output = ''
    for line in source:
        line = line.strip()
        append = ''
        if line.startswith('REM') or not line:
            continue
        elif line.startswith('INPUT'):
            pass
        elif line.startswith('DATA'):
            append = parse_data(line) 
        elif line.startswith('BIN'):
            append = parse_bin(line)
        elif line.startswith('CLEAR'):
            append = parse_clear(line)
        elif line.startswith('PRINT'):
            append = parse_print(line)
        elif line.startswith('ASM'):
            append = parse_asm(line)
        elif line.startswith('ENDIF'):
            pass 
        elif line.startswith('END'):
            append = clear(2) 
        output += str(append)
    return output


# From abct output.py
bin_to_bb2 = lambda s: sum([int(c) * 2 ** i for i,c in enumerate(s.replace(' ', '').replace('1', '2').replace('0', '1'))])


def bct(ct):
    return ''.join([f'1{c}' if c != ';' else '0' for c in ct])


def abct(ct):
    b = bct(ct)
    return bin_to_bb2(b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=ABOUT, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('source', help='CTBASIC source file to process', type=argparse.FileType('r'))
    parser.add_argument('--target', '-t', help='Compile target: CT, BCT, ABCT', default='CT')
    parser.add_argument('--debug', '-d', help='Turn on debug output', action='store_true')
    args = parser.parse_args()

    output = compile_(args.source.readlines())
    target = args.target
    if target == 'CT':
        print(output)
    elif target == 'BCT':
        print(bct(output))
    elif target == 'ABCT':
        print(abct(output))
