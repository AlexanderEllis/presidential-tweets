"""
This reads in json information from the data folder and creates one long string of
all tweets combined together.  The string will then be parsed in generate_chain.py.
"""

import json
import os

def create_tweet_string():
	"""
	This function analyzes the stored json tweet data to create the long sample text
	It opens each json file and adds the text of every tweet to a resulting string
	and then returns that string.
	This function is called by generate_text.py
	"""

	json_files = os.listdir("data")

	resulting_string = ''

	for json_file in json_files:
		path = 'data/' + json_file
		with open(path, 'r') as fp:
			tweets = json.loads(fp.read())
			for i in range(len(tweets)):
				if '"' not in tweets[i]["text"][0]: # No retweets allowed
					resulting_string += tweets[i]["text"].replace('\n', ' ').replace('&amp;', '&') + ' '
		fp.close()

	return resulting_string
