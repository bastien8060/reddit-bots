#!/bin/python3
import os
import sys

if not len(sys.argv) > 1:
        print("Enter SubReddit!")
        print("$ "+sys.argv[0]+" subreddit-name")
        exit(0)
else:
        sr = sys.argv[1]


os.system('python3 src/api.py '+sr)
