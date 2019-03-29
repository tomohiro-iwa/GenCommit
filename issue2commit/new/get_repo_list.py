#! /usr/bin/python3
import urllib.request as url_req
import sys
import json
import base64
import time

args = sys.argv

def make_url(page):
	left = "https://api.github.com/search/repositories?q=language:Java&type=Repositories&sort=starts&page="
	return left + str(page)

def api_get(url):
	headers = {"Authorization":"Basic dG9tb2hpcm8taXdhOnRvbW8yNDM2OTk="}
	req = url_req.Request(url,headers=headers)
	res = url_req.urlopen(req)
	return res

def main():
	result = []
	i = 0
	while True:
		i += 1
		url = make_url(i)
		try:
			res = api_get(url)
		except:
			print(url)
			print( json.dumps(result) )

		data = json.loads(res.read().decode("utf-8"))
		result.extend(data["items"])
		if len(data) < 1 or i > 100:
			break
		time.sleep(1)
		
	print( json.dumps(result) )

if __name__ == "__main__":
	main()
	#url = make_url(1)
	#res = api_get(url)
	#data = json.loads(res.read().decode("utf-8"))
	#print(json.dumps(data))
