import os

cwd = os.getcwd()
print ("current dir:", cwd)    

# r needed for absolute path
path = r"C:\Users\Andi\Documents\GitHub\GitHubData\Hello_world\WebCrawl"

filename = "links.txt" # short testfile
filename = "bookmarks_09.09.19.html" # short testfile
# filename = "links_ph.txt" # long realfile

# file to download with clear absolute path
full_path = os.path.join(path, filename)

# check current directory
cwd = os.getcwd()
print ("current dir:", cwd)    

# open text document with hyperlinks to ph videos
try:
   
    stream = open(full_path, "rt") 
    
    # in case of success we get an object from the open() function and we assign it to the stream variable;
    a= stream.read()
    print (a)
    stream.close()
except Exception as exc:
    # if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)
    print("Cannot open the file:", exc) 



