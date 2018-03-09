# sentiment analysis
# 1. get a string
# 2. break it up into subjects, verbs, objects, etc. through tokenization
# 3. bag of words model
# 4. use sentiment lexicon to determine weight of each word

# steps in advance
# 1. register for Twitter's API
# 2. install dependencies
# 3. write the script

# dependencies install:
# sudo pip install tweepy textblob, can use .tags, .polarity, .words
# python -m textblob.download_corpora

import tweepy
from textblob import TextBlob

# twitter api credentials
consumer_key = ':)'
consumer_secret = ':)'
access_token = ':)'
access_token_secret = ':)'

# auth with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create bridge to api
api = tweepy.API(auth)

# look for tweets related to a topic
public_tweets = api.search('Trump')

# iterate through all tweets
for tweet in public_tweets:
    # print the tweet as plain text
    print tweet.text

    # analyze string
    analysis = TextBlob(tweet.text)

    # print string sentiment attribute
    # polarity: how positive or negative it is
    # subjectivity: how much of an opinion it is
    print(analysis.sentiment)
