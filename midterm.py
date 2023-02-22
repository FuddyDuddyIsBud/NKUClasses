import os
import subprocess as sp

#task1

list=[]

enviro=input()

os.environ['inputfile.txt']=enviro

enviro=os.getenv('inputfile.txt')


#task2



#task3

def add_user(user):
    sp.call(['useradd',user])
    
def remove_user(user):
    123
    
def print_user(user):
    123
