import os
from random import shuffle

#create destination directory
try:
    copydir = "copyuni/"
    os.makedirs(copydir)
    print("Directory '%s' created" %copydir) 
except OSError as e:
        print (e)
        pass

# define source and destination
sourcedir = "uni/"
destdir = "copyuni/"

# check source files
unidir= os.listdir(sourcedir)
print (unidir)

# shuffle source files
shuffle(unidir)


import shutil

for file in unidir:
    print (file)
    shutil.copy (file,destdir)

# sourcefile= sourcedir + unidir[0]
# print (sourcefile)
# copyfile = copydir + unidir[0]
# print (copyfile)

# #copyfile(sourcefile, copyfile)


#for i in unidir:
#    print (i)
#    copyfile(sourcedir/i, copydir/i)

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