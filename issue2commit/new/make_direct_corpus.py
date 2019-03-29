#! /usr/bin/python3
import json
import sys
import os
import subprocess

from nltk import tokenize

def get_diff(hash_id):
	cmd = ["git", "diff",hash_id]
	res = subprocess.run(cmd,stdout=subprocess.PIPE)
	return res.stdout.decode("utf8")

def main():
	corpus_dir = "corpus/"
	repo = sys.argv[1]
	repo_dir = "repo100/"+(repo.split("/")[1])+"/"
	
	data_dir = corpus_dir+repo+"/"
	msg2issue = json.load(open(data_dir+"msg2issue.json"))
	
	issu = open(data_dir+"issu.txt","w")
	diff = open(data_dir+"diff.txt","w")
	msg = open(data_dir+"msg.txt","w")

	os.chdir(repo_dir)

	for i in msg2issue:
		diff_str = get_diff(i["hash"])
		diff_str = " ".join(tokenize.word_tokenize(diff_str)[:200])
		issu_str = " ".join(tokenize.word_tokenize(i["issue"])[:200])

		issu.write(issu_str+"\n")
		diff.write(diff_str+"\n")
		msg.write(i["msg"]+"\n")
	issu.close()
	diff.close()
	msg.close()
	os.chdir("../../")

if __name__ == "__main__":
	main()
