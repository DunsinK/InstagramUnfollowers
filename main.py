from bs4 import BeautifulSoup
from js import document

async def notFollowingBack(event):
    print("main.py running")
    following = document.getElementById("following-file").files.item(0)
    followers = document.getElementById("followers-file").files.item(0)
    not_following_back = {}
    print(following)
    print(followers)
    
    if not (following and followers):
        document.getElementById("results").innerHTML = "<p>Please select both files.</p>"
        return
    followString = await following.text()
    followersString = await followers.text()
    #print(followString)
    #print(followersString)

    followersSoup = BeautifulSoup(followersString, 'lxml') # makes soup object
    followers_name_tags = followersSoup.find_all('a') # finds all name <a> tags
    followingSoup = BeautifulSoup(followString, 'lxml') 
    following_name_tags = followingSoup.find_all('a') 

    for tag in following_name_tags:
        #print(tag.text)
        not_following_back[tag.text] = 0
    for tag in followers_name_tags:
        try:
            del not_following_back[tag.text]  
        except:
            continue 
    listVar = document.getElementById("list")
    for key in not_following_back:
        print(key)
        resultsDiv = document.getElementById("results")
        li = document.createElement("li")
        li.textContent = key
        listVar.appendChild(li)

document.getElementById("process-btn").onclick = notFollowingBack

#How the Program works
# Import your follower and following html files then adjust the html in the open method to be accurate  
# the program then reads the all <a> tags and delete them if them match in both files from a list 
# It then returns a list of names that you follow but arent following you back