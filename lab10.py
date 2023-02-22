#!/usr/bin/python3
import paramiko, getpass

host="10.2.56.119"
port=22
usr="sshuser"
passwd="student"
# this is the menu system
def menu():
    choice = 0
    print('Menu')
    print('1: create files:  ')
    print('2: copy from home to sshuser: ')
    print('3: dns check: ')
    print('4: cpu usage: ')
    print('5: ping website: ')
    print('6: show users logged in: ')
    print('7: show ports opened: ')
    print('8: delete files with specific extension: ')
    while (choice < 1 or choice > 7):
        choice = int(input('Please select an option [1 - 8]: '))
    if str(choice) == "1":
        createfiles(usr, passwd)
    if str(choice) == "2":
        copy(usr,passwd)
    if str(choice) == "3":
        dns(usr,passwd)
    if str(choice) == "4":
        cpu(usr,passwd)
    if str(choice) == "5":
        IPaddress=("input ping test")
        pingwebsite(usr,passwd,IPaddress)
    if str(choice) == "6":
        loggedin(usr,passwd)
    if str(choice) == "7":
        ports(usr,passwd)
    if str(choice) == "8":
        ext=input("file extension to remove")
        delete(usr,passwd,ext)
def connect(usr,passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host,port,usr,passwd)
    return ssh_client
#creates files
def createfiles(usr,passwd):
    ssh_client = connect(usr,passwd)
    ssh_client.exec_command("touch file1.txt file2.txt file3.dat file4.dat")
    ssh_client.close()
#copys home directory
def copy(usr,passwd):
    ssh_client = connect(usr, passwd)
    ssh_client.exec_command("cp * ssh_dir")
    ssh_client.close()
#gets the dns
def dns(usr,passwd):
    results = []
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command('grep "nameserver" /etc/resolv.conf')
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())
#checks cpu usage
def cpu(usr,passwd):
    results=[]
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command("ps --sort=-pcpu | head -n 5")
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())
#pings website
def pingwebsite(usr,passwd,IPaddress):
    results = []
    ssh_client = connect(usr, passwd)
    command = "ping " + str(IPaddress)
    stdin, stdout, sterr = ssh_client.exec_command(command)
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())
#checks logged in users
def loggedin(usr,passwd):
    results = []
    ssh_client = connect(usr, passwd)
    stdin, stdout, sterr = ssh_client.exec_command("usr")
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())
#shows opened ports
def ports(usr,passwd):
    results = []
    ssh_client = connect(usr, passwd)
    command = "netstat -atu"
    stdin, stdout, sterr = ssh_client.exec_command(command)
    for line in stdout:
        results.append(line.strip('\n'))
    ssh_client.close()
    for i in results:
        print(i.strip())
#deletes all files of specific extension
def delete(usr,passwd,ext):
    ssh_client = connect(usr, passwd)
    rmCommand = "cd ssh_dir;rm *." + str(ext)
    ssh_client.exec_command(rmCommand)
    ssh_client.close()
#runs the SSH and the commands with it

active = True  # this will activate the menu
while (active == True):
    menu()