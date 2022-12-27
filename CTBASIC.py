#!/usr/bin/env python

ABOUT = """
Cyclic Tag BASIC compiler.

Compiles a reduced dialect of BASIC into CT or BCT.

Salpynx, 2022.
"""

import argparse
import re
import sys

from CTBASIC.rule110 import rule110
from CTBASIC import graphics
from CTBASIC.graphics import Graphics

STX = '\x02'
ETX = '\x03'
ASM_CT = re.compile(r'^[01;]*$')
BIN = re.compile(r'^[01]*$')

PRINTLINE = re.compile(r'("[^"]*"|CHR\$\s*\d+)')
SPLIT_SENTENCES = re.compile(r'\s*(REM.*|[^:]+(?:(?:[^:]*"[^"]*"[^:]*)+)|[^:]+)\s*')  # colon delimited sentences on one line

# Context constants:
CONTROL = 0
OUTPUT = 1
TEXT = 3
GRAPH = 5


def parse_clear(line):
    n = int(line[6:])
    return clear(n)


def chr_(command):
    """CHR$ n"""
    return chr(int(re.search(r'\d+', command)[0]))


def clear(n):
    return ';' * n


def parse_data(line):
    re_data = re.compile(r'"[^"]*"|CHR\$\s*\d+|\d+')
    r = data(re_data.findall(line))
    return r


def bits(n, pad=0):
    return bin(n)[2:].zfill(pad)


def data(lst):
    output = ''
    for item in lst:
        if isinstance(item, int):
            output += bits(item)
        elif item.startswith('CHR$'):
            output += bits(ord(chr_(item)), 8)
        elif item.startswith('"'):
            output += ''.join([bits(ord(c), 8) for c in item.strip('"')])
        elif re.match(r'\d+', item):
            output += bits(int(item))
        elif len(item) == 1:
            output += bits(ord(item), 8)
    return output


def parse_print(line):
    s = ''
    line = line.replace('+', '')  # TODO: Temporary!
    for v in PRINTLINE.split(line[6:]):
        v = v.strip()
        if not v:
            continue
        if v.startswith('CHR$'):
            s += chr_(v)
        else:
            s += v.strip('"')
    return print_(s)


def print_(s):
    r = ''
    for c in s:
        r += '1' + bits(ord(c), 8) + '0'
    return r


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


class CTCompiler:
    def __init__(self, lines):
        self.source = []
        self.preprocess(lines)
        self.ct = None
        self.context = [CONTROL]

    def preprocess(self, lines):
        """Perform line and sentence based pre-processing."""
        for line in lines:
            sentences = SPLIT_SENTENCES.findall(line)
            self.source += sentences

    def context_transition(self):
        """ Transition to CONTROL context.
            Returns True if a transition was made.
        """
        if self.context[-1] != CONTROL:
            self.context.pop()
            self.context[-1] = CONTROL
            return True
        else:
            return False

    def compile(self, target='CT'):
        if not self.ct:
            self.compile_()
        if target == 'CT':
            return self.ct
        if target == 'BCT':
            return bct(self.ct)
        if target == 'ABCT':
            return abct(self.ct)
        if target == '110':
            return rule110(self.ct, data='1')

    def compile_(self):
        ct = ''
        gfx_block = None
        for line in self.source:
            line = line.strip()
            append = ''
            if line.startswith('REM') or not line:
                continue
            if graphics.match(line):
                if self.context[-1] == CONTROL:
                    self.context += [OUTPUT, GRAPH]
                    gfx_block = Graphics()
                    #append += print_(STX + graphics.GS)
                elif self.context[-1] == TEXT:
                    self.context[-1] = GRAPH
                    gfx_block = Graphics()
                gfx_block.append(line)
            elif gfx_block:  # Graphics block completed; append it to output
                self.context.pop()
                append += print_(STX + gfx_block.end() + ETX)
                gfx_block = None
            if line.startswith('INPUT'):
                pass
            elif line.startswith('DATA'):
                append = parse_data(line)
            elif line.startswith('BIN'):
                if self.context_transition():
                    append += print_(ETX)  # TODO: why isn't this occurring every OUTPUT to CONTROL transition?
                append += parse_bin(line)
            elif line.startswith('CLEAR'):
                self.context_transition()
                append += parse_clear(line)
            elif line.startswith('PRINT'):
                if self.context[-1] == CONTROL:
                    append += print_(STX) + parse_print(line) + print_(ETX)
                elif context[-1] == GRAPH:
                    self.context[-1] = TEXT
                    append += print_(graphics.US) + parse_print(line)
            elif line.startswith('ASM'):
                append = parse_asm(line)
            elif line.startswith('FILL'):
                append = parse_fill(line, 1)
            elif line.startswith('ZFILL'):
                append = parse_fill(line, 0)
            elif line.startswith('CLS'):
                append += print_(STX + graphics.CLS + ETX)
            elif line.startswith('ENDIF'):
                pass
            elif line.startswith('END'):
                self.context_transition()
                append += clear(10)
            ct += str(append)
        self.ct = ct


# Binary to bijective base-2 (taken from abct output.py)
bin_to_bb2 = lambda s: sum([int(c) * 2 ** i for i,c in enumerate(s.replace(' ', '').replace('1', '2').replace('0', '1'))])


def bct(ct):
    return ''.join([f'1{c}' if c != ';' else '0' for c in ct])


def abct(ct):
    b = bct(ct)
    return bin_to_bb2(b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=ABOUT, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('source', help='CTBASIC source file to process', type=argparse.FileType('r'))
    parser.add_argument('--target', '-t', help='Compile target: CT, BCT, ABCT, 110', default='CT')
    parser.add_argument('--debug', '-d', help='Turn on debug output', action='store_true')
    args = parser.parse_args()

    c = CTCompiler(args.source.readlines())
    output = c.compile(args.target)
    print(output)
