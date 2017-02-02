"""
This file will import the two existing Markov chains and generate a text based off
of them.  The first is a Markov chain of length 2, and the second is a Markov chain
of length 1.
"""

import json
import generate_text

with open('chain_two.json', 'r') as fp:
    TWO_WORD_CHAIN = json.load(fp)
fp.close()

with open('chain.json', 'r') as fp:
    ONE_WORD_CHAIN = json.load(fp)
fp.close()


RESULT = generate_text.generate_text(TWO_WORD_CHAIN, ONE_WORD_CHAIN)

print(RESULT)
