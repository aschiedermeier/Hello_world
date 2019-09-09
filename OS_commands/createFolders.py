import os


cwd = os.getcwd()
print (cwd)

# no "/" create here
try:
    dir = "test_no_slash/1"
    os.makedirs(dir)
    print("Directory '%s' created" %dir) 
except OSError as e:
        print (e)
        pass

cwd = os.getcwd()
print (cwd)

# with "/" create at c:
try:
    dir = "/test_with_slash/1"
    os.makedirs(dir)
    print("Directory '%s' created" %dir) 
except OSError as e:
        print (e)
        pass

cwd = os.getcwd()
print (cwd)
