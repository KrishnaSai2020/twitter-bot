import tweepy
import time
auth = tweepy.OAuthHandler('FVLo08sCQXkS5onU4plYp5pEx', 'Uo1teC7Hm7xtU1yBv7PbsT0u004CHTxVFppzDfMlRH9jGDC3Jl')
auth.set_access_token('1246459420197949440-PfQN8kfz40Ni8S8k2aftQUOvGh9al3', 'c0hPTtndB04CnAejqAMQ8Ufj6hJ8mRL5NY45JNAxA9uxD')

api = tweepy.API(auth)
user = api.me()


def limit_handel(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    except StopIteration:
        print('you have no followers')


for follower in limit_handel(tweepy.Cursor(api.followers).items()):
    follower.follow()

search_string = 'python'
num_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(2):
    try:
        tweet.favorite()
        print('I liked that tweet ')
    except StopIteration:
        print('no tweets available')
