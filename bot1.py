import twitter, sys

# this app is being run by cast laboratory..@CASTlaboratory (4003669463)
consumer_key="VqhBSfrKUrYyRKQQSAHxXnlyE"
consumer_secret="XmT0vZ0cm8U8ueHyvONAUTeBiFkkqobukHclbvAv2M2baHCV7c"
access_token="841984028072919040-7wlxtecpYP8Cef2i7MiWOzHD7evXmyA"
access_token_secret="Mg9AJ42usoIlMpgZaHI37naeAXbcACyjmtkgY2N3rk1oq"

auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)

u = "1533860107"
print >> sys.stderr, 'Retweeting everything for user="%s"' % (u)
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
stream = twitter_stream.statuses.filter(follow=u)

for tweet in stream:

tweetText = tweet['text'].encode('utf-8')
print tweetText
user = tweet['user']['screen_name']
if tweetText.startswith('RT @'):
retweet = tweetText
else:
# if it starts with RT @ then its already a retweet...
retweet='RT @' + user.encode('utf-8') + ' ' + tweetText
retweet = retweet[:139]

print retweet
twitter_api.statuses.update(status = retweet)
