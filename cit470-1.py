import re
import os

Pings=[]
bad=[]
notIP=[]

def valid(ip):
    pattern=r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    return re.match(pattern, ip)

with open("ips.txt", "r") as f:
    addresses=f.readlines()

for ip in addresses:
    ip=ip.strip()  
    if not valid(ip):
        notIP.append(ip)
        continue
    result=os.system(f"ping -c 1 {ip}")
    if result==0:
        Pings.append(ip)
    else:
        bad.append(ip)

if Pings:
    print("Works:")
    print("\n".join(Pings))
if bad:
    print("Doesn't work:")
    print("\n".join(bad))
if notIP:
    print("invalid ip's:")
    print("\n".join(notIP))
