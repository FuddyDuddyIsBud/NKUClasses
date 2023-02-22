#!/usr/bin/python3
import argparse as ap
import os
import logging
import sys
#Argparse command
pobj = ap.ArgumentParser()
pobj.add_argument('-H', dest='H', type=str, help='USAGE:<script name> [options] [directory] Once displayed, then exit application')
pobj.add_argument('-d', action='store', dest='D', type=str, required=True, help='Use full path')
pobj.add_argument('-l', action='store_true', dest='L', help='creates a logfile in specified directory.')
pobj.add_argument('-c', action='store', dest='C', type=int, help='input number of directories to create.')
#results of those options simplified
result = pobj.parse_args()
h = result.H
d = result.D
l = result.L
c = result.C
#Prints help
if h:
    print("USAGE:<script name> [options] [directory] Once displayed, then exit application")
#used to get and check path to directory
if d:
    try:
        os.path.isdir(d)
    except:
        print("Sorry, not a directory.")
#creates directories, with error checking
if c:
    for x in range(1, c + 1):
        try:
            extra = "dir_" + str(x)
            directory = d + "/dir_" + str(x)
            os.makedirs(directory)
        except:
            pass
else:
    print("Input a valid option.")
#creates logfile, amd appends it
if l:
    name = input("What do you wish to call the Log file?: ")
    r = open(name, 'w+')
    info = []
    for log in os.listdir(d):
        try:
            info.append(log)
        except:
            pass
#writes and closes
    for n in info:
        print(n)
        r.write(n + ' ')
    r.close()