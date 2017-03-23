import twitter, sys

# this app is being run by cast laboratory..@CASTlaboratory (4003669463)
consumer_key="USNqzBnz5qMRVcbeSfxZyrhPz"
consumer_secret="pKhFkXgyjq2VnyQLiUDjXoKOlHhoBRUES4wZ8B4Vd7iPiXDpZY"
access_token="841996330817990656-jssIDx0EdXbEXCVXFNycDvizk57CCUb"
access_token_secret="JfdEOBTdDkeJbrwP0wALOvSswS8ntyPJQfuwg8RJmjN4W"

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
