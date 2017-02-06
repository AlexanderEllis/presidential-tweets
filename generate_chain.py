
import json
import analyze_data
import markov_chain
import markov_chain_two

SAMPLE_TEXT = analyze_data.create_tweet_string()

GENERATED_CHAIN = markov_chain_two.generate_markov_chain(SAMPLE_TEXT)

with open('markov_chains/chain_two.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)
fp.close()

GENERATED_CHAIN = markov_chain.generate_markov_chain(SAMPLE_TEXT)

with open('markov_chains/chain_one.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)
fp.close()
