
import json
import markov_chain


TEXT_SOURCE = open('example-text.txt', 'r')
SAMPLE_TEXT = TEXT_SOURCE.readline()
TEXT_SOURCE.close()

GENERATED_CHAIN = markov_chain.generate_markov_chain(SAMPLE_TEXT)

with open('chain.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)

fp.close()
