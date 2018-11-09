#! /usr/bin/python3
import urllib.request as url_req
from bs4 import BeautifulSoup
import sys
import re
import json

r_id = re.compile(r"#[0-9]+")

def url2soup(url):
	html = url_req.urlopen(url)
	soup = BeautifulSoup(html,"lxml")
	return soup

def getIDs(url):
	#url <--- issue url
	soup = url2soup(url)
	match_obj = re.search("issues/",url)
	if not match_obj:
		return []
	marg_url = url[:match_obj.end()]
	marg_url = marg_url.replace("issues","pull")
	links = soup.select("a")

	result = set()

	for i in links:
		href = i.get("href")
		match_obj = re.search(marg_url+"[0-9]+",href)
		if match_obj:
			tag = re.search(r"[0-9]+",match_obj.group() ).group()
			result.add(tag)

	#filter
	self_id = re.search(r"[0-9]+",url).group()
	if self_id in result:
		result.remove(self_id)
	
	return list(result)

def main():
	data = json.loads(open(sys.argv[1]).read())

	for issue in data["issues"]:
		id_list = list(getIDs(issue))
		issue["pulls"] = []
		for i in id_list:
			issue["pulls"].append({"id":i})

	print(json.dumps(data))


if __name__ == "__main__":
	main()
	#id_set = getIDs("https://github.com/google/clasp/issues/322")
	#print(list(id_set))

