import shutil
from pathlib import Path
import os.path

ignoredir = input("Path to ignore: ")
newdir = input("Path to add: ")

path = open("path.txt")
dirs = []
for line in path:
    dirs.append(line.strip())

for n in dirs:
    dst = n.replace(ignoredir, newdir)
    dst = dst.rstrip('\\')
    os.mkdir(dst)
    shutil.copy(n, dst)

path.close()
