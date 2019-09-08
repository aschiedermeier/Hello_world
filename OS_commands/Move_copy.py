## move and copy files with shutil
# https://www.youtube.com/watch?v=8F0JkL94bo4
# https://github.com/moondra2017/Python-Stuff

import shutil
import os

# r needed for absolute path
src = r"C:\Users\Andi\Desktop\A"
dest = r"C:\Users\Andi\Desktop\B"

# read both folders
files = os.listdir(src)
print(files)
files2 = os.listdir(dest)
print(files2)

#change directory to source directory
os.chdir(src)

# open files in src
for file in files:
    if os.path.isfile(file): # read only files, not folders
        with open(file) as f:
            print(file, f.read())

# copy files        
# for file in files:
#     if os.path.isfile(file): # copy only files, not folders
#         shutil.copy(file, dest) 

#edit file1.txt for evidence
#overwritting

# move files
# error, if target file already there - can't overwrite
# for file in files:
#     if os.path.isfile(file):
#         shutil.move(file, dest)

# move files
# use fUll_destination path to overwrite
for file in files:
    if os.path.isfile(file):
        print(dest)
        full_dest = os.path.join(dest, file)
        print(full_dest)
        print("\n")
        shutil.move(file, full_dest)