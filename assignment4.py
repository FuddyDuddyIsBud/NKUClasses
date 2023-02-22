#!/usr/bin/env python3.6
#task1
import os

os.system("printenv")

#task2

FILE_NAME=input("file name: ")
FILE_POINTER=input("file pointer: ")
def set_env(FILE_NAME, File_POINTER):
    os.system("export PATH=/home")
    pwd=os.system("pwd")
    change=os.system('')

set_env(FILE_NAME, FILE_POINTER)

print(os.getenv("FILE_NAME"))
print(os.getenv("FILE_POINTER"))

#task3
def set_env():
    pwd=os.system("pwd")
    change=os.system('')

set_env()

print(os.getenv("FILE_NAME"))
print(os.getenv("FILE_POINTER"))
user_input=input("What to write in file: ")

def  write_show_file(FILE_NAME, FILE_POINTER, user_input):
    f=open(FILE_NAME, "a")
    f.write(input)
    f=open(FILE_NAME, "r")
    f.seek(user_input)

write_show_file(FILE_NAME, FILE_POINTER, user_input)