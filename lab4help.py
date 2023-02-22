#!/usr/bin/python3
# imports csv library
import csv
# Needed lists and dictionaries
userid={}
names={}
rows=[]
heading=[]
row=[]
# reads the file and edits it's contents for the list based on the varible of being 250 and above
def read(rows, heading, userid):
    with open("employee-logins.csv", 'r') as InputFile:
        data=csv.reader(InputFile)
        heading=next(data)
        for row in data:
            if row[0] in userid.keys():
                id=row[0]
                logins=userid[id]
                logins=logins + int(row[4])
                userid[id]=logins
                names[id]=[row[1], row[2], logins]
            else:
                id=row[0]
                logins=int(row[4])
                userid[id]=logins
                names[id]=[row[1], row[2], logins]
        userid_copy=userid.copy()
        for key in userid_copy:
            if userid[key]<250:
                del userid[key]
        for key, values in names.items():
            if key in userid.keys():
                userid[key]=names[key]
# writes all the data to a new file called alotoflogins.csv
def write(rows, row, userid):
    with open('alotoflogins.csv', 'w') as file:
        pen=csv.writer(file)
        pen.writerow(['First name', 'Lastname', 'Login_count'])
        for key in userid.keys():
            file.write("%s\n" %  userid[key])
    print(userid)
read(rows, heading, userid)
write(rows, row, userid)