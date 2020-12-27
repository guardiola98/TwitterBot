import tweepy
from random import randrange
from os import listdir
from os.path import isfile, join

def bot_random_image():
    f= open("variables.txt", "r")
    lineas = f.readlines()
    consumer_key = lineas[0].rstrip()
    consumer_secret = lineas[1].rstrip()
    access_token = lineas[2].rstrip()
    access_token_secret = lineas[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    mypath = "static/images"
    path = generate_path(mypath)
    api.update_with_media(path, status="")

def generate_path(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    nombre = onlyfiles[randrange(len(onlyfiles[1]))]
    return mypath + "/" + nombre  

bot_random_image() 


    








