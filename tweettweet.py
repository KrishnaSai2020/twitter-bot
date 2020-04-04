import tweepy

auth = tweepy.OAuthHandler('FVLo08sCQXkS5onU4plYp5pEx', 'Uo1teC7Hm7xtU1yBv7PbsT0u004CHTxVFppzDfMlRH9jGDC3Jl')
auth.set_access_token('1246459420197949440-PfQN8kfz40Ni8S8k2aftQUOvGh9al3', 'c0hPTtndB04CnAejqAMQ8Ufj6hJ8mRL5NY45JNAxA9uxD')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)