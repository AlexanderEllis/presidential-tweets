"""
This file will import the two existing Markov chains and generate a text based off
of them.  The first is a Markov chain order 2, and the second is a Markov chain
order 1.
"""

import json
import generate_text

with open('markov_chains/chain_two.json', 'r') as fp:
    TWO_WORD_CHAIN = json.load(fp)
fp.close()

with open('markov_chains/chain_one.json', 'r') as fp:
    ONE_WORD_CHAIN = json.load(fp)
fp.close()


RESULT = generate_text.generate_text(TWO_WORD_CHAIN, ONE_WORD_CHAIN)

print(RESULT)
