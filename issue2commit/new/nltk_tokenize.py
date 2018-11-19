import sys
import nltk
from nltk import tokenize

for i in sys.stdin:
	tokens = tokenize.word_tokenize(i)
	print(tokens)
