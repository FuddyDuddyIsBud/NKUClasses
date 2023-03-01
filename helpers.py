import os
import subprocess as sp

file = blah
os.environ['file'] = file
txt_file = open(file, "r")
file_content = txt_file.read()
content_list = file_content.split(",")
print(content_list)
print(content_list[::-1])
txt_file.close()
