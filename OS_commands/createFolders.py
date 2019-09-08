import os
try:
    dir = "test/1"
    os.makedirs(dir)
    print("Directory '%s' created" %dir) 
except OSError as e:
        print (e)
        pass


