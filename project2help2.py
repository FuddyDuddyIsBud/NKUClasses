#!/usr/bin/python3
# import subprocess as sp
# import os
# from datetime import datetime,timedelta
# import smtplib,mimetypes,getpass
# from email.message import EmailMessage
# import shutil
# #import paramiko
# def modweeks():
pass


def emails():
    message = EmailMessage()


sender = input("Please enter the SENDERS email address: ")
passwd = getpass.getpass("Please enter the email pass with the SENDERS account: ")
recip = input("Please enter the RECIPENTS email address: ")
subjectline = input("Please enter subject of email: ")
comproind = input("Please enter compro users name: ")
mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
mail_server.login(sender, passwd)

# message headers message['From'] = sender
message['To'] = recip
message['Subject'] = subjectline
body = """Hello, Here are the set of compromised files in their dir along with the user: """ + '\nUser of comp files:' + comproind + "\n" + str(
    modweeks())

message.set_content(body)
flag = input("Do you have a file to attach Y or N: ")
if (flag.upper() == "Y"):
    filename = input("Please enter filename: ")
    mime_type, _ = mimetypes.guess_type('filename')
    mime_type = mimetypes.MimeTypes().guess_type(filename)[0]
    print(mime_type)
    mime_type, mime_subtype = mime_type.split("/")
    with open(filename, "rb") as file:
        message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=filename)
        mail_server.send_message(message)
        mail_server.quit()
else:
    mail_server.send_message(message)
    mail_server.quit()