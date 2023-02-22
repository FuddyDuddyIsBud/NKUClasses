import os
cwd=os.getcwd()
directory=[d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
file=[f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
print("Directories:")
for d in directory:
    print("\t" + d)
print("Files:")
for f in file:
    print("\t" + f)