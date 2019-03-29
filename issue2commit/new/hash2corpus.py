#! /usr/bin/python3
import json
import sys
import os
import subprocess

from nltk import tokenize

def get_msg(hash_id):
	cmd = ["git", "log",hash_id,"--pretty=format:%s","-n1"]
	res = subprocess.run(cmd,stdout=subprocess.PIPE)
	return res.stdout.decode("utf8")


def get_diff(hash_id):
	cmd = ["git", "diff","master..."+hash_id]
	res = subprocess.run(cmd,stdout=subprocess.PIPE)
	return res.stdout.decode("utf8")

def main():
	corpus_dir = "corpus/"
	repo = sys.argv[1]
	repo_dir = "repo/"+(repo.split("/")[1])+"/"
	
	data_dir = corpus_dir+repo+"/"
	summary_data = json.load(open(data_dir+"summary.json"))
	body_data = json.load(open(data_dir+"url2body.json"))
	hash_data = json.load(open(data_dir+"hash.json"))
	
	issu = open("issu.txt","a")
	diff = open("diff.txt","a")
	msg = open("msg.txt","a")

	os.chdir(repo_dir)
	
	for issu_url in summary_data["issues"]:
		pull_url = summary_data["repo_url"]+"/pull/"
		for pull_id in summary_data["issues"][issu_url]["pulls"]:
			for one in hash_data[pull_url+pull_id["id"]+"/commits"]:
				issu_str = summary_data["issues"][issu_url]["title"]
				try:
					issu_str += " __EoT__ "+body_data[issu_url]
				except:
					issu_str += " __EoT__ " 
				issu_str = " ".join(tokenize.word_tokenize(issu_str)[:200])
				diff_str = get_diff(one["hash"])
				diff_str = " ".join(tokenize.word_tokenize(diff_str)[:200])
				msg_str = get_msg(one["hash"]) 

				issu.write(issu_str+"\n")
				diff.write(diff_str+"\n")
				msg.write(msg_str+"\n")
	issu.close()
	diff.close()
	msg.close()
	os.chdir("../../")

if __name__ == "__main__":
	main()
