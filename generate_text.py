# Generating the text using a markov chain

import random

def generate_text(markov_chain):
	"""
	Given a Markov chain as an input, this will generate a sample text.  It currently assumes the chain is length 1.  For a starting word, it randomly selects a word until it finds one with a period at the end, then it selects a random following word to ensure that the first word will be the start of a new sentence.
	"""

	resulting_text = []

	found_first = False
	length = len(markov_chain)

	while not found_first:

		next_word = random.choice(list(markov_chain.keys())) 
		if next_word != '' and next_word != '\n' and  next_word[0].isupper():
			found_first = True

	while len(resulting_text) < 30 or resulting_text[len(resulting_text) - 1][-1] != '.':
		resulting_text.append(next_word)
		next_word = find_next_word(next_word, markov_chain)

	return ' '.join(resulting_text)

def find_next_word(input_word, markov_chain):
	array_of_words = markov_chain[input_word]
	random_index = random.randint(0, len(array_of_words) - 1) # -1 because randint can return the high value
	selected_word = array_of_words[random_index]
	return selected_word