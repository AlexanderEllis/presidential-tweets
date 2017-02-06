"""
This module is for generating a Markov chain order one from a text.
"""

def generate_markov_chain(text):
	"""
	Input assumes text is a long string with words separated by spaces with no new lines.
	This requires some changes to most transcripts ahead of time. Output will be a dictionary
	with each word as a key and a list of words that follow that word as the value. For a
	basic model, I won't calculate percentages for each word, but will instead rely on
	accessing a random index when I use the chain later. For a basic version, I'm creating
	a Markov chain of order 1 for now
	"""
	text_copy = text[:]
	word_array = text_copy.split()

	markov_chain = {}

	for i in range(len(word_array) - 1): # - 1 to not  analyze the last word
		first_word = strip_word(word_array[i])
		second_word = strip_word(word_array[i + 1])
		if first_word not in markov_chain:
			markov_chain[first_word] = [second_word]
		else:
			markov_chain[first_word].append(second_word)

	return markov_chain

def strip_word(string):
	"""
	This function strips the words of any surrounding spaces or quotation marks from an input string,
	but does not replace any single quotes inside words (e.g. "isn't")
	"""
	return string.strip().strip("'").strip('"')