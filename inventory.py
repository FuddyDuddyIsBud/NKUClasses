import json
import pwd
import subprocess as sp

users = {}

userlist = pwd.getpwall()

with open('userfile.json') as f:
    userlist = json.load(f)

for i in range(len(userlist)):
    users = {}
    users['username'] = userlist[i].pw_name
    users['password'] = userlist[i].pw_passwd
    users['GID'] = userlist[i].pw_gid
    users['UID'] = userlist[i].pw_uid
    users['path'] = userlist[i].pw_dir
    userlist.append(users)

with open('userfile.json','w') as f:
    json.dump(users,f)

def update(users):
    with open('userfile.json') as f:
        userinfo = json.load(f)
        usercontent= userinfo.read()
        userinfo = json.load(f)
        userinfo=userinfo.read()
        userinfo.append(userlist)
        userlist.append(users)
    
def delete(userlist):
    with open('userfile.json') as f:
        userinfo = json.load(f)
        userinfo=userinfo.read()
        chosenuser=input("input name of user to delete: ")
        sp.run('userdel', chosenuser)
        userinfo.remove(chosenuser)
        userinfo.append(userlist)
        userlist.append(users)
        with open('userfile.json') as f:
            json.dump(users, f)
        
update(users)
delete(userlist)