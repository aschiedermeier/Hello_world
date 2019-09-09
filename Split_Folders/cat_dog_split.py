## split folder function
# based on tensorflow course
# input: 1 source, 2 target folders, split size (train/target data)

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

import os
import random
from shutil import copyfile

# TARGET dir needed later to define dirs 
# r needed for absolute path
TARGET = r"C:\Users\Andi\Documents\GitHub\0_GitHubFiles\Hello_world\Split_Folders"

cwd = os.getcwd()
print ("current dir:", cwd)

# change directory to TARGET
# new folder gets created there
os.chdir(TARGET)

cwd = os.getcwd()
print ("current dir:", cwd)


# # create folders the first time
# try:
#     dir = "tmp/PetImages/Cat/"
#     os.makedirs(dir)
#     print("Directory '%s' created" %dir) 
# except OSError as e:
#         print (e)
#         pass

# try:
#     dir = "tmp/cats-v-dogs/training/cats/"
#     os.makedirs(dir)
#     print("Directory '%s' created" %dir) 
# except OSError as e:
#         print (e)
#         pass

# try:
#     dir = "tmp/cats-v-dogs/testing/cats/"
#     os.makedirs(dir)
#     print("Directory '%s' created" %dir) 
# except OSError as e:
#         print (e)
#         pass




def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    pass

## read source folder
    files = os.listdir(SOURCE)
    print(len(files),"source files")


    ## train_list_len is defined by split_size
    len_train_list = int(SPLIT_SIZE*len(files))
    print(len_train_list, "shall go into the train list")

    ## Prints list of random items of given length 
    train_files= random.sample(files,len_train_list) 
    print(len(train_files),"training files")
    
    #train_files = train_files[:4]
    #print(train_files)
    print(train_files[0])
    source_file = os.path.join(TARGET,SOURCE, train_files[0])
    target_file = os.path.join(TARGET,TRAINING, train_files[0])

    
    print("source_file",source_file)
    print("target_file",target_file)
    
    
    cwd = os.getcwd()
    print ("current dir:", cwd)    

    #change directory to source directory
    os.chdir(SOURCE)
    
    cwd = os.getcwd()
    print ("new current dir:", cwd)  

   
    #copyfile(source_file, target_file) # always yes
    #copyfile(train_files[0], target_file) # also ok, but only if we are in source directory 
    #copyfile(train_files[0], TRAINING) # nope
    #copyfile(source_file, TRAINING) # nope
    #print("copied",train_files[0])

 
    # copy training files 
    count = 0      
    for file in files:
        if file in train_files:
            #source_file = os.path.join(TARGET,SOURCE, file)
            target_file = os.path.join(TARGET,TRAINING, file)
            if os.path.getsize(file) == 0:
                print(file, "is zero length, so ignoring")
            else:
                copyfile(file, target_file)
                print("copied:",file)
                count +=1
    print (count," files copied to train")

    cwd = os.getcwd()
    print ("current dir:", cwd)  



    # copy testing files 
    count = 0      
    for file in files:
        if file not in train_files:
        #source_file = os.path.join(TARGET, SOURCE, file)
            target_file = os.path.join(TARGET,TESTING, file)
            if os.path.getsize(file) == 0:
                print(file, "is zero length, so ignoring")
            else:
                copyfile(file, target_file)
                print("copied:",file)
            count +=1
    print (count," files copied to test")

    cwd = os.getcwd()
    print ("current dir:", cwd) 
#input data
CAT_SOURCE_DIR = "tmp/PetImages/Cat/" # no slash at the beginning!!!
TRAINING_CATS_DIR = "tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "tmp/cats-v-dogs/testing/cats/"
split_size = .6

#call function
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)

