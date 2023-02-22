#!/usr/bin/python3
import random
import sys
n=-1
while n<=0:
    n=int(input("please enter number of usernames required: "))
suffix_list=[]
usernames=[]
fho=open("sample.txt", 'w')

for i in range(n):
    suffix=0
    while suffix in suffix_list or suffix==0:
        suffix=random.randrange(15,100)
    suffix_list.append(suffix)
    uname="user_"+str(suffix)
    usernames.append(uname)

for user in usernames:
    fho.write(user+'\n')
fho.close()

with open('sample.txt', 'r') as f:
    file = f.read()
print(file)