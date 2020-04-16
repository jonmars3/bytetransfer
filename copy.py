import shutil

path = open("path.txt")
dst = 'folderB/'
dirs = []
for line in path:
    dirs.append(line.strip())

for n in dirs:
    shutil.copy(n, dst)

path.close()
