from bs4 import BeautifulSoup
from js import document

def notFollowingBack():
    not_following_back = {}
    print("main.py ran")
    with open('following.html','r') as following:
        followString = following.read()
        
        with open('followers_1.html','r') as followers:
            followersString = followers.read()

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
            for key in not_following_back:
                print(key)
print("im running!")
document.getElementByID("process-btn").onclick = notFollowingBack

#How the Program works
# Import your follower and following html files then adjust the html in the open method to be accurate  
# the program then reads the all <a> tags and delete them if them match in both files from a list 
# It then returns a list of names that you follow but arent following you back