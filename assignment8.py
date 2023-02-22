import re
import exrex
import glob
import shutil
import os
#task1
f = open("/usr/share/dict/american-english", 'r')

pattern = '[aeiou]{4}$'

words = f.readlines()

word=[]

matchlist = [word for word in words if re.match(pattern, word)]

#task 2
username=input('enter username')
password=input('enter password')
usernamefirst=username[0]
usernamelast=username[-1]

if re.match(r'^[a-zA-Z]{1}[a-zA-Z0-9_]{8}[a-zA-Z]{1}$',password):
	print("password works.")

else:
	newpass = exrex.getone(r"[a-zA-Z0-9_]{8}")
	newpass = usernamefirst+newpass+usernamelast

#task3
os.mkdir("./new")
os.mkdir("./strong")
filelist = glob.glob('new/*.txt')
pattern = r'^[\D+][*]{*}[\D+]$'
pattern_with_path = 'new/' + pattern + '.txt'

shortlist = [f for f in filelist if re.match(pattern_with_path, f)]

shutil.move("new/file1.txt", "strong/file1.txt")

for shortlist in range(n):
	shutil.move("new/file.txt", "strong/file.txt")