"""
This file generates the Markov chains.  It uses analyze_data to create a string of all
tweets, creates the order 2 chain, and finally creates the order 1 chain.
"""

import json
from generating_markov_chains import analyze_data
from generating_markov_chains import markov_chain_two
from generating_markov_chains import markov_chain

SAMPLE_TEXT = analyze_data.create_tweet_string()

GENERATED_CHAIN = markov_chain_two.generate_markov_chain(SAMPLE_TEXT)

with open('markov_chains/chain_two.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)
fp.close()

GENERATED_CHAIN = markov_chain.generate_markov_chain(SAMPLE_TEXT)

with open('markov_chains/chain_one.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)
fp.close()
