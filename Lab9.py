#!/usr/bin/python3
import getpass
from ftplib import FTP
import os
import http.client
import re

#menu system
def menu():
    choice = 0
    print('Menu')
    print('1: Send a file:  ')
    print('2: Recieve a file: ')
    print('3: Check website status: ')
    print('4: Exit Script: ')
    while (choice < 1 or choice > 4):
        choice = int(input('Please select an option [1 - 4]: '))
    if str(choice) == "1":
        send()
    if str(choice) == "2":
        recieve()
    if str(choice) == "3":
        ohttp()
    if str(choice) == "4":
        print("bye.")
        exit(1)
#connects to 10.2.56.119
def connection():
    host='10.2.56.119'
    user='ftpuser'
    passw=getpass.getpass('Please enter you password: ')
    try:
        con=FTP(host, user, passw)
    except:
        print("Sorry, wrong username, password, or host")
    return con
#sends the file
def send():
    con = connection()
    con.cwd('cit383')
    upload=input('Name of file')
    if os.path.exists(upload):
        handler = open(upload, 'rb')
        con.storbinary('STOR: ' + str(upload), handler)
        handler.close()
        con.close()
    else:
        print("failed.")
        con.close()

ftp=FTP("10.2.56.119")
def recieve():
    ftp.login('ftpuser','student')
    con=connection()
    con.cwd('/home/student/')
    check="^(.[a-zA-Z]*[0-9]*)"
    fileType=input("enter extension: ")
    searchFile=check + '(.' + fileType + ')$'
    for files in con.nlst():
        if re.search(searchFile, files):
            try:
                Blah = open(files, 'wb')
                con.retrbinary('RETR' + str(files), Blah, 1024)
                Blah.close()
                print(files + "Downloaded")
            except:
                print("Download failed")

        else:
            print(files + 'Is not a .' + Blah + 'and was not able to be downloaded.')
            con.close()

def ohttp():
    uWeb = input('please enter the website with extension (.com, .edu, etc): ')
    uWeb = 'www.' + uWeb
    print('----------URL INFO----------')
    connection_obj = http.client.HTTPSConnection(uWeb)
    connection_obj.request('GET', '/')
    resp = connection_obj.getresponse()
    print('status code: ', resp.status)
    print('Version: ', resp.version)
    print('Length: ', str(resp.length / 1048576) + " Mb")
    print('Last modified', resp.headers['Last-Modified'])
    connection_obj.close()

active=True
while (active==True):
    menu()