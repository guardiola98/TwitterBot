import tweepy

f= open("variables.txt", "r")
lineas = f.readlines()

print(lineas)
consumer_key = lineas[0].rstrip()
consumer_secret = lineas[1].rstrip()
access_token = lineas[2].rstrip()
access_token_secret = lineas[3].rstrip()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status('Hoola')