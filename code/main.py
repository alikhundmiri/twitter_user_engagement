from credentials import *
from requests_oauthlib import OAuth1
import requests

# Global Auth
AUTH = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)


def request_user_id():
	# user_id = input("Please enter the user id: ")
	user_id = "newlifeshoes"
	return(user_id)

def fetch_followers(user_id, count):
	URL = 'https://api.twitter.com/1.1/followers/list.json'
	# URL = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}

	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	
	# print(r)
	# print("\n\n")
	
	# extracting data in json format
	# for some reason i need to add ['users'] in the forloop statement itself. 
	# no idea why it doesnt work like it did in fetch mention timeline
	for tweet in r.json()['users']:
		# print(tweet['screen_name'])
		print(tweet)
	# print("\n")
	# print(r.json())

def fetch_following(user_id, count):
	URL = 'https://api.twitter.com/1.1/friends/list.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}

	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	
	# print(r)
	# print("\n\n")
	
	# extracting data in json format
	# for some reason i need to add ['users'] in the forloop statement itself. 
	# no idea why it doesnt work like it did in fetch mention timeline
	for tweet in r.json()['users']:
		print(str(tweet['screen_name']) +"  -  "+ str(tweet['location']))
		# print(tweet)
	# print("\n")
	# print(r.json())

# returns a bunch of numbers, which are IDs
def fetch_followers_id(user_id, count):
	URL = 'https://api.twitter.com/1.1/followers/ids.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}

	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	
	# print(r)
	# print("\n\n")
	
	# extracting data in json format
	for tweet in r.json()['ids']:
		# print(tweet['screen_name'])
		print(tweet)
	# print("\n")
	# print(r.json())


# This fetches tweet replies with you mentioned in it!
def fetch_mention_timeline(user_id, count):
	URL = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	# extracting data in json format
	for tweet in r.json():
		# first get the person who tweeted this, then fetch the tweet text
		print(str(tweet['user']['screen_name']) +" - tweeted\n\n\t"+ str(tweet["text"]))
		# print(tweet)
		print('\n')



"""


ok, if you ignore all 
tweet['in_reply_to_screen_name'] == None , and
tweet['in_reply_to_screen_name'].lower() == user_id.lower()

this will leave you with the tweets which are replies, retweets. The metric we need to examine user activity.
"""

def fetch_user_timeline(user_id, count):
	URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	# extracting data in json format
	for tweet in r.json():
		if tweet['in_reply_to_screen_name'] == None or tweet['in_reply_to_screen_name'].lower() == user_id.lower():
			pass
		else:
			# print(tweet['user']['screen_name'])
			print(str(tweet['user']['screen_name']) +" -in reply to "+ str(tweet['in_reply_to_screen_name'])+"  tweeted \n\n"+ str(tweet["text"]))
			# print(tweet)
			print('\n--------------------------------------------\n')



def fetch_user_timeline_test(user_id, count):
	URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
	PARAMS = {
		'screen_name':user_id,
		'count': count}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS, auth=AUTH)
	# extracting data in json format
	for tweet in r.json():
		# print(tweet['user']['screen_name'])
		print(str(tweet['user']['screen_name']) +" -in reply to "+ str(tweet['in_reply_to_screen_name'])+"  tweeted \n\n"+ str(tweet["text"]))
		# print(tweet)
		print('\n--------------------------------------------\n')


def main():
	print('\n============================================\n')
	user_id = request_user_id()
	# fetch_following(user_id, 10)
	# fetch_followers(user_id, 5)
	# fetch_followers_id(user_id, 5)
	# fetch_mention_timeline(user_id, 5)
	# fetch_user_timeline(user_id, 10)
	fetch_user_timeline_test(user_id, 10)

if __name__ == '__main__':
	main()
	# ask for user id

