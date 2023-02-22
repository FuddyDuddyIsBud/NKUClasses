#!/usr/bin/python3
import getpass, smtplib, mimetypes, os, crypt
import argparse as ap
from email.message import EmailMessage
import paramiko
import getpass
from ftplib import FTP
import os
#argument parse with all the little checks for terminal
pobj=ap.ArgumentParse()
pobj.add_argument('-i', action="store", dest='I', type=str, required=True, help='Get the IP address')
pobj.add_argument('-d', action="store", dest='D', type=str, help='Get the directory')
pobj.add_argument('-e', action="store", dest='E', type=str, required=True, help='Email username')
pobj.add_argument('-g', action="store", dest='G', type=str, help='Download the file')
#the results shortened
result=pobj.parse_args()
i=result.I
d=result.D
e=result.E
g=result.G
#gets the IP, username and whatnot and establishes the connection
if i:
    IP=input("Input IP address: ")
    port=22
    uname=input("input username: ")
    passwd=getpass.getpass("input password")
    con=FTP(IP, uname, passwd)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(IP,port,uname,passwd)
#does th
if d:
    stdin, stdout, sterr = ssh_client.exec_command("find /home/ -mtime -14")
    for line in stdout:
        results.append(line.strip('\n'))
    for i in results:
        print(i.strip())
#sends out the email and asks for the attachment
if e:
    message=EmailMessage()
    sender=input("enter SENDERs email address: ")
    passwd=getpass.getpass("enter email password: ")
    recip=input("enter the RECIPIENTS email address: ")
    subjectline=input("enter subject: ")
    compromised=input("enter compromised username")
    mail_server=smtplib.SMTO_SSL("smtp.gmail.com")
    mail_server.login(sender, passwd)
    message["From"] = sender
    message["To"] = recip
    message["Subject"] = subjectline
    body="Hello, here are the set of compromised files in their dir along with the user: " + '\n user of comp files: ' + compromised + "\n" + str(results)

    message.set_content(body)
    flag = input("do you have a file to attach Y or N: ")
    if(flag.upper()=="Y"):
        filename=input("enter filename: ")
        mime_type, _ = mimetypes.guess_type("filename")
        mime_type=mimetypes.MimeTypes().guess_type(filename)[0]
        print(mime_type)
        mime_type, mime_subtype -mime_type.split("/")
        with open(filename, "rb") as file:
            message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=filename)
            mail_server.send_message(message)
            mail_server.quit()
    else:
        mail_server.send_message
        mail_server.quit()
#does the if else for putting the results from d, and downloading them
if g:
    folder=input("folder location: ")
    if (os.path.exists(folder)):
        for files in results:
            ftp_client = ssh_client.open_sftp()
            ftp_client.get(files, folder)
            ftp_client.close()

    else:
        folder=os.getcwd()
        for files in results:
            ftp_client = ssh_client.open_sftp()
            ftp_client.get(files, folder)
            ftp_client.close()