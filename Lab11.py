#!/usr/bin/python3
from collections import Counter
import re
logfile = "appache-access_log"
#opens the logfile and put the data into content
def getFileData():
    logfile = "appache-access_log"
    with open(logfile) as file:
        content = file.read()
        return content
#used to take regex on ip addresses and counts their usesaged
def genClientIP(data):
    print('Frequency of Client IP Addresses: ')
#ip regex
    reg = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|::\d'
    base = 0
#gets the dulplicate ip addresses
    IP = re.findall(reg, data)
#counts it
    IPnum = Counter(IP)
#prints ip and the number of times it's been used to the log
    for k, v in IPnum.items():
        base = base + v
        print(str(k) + '\t' + str(v * '*'))
    print('total ' + str(base) + '\n')
#gets the status codes
def genStatusCode(data):
    print('HTTP Status Codes Summary: ')
#regex to get status code
    reg = '" \d{1,3}'
    Count = 0
#same as above gets duplicates
    status = re.findall(reg, data)
    statuscounter = Counter(status)
#gets the total amount
    for k, v in statuscounter.items():
        Count = Count + v
#does the perc entage calculations and the current status code percentage
    for k, v in statuscounter.items():
        newstring = k.strip('"')
        ammount = (v / Count) * 100
        ammount = str(round(ammount, 2))
#prints it
        print(str(newstring) + ':' + '\t' + str(ammount) + '%')
    print('total ' + str(Count))
#the visual for the data
def printReport():
    print('--------------------------------------------------')
    print('Statistics for the Apache log file access_log')
    print('-------------------------------------------------')
    print(genClientIP(info))
    print(genStatusCode(info))
#function calls
info = getFileData()
printReport()