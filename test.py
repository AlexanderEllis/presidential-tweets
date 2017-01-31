from markov_chain import *
from generate_text import *

f = open('example-text.txt', 'r')
sample_text = f.readline()

generated_chain = generate_markov_chain(sample_text)
result = generate_text(generated_chain)

print(result)
