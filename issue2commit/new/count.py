import json
import re
import sys
from define import url2issueID

def issue_pull():
	# 重複したpullからIssueへのリンクを見たい
	result = {}
	data = json.load(open(sys.argv[1]))
	for issue in data["issues"]:
		for pull in data["issues"][issue]["pulls"]:
			
			if not pull["id"] in result.keys():
				result[pull["id"]] = []
			result[pull["id"]].append(issue)

	print(json.dumps(result))

#def duplication():
	

def same_id():
	# 同じIDのリンクをカウント
	data = json.load(open(sys.argv[1]))
	count = 0
	for pull in data:
			if len(data[pull]) > 1:
				count += 1
	print(count)

if __name__ == "__main__":
	same_id()
