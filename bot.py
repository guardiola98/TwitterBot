import tweepy
from random import randrange
from os import listdir
from os.path import isfile, join

def bot_random_image():
    mypath = "static/images"
    path = generate_path(mypath)
    bot.api.update_with_media(path, status="")

def generate_path(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    nombre = onlyfiles[randrange(len(onlyfiles[1]))]
    return mypath + "/" + nombre  


class Bot:
    def __init__(self, keysFile):
        f= open(keysFile, "r")
        lineas = f.readlines()
        self.consumer_key = lineas[0].rstrip()
        self.consumer_secret = lineas[1].rstrip()
        self.access_token = lineas[2].rstrip()
        self.access_token_secret = lineas[3].rstrip()
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

bot=Bot("variables.txt")
bot_random_image() 


    








