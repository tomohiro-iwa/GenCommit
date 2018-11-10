#! /usr/bin/python3
import urllib.request as url_req
from bs4 import BeautifulSoup
import sys
import json

def url2soup(url):
	html = url_req.urlopen(url)
	soup = BeautifulSoup(html,"lxml")
	return soup

def get_hash(pull_url):
	try:
		soup = url2soup(pull_url)
	except:
		sys.stderr.write(pull_url)
	clips = soup.select("clipboard-copy")
	result = []
	for clip in clips:
		result.append({"hash":clip.get("value")})
	return result

def main():
	github_url = "https://github.com/"

	data = json.load(open(sys.argv[1]))
	pull_set = set()
	result = {}

	#idのsetを作成
	for issue in data["issues"]:
		for pull in data["issues"][issue]["pulls"]:
			pull_set.add(pull["id"])
	
	for pull in pull_set:
		pull_url = github_url+data["repo_name"]+"/pull/"+pull+"/commits"
		result[pull_url] = get_hash(pull_url)
	
	print(json.dumps(result))

if __name__ == "__main__":
	main()
