# input text-file with links (e.g. extracted form bookmarks)
# finds ph links
# toList: list of links to tubeoffline: 
# links: list of all links on one tubeoffline site
# video_links: first video download link of every tubeoffline site
# downloads each video of video_links

# to do
"""
define functions for easier handling of the modules
extract links and downloads in batches of 5, so longer lists can be downloaded batch by batch
edit textfile at the end
"""

import os
import requests 
from bs4 import BeautifulSoup 

###

# open text document with hyperlinks to ph videos
try:
    stream = open("links_ph.txt", "rt") 
    #stream = open("links.txt", "rt") 
    
    # in case of success we get an object from the open() function and we assign it to the stream variable;
    a= stream.read()
    print (a)
    stream.close()
except Exception as exc:
    # if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)
    print("Cannot open the file:", exc) 

# toList: list of links to tubeoffline
# simply find all ph links with keyword "viewkey=ph
# then cut off video code onto tubeoffline link and add to toList
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


####    


#url = "https://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph5c4a47c510896"
#url="https://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph59a46a0f45ba8"

# video_links: first video download link of every tubeoffline site
# take each element of toList (a tubeoffline site)
video_links =[]
counter = 0
for url in toList:
    counter +=1
    print ("toList: ",counter)

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)

    # list of all links in tubeoffline page - needs to be refreshed every round
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
        print(link.get('href'))

    # finds first ph download link and puts into video_link list 
    print("first download link:")
    for l in links:
        print("checking")
        if l.find("phncdn.com/videos")!=-1:
            print("found one")
            print(l)
            video_links.append(l)
            #print("open link")
            #Open url in default browser
            #webbrowser.open(l, new=2)
            print("now break")
            break 


# test list, first one is already in folder and should be skipperd. 
# download second one
#video_links = ["https://cv.phncdn.com/videos/201708/28/130355821/720P_1500K_130355821.mp4?qnUcih0bmUPgxHObyKAKRrbBOEmL7eJ1us3aRm8slbailaYZ8deaXTIxMucWyFoLRIGsdylnIIqljOJIPIcT-1BxDy5CgJ2R-DDFduRzQtliIdCISR696SxqZwSuJb0DTWFCbEhydi6WX5EImZj2TzvmkIkOgWqUy7J94-is6cAibGnNbcBTe28s80qGlmVvn-ZX2EaNzpBOLvmwcTVeEU5gjc-OqVCUBRmJ90ibtZFj","https://cv.phncdn.com/videos/201804/20/162825732/720P_1500K_162825732.mp4?5OtCl1hb61uN0ehF65q2vfpTuXV2VaXAlPMJMGldVBQGpH3jg1lQkrmRsRZmA4CpVbEhyPi8D4Qxol7T2rRGkMMAT1UTYzuiS1eVYhTxMP_IvpBYwfdlyiPYImjPrA7TV_GoFFB_OhqjZNE7r0l_e4vLaU90Sha6ovPCQoXysoSgDiEeQDrSAtJNbirOuDRfhhEYPfT0d9I"]
for l in video_links:
    print (l)

# destination folder
dest = r"C:\Users\Andi\Downloads"
dest = r"C:\Users\Andi\Desktop\A"
files = os.listdir(dest)
print(files)

# function to download all links in list
def download_video_series(video_links): 
  
    for link in video_links: 
  
        '''iterate through all links in video_links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string 
        file_name = link.split('/')[-1]    
        
        # if filename too long, cut off at "mp4"
        mp4= file_name.find("mp4")
        file_name=file_name[:mp4+3]

        if file_name not in files:
            print ("Downloading file:%s"%file_name )
            
            # create response object 
            r = requests.get(link, stream = True) 

            full_dest = os.path.join(dest, file_name)

            # download started 
            with open(full_dest, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 
            
            print ("%s downloaded!\n"%file_name )
        
        else:
            print("%s already downloaded"%file_name)    

    print ("All videos downloaded!")
    return
  

# download all videos 
download_video_series(video_links) 
     















# import requests 
# from bs4 import BeautifulSoup 

# link = "https://cv.phncdn.com/videos/201804/20/162825732/720P_1500K_162825732.mp4?7zPppvI-M9dYUkZcYnDHz-Jvlkv8CBqfD4ABbokMhNNzz46jTFKET43esneQxSdE9NcPx3eJt0yab4pm-Rge0Kv3tWxx60m0grLaTMWCglQvPZaHN10MLff5Rj8TWPHgf7iDYOlnNLSJ0WVtTPlc5JpxQF2rh0u0pY9uqxyFwQMRbtDs6TdJpD5PwrnLvZlHB6uoWO0sTpa0UlDUNvXk07LJ5Zvx25aYh1SBY1R_aVd4MHE"

# # obtain filename by splitting url and getting  
# # last string 
# file_name = link.split('/')[-1]

# mp4= file_name.find("mp4")
# print(mp4)
# file_name=file_name[:mp4+3]
# print(file_name)

# print ("Downloading file:%s"%file_name)
    
# # create response object 
# r = requests.get(link, stream = True) 
    
# # download started 
# with open(file_name, 'wb') as f: 
#     for chunk in r.iter_content(chunk_size = 1024*1024): 
#         if chunk: 
#             f.write(chunk) 