import tweepy
import time
auth = tweepy.OAuthHandler('FVLo08sCQXkS45673plYp5pEx', 'Uo1teC7Hm7xtUJFBV3847GBF3489G90u004CHTxVFppzDfMlRH9jGDC3Jl')
auth.set_access_token('1246459420197949440-PfQN8kfz43456S8k2aftQUOvGh9alB', 'c0hPTtndB04CnACUIRGB853468GVBOVmRL5NY45JNAxA9uxD')

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
