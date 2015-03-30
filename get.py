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
api = tweepy.API(auth, secure=True)

currentFileName = "%s" % datetime.now().strftime("%Y%m%d--%H-%M")
theFile = file(currentFileName, "w")


followers = api.followers_ids(screen_name='ancho85')
userList = []
sortedUserList = []
for page in followers:
    userList.append(page)
    if len(userList) == 100:
        results = api.lookup_users(user_ids=userList)
        for result in results:
            sortedUserList.append(result.screen_name)
        userList = []
if len(userList)>0:
    results = api.lookup_users(user_ids=userList)
    for result in results:
        sortedUserList.append(result.screen_name)
sortedUserList.sort()
for user in sortedUserList:
    theFile.write(user+"\n")

#accessing previous file generated
prevFile = None
#for root,d,files in os.walk("."):
for fn in sorted(os.listdir(".")):
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
