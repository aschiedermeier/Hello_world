# input: text document with hyperlinks
# finds ph links
# output: toList with tubeoffline links

import os

cwd = os.getcwd()
print ("current dir:", cwd)    

# r needed for absolute path
path = r"C:\Users\Andi\Documents\GitHub\GitHubData\Hello_world\WebCrawl"

filename = "links.txt" # short testfile
# filename = "links_ph.txt" # long realfile

# file to download with clear absolute path
full_path = os.path.join(path, filename)

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

toList = []

while True:
    # find ph videolink
    ph= a.find("viewkey=ph")
    # if no video found, stop program
    if ph == -1:
        break
    
    # find name of video
    phkey = a[ph+10:ph+24]

    # shorten link for next round
    a= a[ph+23:]
    
    # base of URL of tubeoffline
    URL = "https://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph"
    # concatenate to new URL
    strURL = URL + phkey

    toList.append(strURL)

for l in toList:
    print (l)

