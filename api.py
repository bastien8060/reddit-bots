#!/bin/python3
import praw
import requests
import sys
import json
import time
import os
import datetime

patterns = ["Meme", "meme", "dam", "joke", "vs", "rick"]
reddit = praw.Reddit(client_id='bL-DxWUFpJRozQ',client_secret='H9OAgZA4sMwkHwq-IydwY_lCKh0',user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',username = 'oscar_hauey',password = 'bastienRES13')

def checkpost(id):
  submission = reddit.submission(id=id)
  print(submission.title)
  flair = submission.link_flair_text
  timed = submission.created
  daten = datetime.datetime.fromtimestamp(timed)
  day = int(datetime.datetime.fromtimestamp(timed).weekday())+1
  print(flair,day)
  if day > 5: 
    if flair == "Meme":
      print(id,"SHOULD BE DELETED!")
      print(flair,day,daten)
      time.sleep(0.2)
    for p in patterns:
      if p in submission.title:
        print(id,"ALERT!")
        print("\n",p,"\n")
        time.sleep(3)

  
  print("\n \n \n")



url = 'https://api.pushshift.io/reddit/search/submission/?after=1592697600&subreddit=camphalfblood&size=1000'
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
print(url)
page = requests.get(url, headers=header)
print(page)
if page.text == '{"message": "Not Found", "error": 404}':
    print("404 Not Found!")
    exit(0)
userposts = json.loads(page.text)

print(len(userposts["data"]))
time.sleep(1)
for x in userposts["data"]:
  checkpost(x["id"])
  

#submission = reddit.submission("8dmv8z")
#submission.delete()