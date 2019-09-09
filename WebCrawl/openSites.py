# ph download helper
# input list of ph download links
# using bookmarks as html file, then rightclick "untersuchen", then past into console:
# urls = $$('a'); for (url in urls) console.log ( urls[url].href );
# download txt.file of links


# todo
"""
aks after ten round if i want to continue
find downlaod link in new link 
automatically download
check if already downloaded

"""
import time

# open document with hyperlinks to ph videos
try:
    stream = open("links_ph.txt", "rt") 
    # in case of success we get an object from the open() function and we assign it to the stream variable;
    a= stream.read()
    stream.close()
except Exception as exc:
    # if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)
    print("Cannot open the file:", exc) 


round = 0
while True:
    round +=1
    print (round)
    # ## sleep after x rounds for a while 
    # if round%1 == 0:
    #     print ("Sleep every '%s' round" %round)
    #     time.sleep(1)

    # pause every 10 round, must continue manually
    if round%10 == 0:
        input("\nPress 'return' when your are ready!\n")

# entered = False
# while entered == False:
#     review = input("\nDo you want to review those starsigns first?\ny/n: ")

#         input("\nPress 'return' when your are ready!\n")
#         # call clear function we defined above 
#         ## clear() 
#     else: 
#         print ("Cool, let's go!")

#     entered = True  



    ## stop after 5 rounds for testing reasons
    #if round == 5:
    #    break 

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

    # importing webbrowser python module
    import webbrowser
    #Open url in default browser
    webbrowser.open(strURL, new=2)
    
    # The 'new' parameter have special significance.
    # If new = 0, open URL in same browser window
    # If new = 1,  opens URL in new browser window
    # If new = 2, open URL in same tab.
