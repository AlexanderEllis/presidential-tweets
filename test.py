import json
from markov_chain import *
from generate_text import *

with open('chain.json', 'r') as fp:
    generated_chain = json.load(fp)

result = generate_text(generated_chain)

print(result)