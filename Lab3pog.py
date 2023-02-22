#!/usr/bin/python
import os

def get_inode_type (name):
    if os.path.isdir(name):
        return "Directory"
    if os.path.isfile(name):
        return "File"

def list_entries (dir):
    files = os.listdir(dir)
    print("%-15s %-20s" % ("Name", "Type"))
    print("%-15s %-20s" % ("-------", "-------"))
    for i in files:
        print("%-15s %-20s" % (i, get_inode_type(dir + "/" + i)))

def create_files (dir, num):
    i = 1
    while num >= i:
        file = dir + "/test" + str(i) + ".txt"
        os.mknod(file)
        i += 1

def create_sub_directories (dir, num):
    i = 1
    while num >= i:
        directory = dir + "/subdir" + str(i)
        os.makedirs(directory)
        i += 1

def rename_files (dir, curext, newext):
    for i in os.listdir(dir):
        file, ext = os.path.splitext(i)
        if ext == curext:
            newfile = file + newext
            os.rename((dir + "/" + i), (dir + "/" + newfile))





home = os.path.expanduser("~")
path = os.getcwd()

#1. print to the console the current directory
print(path)

#2. create a directory called Lab3 in home directory
newdir = home + "/Lab3"
if os.path.exists(newdir):
    pass
else:
    os.makedirs(newdir)

#3. change directory to Lab3
os.chdir(newdir)

#4. print to the console the current directory
path = os.getcwd()
print(path)

#5. create 10 files named test#.txt
create_files(path, 10)

#6. create 5 sub-directories named subdir#
create_sub_directories(path, 5)

#7. list everything in the Lab3 sub directory
list_entries(path)

#8. rename all files that end with .txt to .dat
rename_files(newdir, ".txt", ".dat")

#9. list everything in the Lab3 sub directory
list_entries(path)