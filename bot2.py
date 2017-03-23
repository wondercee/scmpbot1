import twitter, sys

# this app is being run by cast laboratory..@CASTlaboratory (4003669463)
consumer_key="PZ9KyEvqfasbqg9V7eu2IqXd2"
consumer_secret="gEishFs95FQMdlv0rktRL4jfWNXuuNfgBSbVLp7CfEkAe1PTqj"
access_token="841990754134331393-xpvxKTNURaE0tt8BUcFwIeCmC6Ob5Py"
access_token_secret="s45lroRn15T8fFGz9qsjU7imYcwfSi029DcApEVgKhRvD"

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
