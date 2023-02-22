#!/usr/bin/python3
import argparse as ap
#this is the argparse
pobj=ap.ArgumentParser()
pobj.add_argument('-g', action='store', dest='G', type=int, required=True,
                  help='Enter the group')
#the returned value of the argparse input
result=pobj.parse_args()
#puts it into group so it's easier to remember
group=result.G
#the total number of members in the group, starts at zero then adds up
total=0
#file where everything is stored, and reads it
passwd=open("/etc/passwd", "r")
#prints the visual
print("UserID     Full Name    GroupID")
print("=====      ========     =======")
#gets the data from passwd, spits it, and then groups it up under the visual.
for line in sorted(passwd.readlines()):
    c=line.split(":")
    if str(group) == c[3]:
        print(c[0] + ' ' + c[4] + ' ' + c[3])
        #adds to the total group by one to account for the newly added member
        total = total + 1
#prints the total number of members in group
print("Total number of users in group: " + str(total))
