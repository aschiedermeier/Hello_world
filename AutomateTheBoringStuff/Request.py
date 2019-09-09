# Automate the Boring Stuff with Python
# Practical programming for total beginners. Written by Al Sweigart.
# # Chapter 11 – Web Scraping

# request.get(): download from the internet
# status_code == requests.codes.ok: check if ok
# raise_for_status(): method to raise exception after download error
# iter_content(): return chunks of the content on each iteration though the loop. 100000 bytes is a good size
import requests
import os

# get txt.file
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#res = requests.get('https://automatetheboringstuff.com/images/automate_small_cover.png')


# check if it's ok
print("Download success:", res.status_code == requests.codes.ok)

# print type, length and some content
print(type(res))
print("Size of text:",len(res.text))
print("Size of content:",len(res.content))
print(res.text[:250])
print()

# download location
# r needed for absolute path
path = r"C:\Users\Andi\Documents\GitHub\0_GitHubFiles\Hello_world\AutomateTheBoringStuff"
filename = "RomeoAndJuliet.txt" 
#filename = "automate_small_cover.png" 
# file to download with clear absolute path
full_path = os.path.join(path, filename)

# open file to download to in write binary mode ("wb") to maintain the Unicode encoding. (even a txt.file)
playFile = open(full_path, 'wb')


# copy chunk by chunk: 100K bytes is a good measure

size = len(res.content)/1000
print("Size of content:",size)

downloaded = 0
for chunk in res.iter_content(100000):
        playFile.write(chunk)
        downloaded += 100
        done = round(downloaded/size*100,2)
        if downloaded < size:
            print ("Downloaded",downloaded,"Kbyte from",size)
            print ("Downloaded",done,"%")
        else:
            print ("Downloaded",size,"Kbyte from",size)
            print ("Downloaded","100","%")

playFile.close()

print("Size of downloaded file:",os.path.getsize(full_path))

####
### example of unsuccessful download

# get page
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

# check if it's ok
print(res.status_code == requests.codes.ok)
print(res.status_code) # 400 is not ok
print(requests.codes.ok) # 200 is ok

# Always call raise_for_status() after calling requests.get(). 
# You want to be sure that the download has actually worked before your program continues.
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))