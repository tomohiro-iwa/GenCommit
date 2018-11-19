import json
import sys
import os
from nltk import tokenize

	
def main():
	summary = json.load(open(sys.argv[1]))
	commit = json.load(open(sys.argv[2]))

	issu = open("issu.txt","a")
	diff = open("diff.txt","a")
	msg = open("msg.txt","a")

	for issu_url in summary["issues"]:
		pull_url = summary["repo_url"]+"/pull/"
		for pull_id in summary["issues"][issu_url]["pulls"]:
			for one in commit[pull_url+pull_id["id"]+"/commits"]:

				issu_str = summary["issues"][issu_url]["title"]+"\n"
				diff_str = one["diff"]+"\n"
				msg_str = one["msg"]+"\n"

				if diff_str == "\n":
					continue

				issu.write(issu_str)

				diff_str = " ".join(tokenize.word_tokenize(diff_str)[:200])
				diff.write(diff_str)
				
				msg.write(msg_str)

				
		

if __name__ == "__main__":
	main()
