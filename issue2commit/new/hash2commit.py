
import json
import sys
import subprocess
import os

def get_commit_msg(hash_id):
	cmd = ["git", "log",hash_id,"--pretty=format:%s","-n1"]
	res = subprocess.run(cmd,stdout=subprocess.PIPE)
	return res.stdout.decode("utf8")


def get_diff(hash_id):
	cmd = ["git", "diff","master..."+hash_id]
	res = subprocess.run(cmd,stdout=subprocess.PIPE)
	return res.stdout.decode("utf8")

def main():
	repo_name = sys.argv[1]

	hash_path = "test_corpus/"+repo_name+"/hash.json"
	hash_data = json.load(open(hash_path))

	summary_path = "test_corpus/"+repo_name+"/summary.json"
	summary_data = json.load(open(summary_path))

	os.chdir("repo/"+repo_name)
	result = {}

	for i in hash_data:
		result[i] = {}
		result[i]["commits"] = []
		for j in hash_data[i]:
			one = {}
			one["msg"] = get_commit_msg(j["hash"])
			one["diff"] = get_diff(j["hash"])
			result[i]["commits"].append(one)

	for i in summary_data["issues"]:
		for j in summary_data["issues"][i]["pulls"]:
			pull_url = summary_data["repo_url"]+"/pull/"+j["id"]+"/commits"
			issue = summary_data["issues"][i]["title"]
			result[pull_url]["issue"]=issue

	print(json.dumps(result))


if __name__ == "__main__":
	main()
