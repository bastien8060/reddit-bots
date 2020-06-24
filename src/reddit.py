import requests
import sys
import json
import time
import os

class bcolors:
    HEADER = '\033[95m'
    CONTENT = '\033[94m\033[4m'
    FLAIR = '\033[93m'
    SUBREDDITPOST = '\033[92m'
    SUBREDDIT = '\033[93m'
    USER = '\033[91m'
    VOTE = '\033[91m'
    ENDC = '\033[0m'
    ENDCO = '\033[0m\033[0m'
    BOLD = '\033[1m'
    TITLE = '\033[92m\033[4m\033[1m'
    ENDTITLE = '\033[0m\033[0m'
    UNDERLINE = '\033[4m'
rows, columns = os.popen('stty size', 'r').read().split()
halfcol = int(columns) / 2 + ((int(columns) / 2) / 2)
r = 0
if len(sys.argv)>2:
        maxi = sys.argv[2]
else:
        maxi = 1    

def limit(titlein):
    title = bcolors.TITLE+titlein+bcolors.ENDTITLE
    print("\n \n")
    print('#' * int(columns))
    print("\n")
    print(title.center(int(columns)))
    print("\n")


url = 'https://www.reddit.com/user/'+sys.argv[1]+"/.json"
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
print(url)
page = requests.get(url, headers=header)
print(page)
if page.text == '{"message": "Not Found", "error": 404}':
    limit("404 User Not Found!")
    limit("")
    exit(0)
userposts = json.loads(page.text)





limit("Posts:")



for i in userposts["data"]["children"]:
    if i["kind"] == "t3":
        print(bcolors.BOLD,"Post Title:",bcolors.ENDC, bcolors.CONTENT+i['data']['title']+bcolors.ENDCO,bcolors.VOTE,i["data"]["score"],"Upvotes",bcolors.ENDC,bcolors.FLAIR,i["data"]["link_flair_text"],bcolors.ENDC,bcolors.SUBREDDITPOST,i["data"]["subreddit_name_prefixed"],bcolors.ENDC)
        time.sleep(0.1)



limit("Comments:")





for i in userposts["data"]["children"]:
    if i["kind"] == "t1":
        print(bcolors.CONTENT + i["data"]["body"][:int(halfcol)] + bcolors.ENDCO ,"to:",bcolors.USER +i["data"]["link_author"]+bcolors.ENDC,"on:",bcolors.SUBREDDIT +i["data"]["subreddit_name_prefixed"]+bcolors.ENDC,"\n \n")
        time.sleep(0.4)
