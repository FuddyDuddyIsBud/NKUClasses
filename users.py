import subprocess as sp
import os

choice=input("please input choice;add, remove, print: ")

if choice==add:
    def add_user(user):
        sp.call(['useradd', user])

if choice==remove:
    def remove_user(user):
        sp.call(['deluser', user])

if choice==print:
    def print_user(user):
        123

add_user(user)
remove_user(user)
print_user(user)
