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


for follower in limit_handel(tweepy.Cursor(api.followers).items()):
    follower.follow()
