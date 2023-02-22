#!/usr/bin/python3
#imports modules
import csv
import time
import random
import subprocess as sp
#opens the file and reads it, creates an array for the data
with open("employee-1.csv", 'r') as InputFile:
    data = csv.reader(InputFile)
    heading = next(data)
    array = list(data)
#adds the groups from the csv to the computer
def groups():
    for users in array:
        sp.run(['groupadd', users[2]])
        print(users[2])
#opens the passwd file with read, and checks to see if the user exists, and creates a list based off those users
def usercheck(user):
    allusers = []
    with open('/etc/passwd', 'r') as r:
        passwduser=r.readlines()
#splits the data entry at :
    for i in passwduser:
        npasswduser=i.split(':')
        allusers.append(npasswduser[0])
    if user in allusers:
        return True
    else:
        return False
#creates the username based off of csv data
def createusername(users):
    random=random.randint(1, 10)
    newuser=(users[1]).lower() + (users[0][0]).lower() + users[0][-1].lower() + str(random)
    return newuser
#creates the new user based off of the username
def createuser():
    allusers=[]
    for users in array:
        group=users[2]
        list=users
        firstxlast=(users[0] + ' ' + users[1])
        username='root'
        x=0
        while (usercheck(username)):
            username=createusername(list)
            x=x+1
            if x==10:
                print('They already exists')
                exit
        sp.run(['useradd', username])
        sp.run(['usermod', '-c', firstxlast, username])
        sp.run(['usermod', '-g', group, username])
        newlist=[]
        newlist.append(users[0])
        newlist.append(users[1])
        newlist.append(username)
        allusers.append(newlist)
    write(allusers)
#writes the data to newusernames
def write(allusers):
    heading = ['First name', 'Lastname', 'username']
    file = open('newusernames.csv', 'w+', newline = '')
    with file:
        pen = csv.writer(file)
        pen.writerow(heading)
        pen.writerows(allusers)
groups()
createuser()

