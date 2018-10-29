import urllib.request as url_req
from bs4 import BeautifulSoup
import sys
import json

def url2soup(url):
	html = url_req.urlopen(url)
	soup = BeautifulSoup(html,"lxml")
	return soup

def get_pull(pull_url):
	try:
		soup = url2soup(pull_url)
	except:
		sys.stderr.write(pull_url)
	clips = soup.select("clipboard-copy")
	pull = {}
	pull["id"] = i
	pull["commits"] = []
	for clip in clips:
		one = {}
		one["hash"] = clip.get("value")
		pull["commits"].append(one)
	return pull

if __name__ == "__main__":
	github_url = "https://github.com/"

	data = json.load(open(sys.argv[1]))
	pull_set = set()

	#idのsetを作成
	for issue in data["issues"]:
		for pull in issue["pulls"]:
			pull_set.add(pull["id"])

	data["pulls"] = []
	for i in list(pull_set):
		pull_url = github_url+data["repo_name"]+"/pull/"+i+"/commits"
		pull = get_pull(pull_url)
		data["pulls"].append(pull)

	print(json.dumps(data))

