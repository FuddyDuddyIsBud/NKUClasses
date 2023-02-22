#!/usr/bin/python3
#Imports needed
import os
import shutil
import subprocess as sp
import zipfile
from datetime import datetime
#creates backup method
def createBackup():
    #sets the original and backup location
    original = input("Enter the directory name you want to backup: ")
    backup = input("Enter backup location: ")
#checks to see if the path already exists to backup, if it doesn't reask
    if (os.path.exists(original)):
        if (os.path.isdir(original)):
            sp.call(['rsync', '-a', original, backup])
    else:
        print("That directory doesn't exist, please enter one that does: ")
#create archive method
def createArchive():
    #takes name of arhive
    dirarchive=input("Enter directory you want to archive? ")
    if (os.path.exists(dirarchive)):
        #sets to zero for while statement
        x = 0
    else:
        dirarchive=input("enter directory you want to archive? ")
    archivetype=input("Enter the type of archive to be created (zip,gztar,tar,bztar,xztar): ")
    if (archivetype=="zip"):
        x=0
    elif (archivetype=="gztar"):
        x=0
    elif (archivetype=="tar"):
        x=0
    elif (archivetype=="bztar"):
        x=0
    elif (archivetype=="xztar"):
        x=0
    else:
        archivetype=input("Enter the type of archive to be created (zip,gztar,tar,bztar,xztar): ")
    shutil.make_archive(dirarchive, archivetype, root_dir='../..', base_dir=str(dirarchive))
def osZipSize():
    #gets the file location and size, with that sees if it's windwos or linux or unknown, and prints the info about it
    file=input("Enter the location to the file: ")
    kilobyenumber=input("what is the size In kilobytes: ")
    with zipfile.ZipFile(file) as zf:
        for info in zf.infolist():
            print(info.filename)
            if info.create_system==0:
                system="Windows"
            elif info.create_system==3:
                system="Unix"
            else:
                system="UNKNOWN"
            print("System       : ", system)
            print("Size (kb)    : ", int(info.file_size) / (int(kilobyenumber) * 1024))
#finds the last modified files within a specific directory
def lastMod():
    path=input("Choose a directory: ")
    dirlist=[]
    currentTime=datetime.now()
    if (os.path.exists(path)):
        os.chdir(path)
        for file in os.listdir(path):
            try:
                mtime=os.path.getmtime(file)
                mtime=datetime.fromtimestamp(mtime)
                timeModified=currentTime - mtime
                print(timeModified)
                if timeModified.days<=30:
                    dirlist.append(file)
            except:
                pass
    else:
        path = os.getcwd()
        for file in os.listdir(path):
            try:
                mtime = os.path.getmtime(file)
                mtime = datetime.fromtimestamp(mtime)
                timeModified = currentTime - mtime
                print(timeModified)
                if timeModified.days < 30:
                    dirlist.append(file)
            except:
                pass
    print("The last modified files are: ")
    for i in dirlist:
        print(i)
#menu system, sets it to true to run and then allows the user to input a number and it is ran across the options.
menubar=True
while (menubar==True):
    print("1: Backup directory")
    print("2: Archive directory")
    print("3: Examine zip file")
    print("4: View last modified")
    choice = input("Please select number for action or type in exit, to quit.")

    if (choice=="1"):
        createBackup()
    elif (choice=="2"):
        createArchive()
    elif (choice=="3"):
        osZipSize()
    elif (choice=="4"):
        lastMod()
    elif (choice=="exit"):
        menubar = False
    else:
        print("Not valid, restart program and try again.")
