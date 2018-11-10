#! /usr/bin/python3
import urllib.request as url_req
import sys
import json
import base64

args = sys.argv

def make_url(repo,page):
	left = "https://api.github.com/repos/"
	right = "/issues?state=closed&page="
	return left + repo + right + str(page)

if __name__ == "__main__":
	result = []

	for i in range(100):
		url = make_url(args[1],i+1)
		headers = {"Authorization":"Basic dG9tb2hpcm8taXdhOnRvbW8yNDM2OTk="}
		req = url_req.Request(url,headers=headers)
		res = url_req.urlopen(req)
		data = json.loads(res.read().decode("utf-8"))
		if len(data) < 1:
			break
		result.extend(data)
	print( json.dumps(result) )

