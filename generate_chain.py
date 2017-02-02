
import json
import markov_chain_two


TEXT_SOURCE = open('example-text.txt', 'r')
SAMPLE_TEXT = TEXT_SOURCE.readline()
TEXT_SOURCE.close()

GENERATED_CHAIN = markov_chain_two.generate_markov_chain(SAMPLE_TEXT)

with open('chain_two.json', 'w') as fp:
    json.dump(GENERATED_CHAIN, fp)

fp.close()
