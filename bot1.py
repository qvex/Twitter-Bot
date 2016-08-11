import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open('text.txt', 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    print(line)
    time.sleep(15)
