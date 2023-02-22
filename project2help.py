
import subprocess as sp
import os
from datetime import datetime, timedelta
import smtplib,mimetypes,getpass
from email.message import EmailMessage
import shutil
import paramiko
from datetime import datetime,timedelta
import smtplib,mimetypes,getpass
import shutil

def modweeks():
    pass

def emails():
    message=EmailMessage()
    sender=input("enter SENDERs email address: ")
    passwd=getpass.getpass("enter email password: ")
    recip=input("enter the RECIPIENTS email address: ")
    subjectline=input("enter subject: ")
    compromised=input("enter compromised username")
    mail_server=smtplib.SMTO_SSL("smtp.gmail.com")
    mail_server.login(sender, passwd)

    #message headers
    message["From"] = sender
    message["To"] = recip
    message["Subject"] = subjectline
    body="""Hello,
    here are the set of compromised files in their dir along with the user: """ + '\nuser of comp files: ' + compromised + "\n" + str(modweeks())

    message.set_content(body)
    flag = input("do you have a file to attach Y or N: ")
    if(flag.upper()=="Y"):
        filename=input("enter filename: ")
        mime_type, _ = mimetypes.guess_type("filename")
        mime_type=mimetypes.MimeTypes().guess_type(filename)[0]
        print(mime_type)
        mime_type, mime_subtype -mime_type.split("/")
        with open(filename. "rb") as file:
            message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype filename=filename)
            mail_server.send_message(message)
            mail_server.quit()
    else:
        mail_server.send_message
        mail_server.quit()
