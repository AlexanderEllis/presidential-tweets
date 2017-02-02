"""
This module is for generating the markov chain from a text.
"""

def generate_markov_chain(text):
	"""
	Input assumes text is a long string with words separated by spaces with no new lines.
	This requires some changes to most transcripts ahead of time. Output will be a dictionary
	with each word as a key and a list of words that follow that word as the value. For a
	basic model, I won't calculate percentages for each word, but will instead rely on
	accessing a random index when I use the chain later. For a basic version, I'm creating
	a Markov chain of length 1 for now
	"""
	text_copy = text[:]
	word_array = text_copy.split(" ")

	markov_chain = {}

	for i in range(len(word_array) - 1): # - 1 to not  analyze the last word
		if word_array[i] not in markov_chain:
			markov_chain[word_array[i]] = [word_array[i + 1]]
		else:
			markov_chain[word_array[i]].append(word_array[i + 1])

	return markov_chain
