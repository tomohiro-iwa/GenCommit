import sys
import json
import random

from nltk.translate import bleu_score

def get_bleu(a,b):
	bleu = bleu_score.sentence_bleu(
        	[a.split(" ")], b.split(" "),
        	smoothing_function=bleu_score.SmoothingFunction().method1)
	return bleu

skip = True

data_m = open(sys.argv[1]).read().strip().split("\n")
data_i = open(sys.argv[2]).read().strip().split("\n")
num = list(range(len(data_m)))
sample = [random.sample(num,2) for i in range(100000)]

msg = [None,None]
issue = [None,None]
for i in sample:
	msg[0] = data_m[i[0]]
	msg[1] = data_m[i[1]]

	issue[0] = " ".join(data_i[i[0]].split(" ")[:200])
	issue[1] = " ".join(data_i[i[1]].split(" ")[:200])

	msg_bleu = get_bleu(msg[0], msg[1])
	issue_bleu = get_bleu(issue[0], issue[1])
	print(msg_bleu , issue_bleu , sep=",")
