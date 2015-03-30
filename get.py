#!/usr/bin/env python
import sys
import tweepy
from datetime import datetime
import os

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#getting current followers list
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
currentFileName = "%s" % datetime.now().strftime("%Y%m%d--%H-%M")
theFile = file(currentFileName, "w")
for page in tweepy.Cursor(api.followers).pages():
    for pageNr in page:
        theFile.write(pageNr.screen_name+"\n")
theFile.close()

#accessing previous file generated
prevFile = None
for root,d,files in os.walk("."):
    files.sort()
    for fn in files:
        if fn[-3:] == ".py":
            continue
        if fn != currentFileName:
            prevFile = fn
#cmpFile = file(prevFile,"r")

import difflib
fromfile, tofile = prevFile, currentFileName

fromlines = open(fromfile, 'U').readlines()
tolines = open(tofile, 'U').readlines()

diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile)
sys.stdout.writelines(diff)
