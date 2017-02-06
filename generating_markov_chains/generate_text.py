"""
This module generates the resulting text from a Markov chain.  It uses
a basic random search for a word with the first letter capitalized to
find the first word, then it repeatedly finds the next word until the
desired length is met.
"""

import random

def generate_text(two_word_chain, one_word_chain):
	"""
	Given a Markov chain as an input, this will generate a sample text.
	This function will first check to see if the word and the one before
	it exist in the order 2 chain, but if not, it will then check for the
	word in the second chain.
	"""

	resulting_text = []
	char_count = 0
	punctuation = ['.', '!', '?', '...']
	end_punctuation = punctuation[random.randint(0, 3)]
	tweet_length = random.randint(60, 140)
	found_first = False

	while not found_first:

		next_word = random.choice(list(one_word_chain.keys()))
		if next_word != '' and next_word != '\n' and  next_word[0].isupper():
			found_first = True

	while char_count < tweet_length - len(next_word) - len(end_punctuation):
		resulting_text.append(next_word)
		char_count += len(next_word)

		if len(resulting_text) > 1:
			word_before = resulting_text[-1]
		else:
			word_before = ''
		next_word = find_next_word(next_word, word_before, two_word_chain, one_word_chain)

	return ' '.join(resulting_text) + end_punctuation

def find_next_word(input_word, word_before, two_word_chain, one_word_chain):
	"""
	Given an existing word, this function accesses the Markov chain values
	for that word and selects a random word from that list.  The probability
	distribution mimics storing a probability for each word.
	Given that Trump often ends his tweets with links, I also included a random word
	if the input word isn't in either of our chains.
	"""
	pair = input_word + ' ' + word_before
	
	if pair in two_word_chain:
		array_of_words = two_word_chain[pair]
	elif input_word in one_word_chain:
		array_of_words = one_word_chain[input_word]
	else:
		array_of_words = [random.choice(list(one_word_chain.keys()))]
	random_index = random.randint(0, len(array_of_words) - 1)
	selected_word = array_of_words[random_index]
	return selected_word
