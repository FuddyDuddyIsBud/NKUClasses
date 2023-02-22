#!/usr/bin/python3
#imports needed
import re
import csv
#menu for the user to select options
def menu():
    choice=0
    print('Menu')
    print('1: compromised devices:  ')
    print('2: password: ')
    print('3: email: ')
    print('4: Exit Script: ')
#updated selection method
    while (choice < 1 or choice > 4):
        choice = int(input('Please select an option [1 - 4]: '))
    if str(choice)=="1":
        compromised()
    if str(choice)=="2":
        password()
    if str(choice)=="3":
        email()
    if str(choice)=="4":
        exit()
#opens the file and reads it
with open("empdata-2.csv", 'r') as InputFile:
    data = csv.reader(InputFile)
    heading = next(data)
    user = list(data)
#uses regex to check compromised machines
def compromised():
    compromised = []
    for users in user:
        ip = users[3]
#regex checks then appends list
        check = ('250\.30\.8\.[0-255]')
        if re.search(check, users[3]):
            compromised.append(users)
#opens the file to write
    with open('compromised.csv', 'w', newline='') as file:
        pen = csv.writer(file)
        pen.writerow(['First name', 'Last Name', 'Department', 'Email Address'])
#makes each line fo required information
        for list in compromised:
            info = []
            info.append(list[0])
            info.append(list[1])
            info.append(list[4])
            info.append(list[2])
            pen.writerow(info)
#checks passwords
def password():
    print('Users with bad passwords: ')
    for users in user:
        check = 0
        if len(users[6]) < 8 or len(users[6]) > 12:
            check=check + 1
        if not re.search("\W", users[6]):
            check=check + 1
        if not re.search("[A-Z]", users[6]):
            check=check + 1
        if not re.search("[a-z]", users[6]):
            check=check + 1
        if not re.search("[\d]+", users[6]):
            check=check + 1
#if they don't math, it prints them
        if check > 0:
            print(users[0], users[1], users[6])
#checks the emails using regex, if they are bad add them to the list emails
def email():
    emails = []
    for users in user:
        check = '[a-zA-Z0-9]{10,100}@[a-zA-Z]+\.(ru|jp)'
        emails = users[2]
        if re.search(check, emails):
            emails.append(users)
    print('These are the bad emails: ')
#prints users in bad list
    for users in emails:
        print(users[0], users[1], users[2])
    print(' ')
#menu
active = True
while (active == True):
    menu()