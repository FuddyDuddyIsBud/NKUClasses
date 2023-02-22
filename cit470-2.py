import os
num=input("Enter a port: ")
result = os.system(f"firewall-cmd --add-port={port}/tcp --permanent")
if result==0:
    print("Port", num, "Added to firewall.")
    result = os.system("firewall-cmd --reload")
    if result==0:
        print("Firewall reloaded.")
    else:
        print("Issue reloading firewall")
else:
    print("Issue adding port to firewall")
