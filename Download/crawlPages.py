# C:\Users\Andi\Documents\2016 Udacity Videos\03 Computer Science\0 Done\Lesson 2- How to Repeat Videos

#print (get_page(https://xkcd.com))

from bs4 import BeautifulSoup, SoupStrainer
import requests
import webbrowser

url = "http://stackoverflow.com/"
url = "https://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph5c4a47c510896"
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

#print (data)
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    print(link.get('href'))

print("first download link:")
for l in links:
    print("checking")
    if l.find("phncdn.com/videos")!=-1:
        print("found one")
        print(l)
        print("open link")
        #Open url in default browser
        webbrowser.open(l, new=2)
        print("now break")
        break    
#https://dv.phncdn.com/videos/201901/24/203619751/720P_1500K_203619751.mp4?ttl=1567975943&ri=1433600&rs=1416&hash=db28eec2178093059ee532f5bba7cfbd
# https://ev.phncdn.com/videos/201901/24/203619751/720P_1500K_203619751.mp4?validfrom=1567968829&validto=1567976029&rate=177k&burst=1400k&hash=8KJF4eIaouJeVxx8n7UvhpcnLYg%3D
