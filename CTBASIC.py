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

PRINTLINE = re.compile(r'("[^"]*"|CHR\$\(\d+\))')


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
    line = PRINTLINE.split(line[6:])
    s = ''
    for v in line:
        v = v.strip()
        if not v:
            continue
        if v.startswith('CHR$'):
            s += chr(int(re.search(r'\d+', v)[0]))
        else:
            s += v.strip('"')
    s = STX + s + ETX
    for c in s:
        r += [1, c, 0]
    return data(r)


def parse_asm(line):
    code = line[4:].replace(' ', '')
    assert ASM_CT.match(code)
    return code


def parse_bin(line):
    b = line[4:].replace(' ', '')
    assert BIN.match(b)
    return b


# FILL / ZFILL parser
def parse_fill(line, fill):
    n = int(line[5:].strip())
    return str(fill) * n


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
        elif line.startswith('FILL'):
            append = parse_fill(line, 1)
        elif line.startswith('ZFILL'):
            append = parse_fill(line, 0)
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


def expandsix(ct):
    """
    Expand CT appendants / productions to be a multiple of 6.
    Using technique described in Cook 2009, 1.0.
    """
    # TODO: short cut -- if the CT is simple and isn't meant to loop (ends with an END of many CLEARs)
    # pad the many ';' to a multiple of 6.
    exp = ''
    for c in ct:
        if c == ';':
            exp += ';' * 6
        elif c in '01':
            exp += c + '0' * 5
    return exp


def rule110(ct, data='1'):
    """
    Compile to Rule 110 'blocks' following the algorithm in 1.4 of:
Cook, Matthew (2009). "A Concrete View of Rule 110 Computation". In Neary, T.; Woods, D.; Seda, A. K.; Murphy, N. (eds.).
Electronic Proceedings in Theoretical Computer Science. Vol. 1. pp. 31–55.
doi: 10.4204/EPTCS.1.4 (https://doi.org/10.4204/EPTCS.1.4)
    """
    appendants = ct.split(';')[:-1]
    count = len(appendants)
    if (count % 6) != 0:
        return rule110(expandsix(ct), data)

    central = 'C' + data.replace('0', 'ED').replace('1', 'FD')
    central = central[:-1] + 'G'
    right = ''
    empty = 0
    for a in appendants:
        if not a:
            empty += 1
            right += 'L'
            continue
        d = a.replace('0', 'IJ').replace('1', 'II')
        d = 'KH' + d[1:]
        right += d
    right = right[1:] + right[0]
    v = (76 * ct.count('1') +
         + 80 * ct.count('1')
         + 60 * (count - empty)
         + 43 * empty)
    left = 'A' * v + 'B' + 'A' * 13 + 'B' + 'A' * 11 + 'B' + 'A' * 12 + 'B'
    return left, central, right


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
    elif target == '110':
        print(rule110(output, data='1'))
