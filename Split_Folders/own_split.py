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


# Write a python function called split_data which takes
# a SOURCE directory containing the files
# a TRAINING directory that a portion of the files will be copied to
# a TESTING directory that a portion of the files will be copie to
# a SPLIT SIZE to determine the portion
# The files should also be randomized, so that the training set is a random
# X% of the files, and the test set is the remaining files
# SO, for example, if SOURCE is PetImages/Cat, and SPLIT SIZE is .9
# Then 90% of the images in PetImages/Cat will be copied to the TRAINING dir
# and 10% of the images will be copied to the TESTING dir
# Also -- All images should be checked, and if they have a zero file length,
# they will not be copied over
#
# os.listdir(DIRECTORY) gives you a listing of the contents of that directory
# os.path.getsize(PATH) gives you the size of the file
# copyfile(source, destination) copies a file from source to destination
# random.sample(list, len(list)) shuffles a list
#def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
# YOUR CODE STARTS HERE
# YOUR CODE ENDS HERE

# os.listdir(DIRECTORY) gives you a listing of the contents of that directory
# os.path.getsize(PATH) gives you the size of the file
# copyfile(source, destination) copies a file from source to destination
# random.sample(list, len(list)) shuffles a list


# CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
# TRAINING_CATS_DIR = "/tmp/cats-v-dogs/training/cats/"
# TESTING_CATS_DIR = "/tmp/cats-v-dogs/testing/cats/"
# DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
# TRAINING_DOGS_DIR = "/tmp/cats-v-dogs/training/dogs/"
# TESTING_DOGS_DIR = "/tmp/cats-v-dogs/testing/dogs/"

# split_size = .9
# split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
# split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)

# Expected output
# 666.jpg is zero length, so ignoring
# 11702.jpg is zero length, so ignoring
