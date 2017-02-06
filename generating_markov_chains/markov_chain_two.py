"""
This module is for generating a Markov chain order two from a text.
"""

def generate_markov_chain(tweet_array):
	"""
	Input assumes text is an array of tweets, each tweet with words separated by spaces with no new lines.
	This requires some changes to most transcripts ahead of time. Output will be a dictionary
	with each pair of words that exists in the text as a key and a list of words that follow
	that pair as the value.
	"""
	tweets_copy = tweet_array[:]

	markov_chain = {}

	for tweet in tweets_copy:

		word_array = tweet.split()

		for i in range(len(word_array) - 2): # - 2 to not  analyze the last word as first in pair
			first_word = strip_word(word_array[i])
			second_word = strip_word(word_array[i + 1])
			third_word = strip_word(word_array[i + 2])

			pair = first_word + ' ' + second_word

			if pair not in markov_chain:
				markov_chain[pair] = [third_word]
			else:
				markov_chain[pair].append(third_word)

	return markov_chain

def strip_word(string):
	"""
	This function strips the words of any surrounding spaces or quotation marks from an input string,
	but does not replace any single quotes inside words (e.g. "isn't")
	"""
	return string.strip().strip("'").strip('"')