#! /usr/bin/python3
import urllib.request as url_req
import sys
import json

args = sys.argv

def make_url(repo,page):
	left = "https://api.github.com/repos/"
	right = "/issues?state=closed&page="
	return left + repo + right + str(page)

if __name__ == "__main__":
	result = {}
	result["repo_name"] = args[1]
	result["issues"] = []

	for i in range(60):
		url = make_url(args[1],i+1)
		res = url_req.urlopen(url)
		data = json.loads(res.read().decode())
		if len(data) < 1:
			break
		for j in data:
			one = {}
			one["title"] = j["title"]
			one["url"] = j["html_url"]
			result["issues"].append(one)
	print( json.dumps(result) )

