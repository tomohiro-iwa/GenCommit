#! /usr/bin/python3
import urllib.request as url_req
import sys
import json
import base64
import time

args = sys.argv

def make_url(repo,page):
	left = "https://api.github.com/repos/"
	right = "/issues?state=closed&page="
	return left + repo + right + str(page)

if __name__ == "__main__":
	result = []
	i = 0
	while True:
		i += 1
		url = make_url(args[1],i)
		headers = {"Authorization":"Basic dG9tb2hpcm8taXdhOnRvbW8yNDM2OTk="}
		req = url_req.Request(url,headers=headers)
		res = url_req.urlopen(req)
		data = json.loads(res.read().decode("utf-8"))
		time.sleep(1)
		if len(data) < 1:
			break
		result.extend(data)
	print( json.dumps(result) )

