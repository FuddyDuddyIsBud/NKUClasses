#!/usr/bin/python3
#important imports
import getpass
import subprocess as sp
import crypt
#menu from previous labs just modified
def menu():
    useroption = 0
    print('Menu')
    print('1: Create User: ')
    print('2: Delete User: ')
    print('3: Modify User: ')
    print('4: Exit: ')
    while (useroption < 1 or useroption > 4):
        useroption = int(input('Choose option 1 through 4: '))
    if (str(useroption) == "1"):
        CreateUser()
    if (str(useroption) == "2"):
        DeleteUser()
    if (str(useroption) == "3"):
        modifyuser()
    if (str(useroption) == "4"):
        exit(1)
#checks if user exists
def CheckUser(user):
    UserList = []
    with open('/etc/passwd', 'r') as pf:
        records = pf.readlines()
    for y in records:
        urecord = y.split(':')
        UserList.append(urecord[0])
    if user in UserList:
        return True
    else:
        return False
#deletes specific user
def DeleteUser():
    username = input("Enter username you wish to delete: ")
    while not (CheckUser(username)):
        username=input("user wasn't in the system, try again: ")
        print(CheckUser(username))
#deletes the user
    try:
        sp.run(['userdel','-r',username])
    except:
        print('sorry unable to delete user account')
#creates the user account
def CreateUser():
#sets the username and first name
    username = ('root')
    fullname = input("Enter full name: ")
    username = input("Enter username: ")
    print(CheckUser(username))
#checks to see if user is already in system, if they are, reask
    while CheckUser(username):
        username = input('User already exists, input new username: ')
    passwd = getpass.getpass(prompt='Please enter a password')
    passwd = crypt.crypt(passwd)
#runs the command to add the user
    try:
        sp.run(['useradd', '-p', passwd, username])
        sp.run(['usermod', '-c', fullname, username])
        print("User added ")
    except:
        print('sorry it didnt work')
#modify user account, either locking them or adding a real name.
def modifyuser():
    modify = input("Do you wish to add a real name to the account(1), or lock the account(2). ")
#if 1, it adds a real name if the user exists.
    if (str(modify) == "1"):
        account = input("enter username")
        while not (CheckUser(account)):
            account = input("input a username in the system: ")
        try:
            name = input("type in real name: ")
            sp.run(['usermod', '-c', name, account])
        except:
            print("Sorry, unable to modify", account)
#if 2, it locks the account if the user exists
    if (str(modify) == "2"):
        account = input("Enter username to lock.")
        while not (CheckUser(account)):
            account = input("input a username in the system: ")
        try:
            sp.run(['usermod', '-L', account])
        except:
            print("Sorry, unable to lock account.")
#runs the menu system
active = True  # this will activate the menu
while (active == True):
    menu()