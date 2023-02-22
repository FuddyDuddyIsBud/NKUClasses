import re,os,os.path as p, argparse as ap

# create parser objecte and add arguments
pobj=ap.ArgumentParser()
pobj.add_argument('-d',action="store",dest='dir',default='.',help='A directory is required')# use current working directory as default directory if not provided
pobj.add_argument('-e',action="store",dest='ext',default='py',help='A file extension is required') #use py as default file extension if not provided
res=pobj.parse_args()
# pick values associated without various options and store ain appropriate variables
dir=res.dir
ext=res.ext

dirList=[]# store directory listing

if not (p.exists(dir)):
    print("Sorry this is an invalid directory")
    exit(1)
else:
    dirList=os.listdir(dir)
reg=ext+'$'# regex ensures extension macthes end of filename being searched

for file in dirList:
    if re.search(reg,file):
        print(file)




