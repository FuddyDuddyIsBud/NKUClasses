#!/usr/bin/python3
import getpass as gp
from ftplib import FTP
import os
import http.client

def connect(): # connects to the device with the information
    host = '10.2.56.119' #this may haev to be changed to your machine
    usr = 'ftpuser' #hard coded username, may need to change
    passwd = gp.getpass("Please enter the password for the ftpuser account: ")
    con = ""
    try:
        con = FTP(host,usr,passwd) #connects using the variables
    except :
        print("Connection to ", host, " has failed")
    return con

def upload():
    con = connect()
    con.cwd('cit383')
    file = input("Enter the file to upload to the ftp server: ")
    if os.path.exists(file):
        fh = open(file, 'rb') #opens the file and allows it to read it
        sendFile = "STOR "+str(file) #made just incase it causes an error
        con.storbinary(sendFile, file)
        fh.close()
        con.close()

ftp = FTP('10.2.56.120') #the ip of the device, it is currently hard coded
def download():
    ftp.login('ftpuser','student')
    ftp.cwd('cit383')
    exten = input("Please enter the file extension you wish to download: ")
    files = ftp.nlst() #gets all the files in the working dir
    for file in files:
        ext = os.path.splitext(file)[-1].lower() #gets the extemsion of the file
        if not os.path.isdir(file):
            if exten == ext:
                print("Downloading " + file)
                ftp.retrbinary("RETR %s" % file, open(file, 'wb').write)
    ftp.close()

def toHTTP(url): #THis is for getting the HTTP stuff
    connect = http.client.HTTPConnection(url) #takes the URL and connects to it
    connect.request("GET", "/") #stores the information
    response = connect.getresponse()
    print("Status Code: {}".format(response.status))
    print("Version: {}".format(response.version))
    print("Length in KB {}".format(response.length))
    print(response.headers['Last-Modified'])
    print('*'*40)

def menu():
    print("1 is for uploading a file")
    print("2 is for Downloading a file")
    print("3 is for showing webpage stats")
    print("*"*40)
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("Please choose one of the options from the list: "))
    if choice == 1: #this is for uploading
        upload()
    if choice == 2: #this calls downloadd
        download()
    if choice == 3: #this checks for http
        url = input("Please enter a URL: ") #we are currently not checking if it exists, and we do not execpt ips
        toHTTP(url)

if __name__ == '__main__':
    menu()