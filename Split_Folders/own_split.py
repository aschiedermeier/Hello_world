# my own split program
# split up files into a given ratio
# move from source folder into tran and test folder
# randomized by using sample method
# no empty files are moved

import os
import shutil
from random import sample


# r needed for absolute path
src = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\source"
train = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\train"
test = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\test"
# split size
split_size = .8

# read src folder
files = os.listdir(src)

#change directory to source directory
os.chdir(src)


print("files:", len(files))

# train_list_len is defined by split_size
len_train_list = int(split_size*len(files))
print(len_train_list)

# Prints list of random items of given length 
train_files= sample(files,len_train_list) 
print(train_files) 

# size of files    
for file in train_files:      
    print ("name: ", file)
    print("size: ",os.path.getsize(file))

# copy files 
# count = 0      
# for file in train_files:
#     if os.path.getsize(file) != 0:
#         shutil.copy(file, train)
#         print("copied: ",file)
#         count +=1
# print (count," files copied to train")

# move files
# use fUll_destination path to overwrite
count = 0
for file in train_files:
    if os.path.getsize(file) == 0:
        print(file, " is zero length, so ignoring")
    else:
        full_dest = os.path.join(train, file)
        shutil.move(file, full_dest)
        print("moved: ",file)
        count +=1
print (count," files moved to train")

# read updated src folder
files = os.listdir(src)

count = 0
for file in files:
    if os.path.getsize(file) == 0:
        print(file, " is zero length, so ignoring")        
    else:
        full_dest = os.path.join(test, file)
        shutil.move(file, full_dest)
        print("moved: ",file)
        count +=1
print (count," files moved to test")


