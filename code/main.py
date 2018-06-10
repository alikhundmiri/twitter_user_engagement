from credentials import *
import requests


def request_user_id():
	user_id = input("Please enter the user id: ")
	return(user_id)

def fetch_followers(user_id):
	URL = 'https://api.twitter.com/1.1/followers/list.json'
	PARAMS = {'screen_name':user_id}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	 
	# extracting data in json format
	data = r.json()
	print(data)


def main():
	user_id = request_user_id()
	fetch_followers(user_id)
	# print(consumer_key)
	# print(consumer_secret)

if __name__ == '__main__':
	main()
	# ask for user id

