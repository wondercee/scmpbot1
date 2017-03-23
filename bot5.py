import twitter, sys

# this app is being run by cast laboratory..@CASTlaboratory (4003669463)
consumer_key="rDGbpj3FzI8Eh5E4rwFPtH3n9"
consumer_secret="rm64Bg2gREsc1X0W84RAbLoESgj04RzVCK3rUFz7CNwHxYPdUY"
access_token="842005917424078848-yBX3k2hH6NKrkWAlbaWSNlajAaq0itF"
access_token_secret="yyc2JjzCrPSOcpl4v02HeTZwp01viapAf0A1O8c5kfTKM"

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
