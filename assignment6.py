#task1
import argparse as ap
import subprocess

subprocess.run(['rm', '-r', 'Task8'])
subprocess.run(['mkdir','Task8'])

pobj = ap.ArgumentParser()
pobj.add_argument('-H', dest='H', type=str, help='USAGE:<script name> [options] [directory] Once displayed, then exit application')
pobj.add_argument('-W', '--word', action='store', dest='W', type=str, required=True, help='Use full path')
pobj.add_argument('-N', '--number', action='store', dest='N', type=int, required=False, help='input number of directories to create.')

result = pobj.parse_args()
h = result.H
w = result.W
n = result.N

if w:
    f=open("/usr/share/dict/words", "r")
    words = [w[i: j] for i in range(len(w)) for j in range(i + 1, len(w) + 1)]

if n:
    list = [ele if ele >= n else n for ele in words]

textfile=w+'.txt'

file = open(textfile, "w")
for x in words:
    file.write(w)
file.close()

subprocess.run(['mv', w, 'Task8'])


