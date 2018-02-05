# coding: utf-8

import sys
import argparse

def tail():
    prog = 'tail [-n count] [file ...]'
    description = 'tail -- display the last part of a file'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-n', default=10, type=int)
    parser.add_argument('infile', nargs='?', type=argparse.FileType())
    options = parser.parse_args()
    
    count = options.n
    infile = options.infile or sys.stdin
    outfile = sys.stdout

    with infile, outfile:
        # TODO(Gimo): if file is large, should be rewritten.
        for line in infile.readlines()[-count:]:
            outfile.write(line)

if __name__ == '__main__':
    tail()