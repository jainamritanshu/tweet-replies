import tweepy
from keys import keys
CONSUMER_KEY = keys['c_key']
CONSUMER_SECRET = keys['c_secret']
ACCESS_TOKEN = keys['a_token']
ACCESS_TOKEN_SECRET = keys['a_token_s']auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_a_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)twts = api.search(q="Leviathan")

#list of specific strings we want to check for in Tweets
t = ['Leviathan!',
'Leviathan']

for x in twt:
for i in t:
if i == x.text:
u_name = s.user.screen_name
m = "@%s nice tweet" % (u_name) #your message or reply
x = api.update_status(m, x.id)