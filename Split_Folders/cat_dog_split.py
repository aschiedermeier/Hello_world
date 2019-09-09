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


#def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):

import os
import shutil
from random import sample

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

# # r needed for absolute path
# src = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\source"
# train = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\train"
# test = r"C:\Users\Andi\Documents\GitHub\Hello_world\Split_Folders\test"

    # define home directory
    home = os.getcwd()
    print ("home dir:", home)

    # os.chdir(SOURCE)
    # cwd = os.getcwd()
    # print ("current dir:", cwd)

    # read src folder
    files = os.listdir(SOURCE)
    print(len(files),"source files")
    # for f in files:
    #     print (f)
    #     full_f = os.path.join(SOURCE, f)
    #     print(os.path.getsize(full_f))


    # train_list_len is defined by split_size
    len_train_list = int(SPLIT_SIZE*len(files))
    print(len_train_list, "shall go into the train list")
    
    # #change directory to source directory
    # os.chdir(SOURCE)

    cwd = os.getcwd()
    print ("current dir:", cwd)    

    # Prints list of random items of given length 
    train_files= sample(files,len_train_list) 
    print(len(train_files)," training files")
    # for f in train_files:
    #     print (f)
    #     full_f = os.path.join(SOURCE, f)
    #     print(os.path.getsize(full_f))

    # copy files 
    count = 0      
    for file in train_files:
        if os.path.getsize(file) != 0:
            shutil.copyfile(file, train)
            print("copied: ",file)
            count +=1
    print (count," files copied to train")


    # move files
    # use fUll_destination path to overwrite
    count = 0
    for file in train_files:
        full_f = os.path.join(SOURCE, file)
        if os.path.getsize(full_f) == 0:
            print(file, " is zero length, so ignoring")
        else:
            shutil.move(file, TRAINING)
            print("moved: ",file)
            count +=1
    print (count," files moved to TRAINING")

    cwd = os.getcwd()
    print ("current dir:", cwd)    

    #change directory to home directory
    os.chdir(home)

    cwd = os.getcwd()
    print (cwd)

    # read updated src folder
    files = os.listdir(SOURCE)  
    print(len(files)," files")

    count = 0
    for file in files:
        full_f = os.path.join(SOURCE, file)
        if os.path.getsize(full_f) == 0:
            print(file, " is zero length, so ignoring")        
        else:
            full_dest = os.path.join(TESTING, file)
            shutil.move(file, full_dest)
            print("moved: ",file)
            count +=1
    print (count," files moved to TESTING")


#input data
CAT_SOURCE_DIR = "tmp/PetImages/Cat/"
TRAINING_CATS_DIR = "tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "tmp/cats-v-dogs/testing/cats/"
split_size = .9

# call function
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)

# Expected output
# 666.jpg is zero length, so ignoring
# 11702.jpg is zero length, so ignoring


### copied from original


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
def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
  
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
  source_file = os.path.join(SOURCE, train_files[0])
  target_file = os.path.join(TRAINING, train_files[0])
  
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
      #source_file = os.path.join(SOURCE, file)
        target_file = os.path.join(TRAINING, file)
        if os.path.getsize(file) == 0:
          print(file, "is zero length, so ignoring")
        else:
          copyfile(file, target_file)
          #print("copied:",file)
          count +=1
  print (count," files copied to train")

  cwd = os.getcwd()
  print ("current dir:", cwd)  
  

  
  # copy testing files 
  count = 0      
  for file in files:
      if file not in train_files:
      #source_file = os.path.join(SOURCE, file)
        target_file = os.path.join(TESTING, file)
        if os.path.getsize(file) == 0:
          print(file, "is zero length, so ignoring")
        else:
          copyfile(file, target_file)
          #print("copied:",file)
          count +=1
  print (count," files copied to train")

  cwd = os.getcwd()
  print ("current dir:", cwd)  

  
  

# YOUR CODE ENDS HERE


CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
TRAINING_CATS_DIR = "/tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "/tmp/cats-v-dogs/testing/cats/"
DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
TRAINING_DOGS_DIR = "/tmp/cats-v-dogs/training/dogs/"
TESTING_DOGS_DIR = "/tmp/cats-v-dogs/testing/dogs/"

split_size = .9
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)

print(len(os.listdir(TRAINING_CATS_DIR)))
print(len(os.listdir(TESTING_CATS_DIR)))
print(len(os.listdir(TRAINING_DOGS_DIR)))
print(len(os.listdir(TESTING_DOGS_DIR)))


# Expected output
# 666.jpg is zero length, so ignoring
# 11702.jpg is zero length, so ignoring

