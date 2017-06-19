import tweepy
import time
# this is for
# import spacy
# nlp = spacy.load('en')

# twitter app keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# authourization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# handle limits and errors specific to rate limits
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

# fetches everything based on a specific user timeline
for status in limit_handled(tweepy.Cursor(api.user_timeline, id="twitter_handle").items()):
    # prints out the text
    print "--:"+status.text
