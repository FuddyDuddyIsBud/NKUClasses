#!/usr/bin/python3
import paramiko
import os
from os import path
#ip for VM2 - 10.2.56.120
host = "10.2.56.119"
port = 22
user = "sshuser"
passwd = "student"

def connect(usr,passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host,port,usr,passwd)
    return ssh_client

def mkfile(usr,passwd): #makes 4 files
    ssh_client = connect(usr,passwd)
    ssh_client.exec_command("touch file1.txt file2.txt file3.dat file4.dat")
    ssh_client.close()

def cpfile(usr,passwd):
    ssh_client = connect(usr, passwd)
    ssh_client.exec_command("cp * ssh_dir")
    ssh_client.close()

def rmForExt(usr,passwd,exten):
    ssh_client = connect(usr, passwd)
    rmCommand = "cd ssh_dir;rm *." + str(exten)
    ssh_client.exec_command(rmCommand)
    ssh_client.close()

def dnsServer(usr,passwd):
    results = []
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command(
        "cat /etc/resolv.conf")
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())

def top5Jobs(usr,passwd):
    results=[]
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command("ps --sort=-pcpu | head -n 6")
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())

def netConTest(usr,passwd,addr):
    results = []
    ssh_client = connect(usr, passwd)
    command = "ping -c 5 " + str(addr)
    stdin, stdout, sterr = ssh_client.exec_command(command)
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())

def usersLoggedIn(usr,passwd):
    results = []
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command("users")
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())

def menu():
    print("Welcome to Lab 10")
    print("*"*50)
    print("1 is for create files on user pc")
    print("2 is for copy all files to ssh_dir")
    print("3 is for delete all files with a given extension")
    print("4 is for display the DNS sever of my second VM")
    print("5 is for display the top 5 jobs (CPU usage)")
    print("6 is for nextwork connectivity test")
    print("7 is for display all current logged in users")
    print("*"*50)
    choice = 0
    if choice < 1 or choice > 7:
        choice = int(input("Please enter your choice: "))
    if choice == 1:
        mkfile(user,passwd)
    if choice == 2:
        cpfile(user,passwd)
    if choice == 3:
        fileExe = input("Please enter a file extension you wish to remove: ")
        rmForExt(user,passwd,fileExe)
    if choice == 4:
        dnsServer(user,passwd)
    if choice == 5:
        top5Jobs(user,passwd)
    if choice == 6:
        addr = input("Please enter a URL or a IP Address: ")
        netConTest(user,passwd,addr)
    if choice == 7:
        usersLoggedIn(user,passwd)

menu() #calls the menu, and runs the whole puppy