"""
This module is for generating a Markov chain with length two from a text.
"""

def generate_markov_chain(text):
	"""
	Input assumes text is a long string with words separated by spaces with no new lines.
	This requires some changes to most transcripts ahead of time. Output will be a dictionary
	with each pair of words that exists in the text as a key and a list of words that follow
	that pair as the value.
	"""
	text_copy = text[:]
	word_array = text_copy.split(" ")

	markov_chain = {}

	for i in range(len(word_array) - 2): # - 2 to not  analyze the last word as first in pair
		pair = word_array[i] + ' ' + word_array[i + 1]
		if pair not in markov_chain:
			markov_chain[pair] = [word_array[i + 2]]
		else:
			markov_chain[pair].append(word_array[i + 2])

	return markov_chain
