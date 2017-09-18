import tweepy

credentials = {}
with open('credentials.txt') as inputfile:
    for line in inputfile:
    	key, value = line.strip().split('=')
    	credentials[key] = value

auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth)

api.update_status('test')
