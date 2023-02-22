#!/usr/bin/python3
#import important
import os
import subprocess
#dictionary everything is stored in
storage={}
#creates and changes the directory while also printing it to the console
home=os.path.expanduser("~")
path=os.getcwd()
print(path)
dir=home + "/Lab3"
if os.path.exists(dir):
    pass
else:
    os.makedirs(dir)
#changes the directory and prints it to console
os.chdir(dir)
path=os.getcwd()
print(path)
#variables needed later
num_files=-1
sub_dir=-1
#creates files based on user input
def create_files(dir, num, storage, num_files):
    while num_files<0:
        num_files=int(input("enter the number of files: "))
        for m in range(num_files):
            type="file_"+str(m + 1)+".docx"
            file=dir+"/file_"+str(m + 1)+".xls"
            open(file, 'w+')
            os.chmod(file, 740)
            storage[type]=(get_inode_type(file))
#creates directories based on user input
def create_sub_directories(dir, num, storage):
    num_dir=-1
    while num_dir<=0:
        num_dir=int(input("Enter the number of directories: "))
        for n in range(num_dir):
            type="dir_"+str(n + 1)
            directory=dir+"/dir_" + str(n + 1)
            os.makedirs(directory)
            storage[type]=get_inode_type(dir + '/')
#sets up the method for renaming files
def rename_files(dir, curext, newext):
    for i in os.listdir(dir):
        file, ext=os.path.splitext(i)
        if ext==curext:
            newfile=file+newext
            os.rename((dir+"/"+i), (newfile))
#Checks whether it's a file or directory
def get_inode_type(name):
    if os.path.isdir(name):
        return "Directory"
    if os.path.isfile(name):
        return "File"
#sets up the display and gets the directory
def list_entries(storage):
    print("%-15s %-15s" % ("Name", "Type"))
    print("%-15s %-15s" % ("-------", "-------"))
    for x, y in storage.items():
        print("%-15s %-15s" % (x, y))
#second part to create_files
create_files(path, num_files, storage, num_files)
#second part to create directories
create_sub_directories(path, sub_dir, storage)
#second part to rename_files
rename_files(dir, ".xls", ".docx")
#second part to list entries
list_entries(storage)