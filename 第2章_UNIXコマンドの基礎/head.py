# coding: utf-8

import sys
import argparse

def head():
    prog = 'head [-n count] [file ...]'
    description = 'head -- display first lines of a file'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-n', default=10, type=int)
    parser.add_argument('infile', nargs='?', type=argparse.FileType())
    options = parser.parse_args()
    
    count = options.n
    infile = options.infile or sys.stdin
    outfile = sys.stdout

    with infile, outfile:
        for line_no, line in enumerate(infile, 0):
            if line_no == count:
                return
            outfile.write(line)

if __name__ == '__main__':
    head()