#task1
# !/usr/bin/env python3.6
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('filename',help="blah")
parser.add_argument('--lines','-l',type=int, nargs=1 ,help="blah")

argv=parser.parse_args()

if argv.lines:
    f=open(argv.filename,'r')
    ln=f.readlines()
    print(ln)

#task2
# !/usr/bin/env python3.6
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('filename',help="blah")
parser.add_argument('--lines','-l',type=int, nargs=1, help="blah")

argv=parser.parse_args()

if argv.lines:
    f=open(argv.filename,'r')
    ln=f.readlines()
    print(ln)

#task3
# !/usr/bin/env python3.6

import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('filename',help="blah")
parser.add_argument('--lines','-l',type=int, nargs=1, help="blah")
parser.add_argument('--reverse', '-r', request=False, nargs=2, help='reverse')
args=parser.parse_args()

if args.reverse:
    print(sys.argv[-1:])

if argv.lines:
    f=open(argv.filename,'r')
    ln=f.readlines()
    print(ln)

#task4
# !/usr/bin/env python3.6

import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('filename',help="blah")
parser.add_argument('--lines','-l',type=int, nargs=1, help="blah")
parser.add_argument('--reverse', '-r', request=False, nargs=2, help='reverse')
parser.add_argument('--copy', '-c', request=False, nargs=2, help='reverse')
argv=parser.parse_args()

if argv.reverse:
    print(sys.argv[-1:])

if argv.lines:
    f=open(argv.filename,'r')
    ln=f.readlines()
    print(ln)
if argv.copy:
    filename=input("Enter file name: ")
    number=input("Enter a number: ")