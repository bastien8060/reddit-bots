#!/bin/python3
import praw
from datetime import date
import time

olddate = 0
reddit = praw.Reddit(client_id='bL-DxWUFpJRozQ',client_secret='H9OAgZA4sMwkHwq-IydwY_lCKh0',user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',username = 'oscar_hauey',password = 'bastienRES13')

#reddit.subreddit("festus8070").wiki['index/sidebar'].edit("my new sidebar")
#print(reddit.subreddit("festus8070").mod.settings())
while True:
	def weekend():
		print("Weekend Mode Activated!")
		reddit.subreddit("festus8070").mod.update(allow_images="false")
		reddit.subreddit("festus8070").mod.update(allow_polls="false")
		reddit.subreddit("festus8070").mod.update(link_type="self")
	def weekday():
		print("Weekday Mode Activated!")
		reddit.subreddit("festus8070").mod.update(allow_images="true")
		reddit.subreddit("festus8070").mod.update(allow_polls="true")
		reddit.subreddit("festus8070").mod.update(all_original_content="false")
		reddit.subreddit("festus8070").mod.update(link_type="any")

	#day = (date.today().weekday())+1
	day = 6
	print(day)
	if olddate == day:
		print("No change")
	else:
		if day > 5:
			weekend();
		else:
			weekday();

	olddate = day

	time.sleep(600)