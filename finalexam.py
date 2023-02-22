#!/usr/bin/python3

import sys
import crypt
import subprocess as sp
import os
import argparse as ap

parser=ap.ArgumentParser()
parser.add_argument(action="store", defaults=".", dest="dir_path", help="please enter user to be added")
args=parser.parse_args()
dir_path=args.dir_path

def checkuser(uname, group):
    passwd=open("/etc/passwd", "r")
    for line in sorted(passwd.readlines()):
        a=line.split(":")

        if uname == a[0]:
            return True
    return False

def groupthing():
    passwd=open("/etc/passwd", "r")
    for line in sorted(passwd.readlines()):
        a=line.split(":")
        list=[]
        for list in groupthing:
            list.append[a[3]]
            list.append[a[5]]
            list.append[a[2]]
        return list

def newuser():
    notunique=True
    while notunique == True:
        userfirstlast=input("Enter first and last name with a space between them")
        uname=input("enter username")
        password=input("enter password")
        group=input("enter group")
        passenc=crypt.crypt(password)
        if "cat / etc / group | grep ', +group, ' 1 > / dev / null":
            print("group doesn't exist")
        else:
            notunique=checkuser(uname)
            if notunique == True:
                print("user exists")
            if notunique == False:
                try:
                    sp.run(["useradd","-p", passenc, "-c", userfirstlast, uname])
                    sp.run(["sudo usermod", "-a", "-G", group, uname])
                    print("user has been added")
                except:
                    print("not able to be added")


    print('User ID       Full Name          Group ID')
    print('==========================================')
    for list in groupthing:
        print(list)