#! /usr/bin/env python3

import json
import tweepy 
import time
try:
	from tweepy import OAuthHandler
	from tweepy import Stream 
	from tweepy .streaming import StreamListener 
except ImportError:
	print('Tweepy is not installed')

#open twitter connection
with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

print("-------------------------------------------")
print("\n")
print("connexion OK")
print("-------------------------------------------")
print("\n")

#Flux fonctions 
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


#Listener 
class TweetListener(StreamListener): 
	#le listener traite les tweets reçu du stream 
	def on_data(self, data):
		print(data) 
		return True 
	
	def on_error(self, data):
		print(status) 


TwitterStream = Stream(auth, TweetListener())


#hashtag def 
hashtag1 = "mazagan"
hashtag2 = "mazagao"

maximum_number_of_tweets_to_be_extracted = 10000

#test de sleep sur twitter 
#c = tweepy.Cursor(api.search, q=search, include_entities=True).items()

while True : 
	try : 
		#extract first hashtag and load into a txt file 
		for tweet in tweepy.Cursor(api.search, q='#' + hashtag1, rpp=100).items(maximum_number_of_tweets_to_be_extracted):
			with open('TEST_WithSleep_tweets_with_hashtag_' + hashtag1 + '.txt', 'a') as the_file: 
				the_file.write(str(tweet.text))

		print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) + ' tweets with hashtag #' + hashtag1)
		
		
		#extract second hashtag and load into a txt file
		for tweet in tweepy.Cursor(api.search, q='#' + hashtag2, rpp=100).items(maximum_number_of_tweets_to_be_extracted):
			with open('tweets_with_hashtag_' + hashtag2 + '.txt', 'a') as the_file:
				the_file.write(str(tweet.text))

		print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) + ' tweets with hashtag #' + hashtag2)

	except tweepy.TweepError :
		time.sleep(60 * 15)
		print("Twitter API error | Attente")
		continue 
		
	except StopIteration : 
		break 

