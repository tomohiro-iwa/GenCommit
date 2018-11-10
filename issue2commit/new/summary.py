#! /usr/bin/python3
import urllib.request as url_req
from bs4 import BeautifulSoup
import sys
import re
import json

def url2ID(url,key="/pull/"):
	id_match = re.search(key+"[0-9]+",url)
	if id_match:
		tag = id_match.group()
		return tag.replace(key,"")
	else:
		return ""

def url2pullID(url):
	return url2ID(url,"/pull/")

def url2issueID(url):
	return url2ID(url,"/issues/")

def drip(data):
	issues = {}
	pulls = {}

	for i in data:
		url = i["html_url"]
		title = i["title"]
		if "/issues/" in url:
			issues[url] = {"title":title}
		if "/pull/" in url:
			pulls[url] = {"title":title}

	return issues,pulls

def url2soup(url):
	html = url_req.urlopen(url)
	soup = BeautifulSoup(html,"lxml")
	return soup

def issue2pull(url):
	match_obj = re.search("/issues/",url)
	marg_url = url[:match_obj.end()]
	marg_url = marg_url.replace("issues","pull")
	return marg_url

def getIDs(url):
	#url <--- issue url
	soup = url2soup(url)

	links = soup.select("a")
	result = set()

	marg_url = issue2pull(url)

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
	api_json = json.load(open(sys.argv[1]))
	data = {}
	data["error"] = []
	rm_str = "https://api.github.com/repos/"
	data["repo_name"] = api_json[0]["repository_url"].replace(rm_str,"")
	data["repo_url"] = "https://github.com/"+data["repo_name"]

	data["issues"],data["pull"] = drip(api_json)

	for issue in data["issues"]:
		data_ptr = data["issues"][issue]
		id_list = getIDs( issue )

		data_ptr["pulls"] = []
		for i in id_list:
			data_ptr["pulls"].append({"id":i})
	
	for pull in data["pull"]:
		data_ptr = data["pull"][pull]
		tag_match = re.search("#[0-9]+",data_ptr["title"])
		if tag_match:
			issue_id = tag_match.group().replace("#","")
			issue_url = data["repo_url"]+"/issues/"+issue_id
			pull_id = url2pullID(pull)
			try:
				pull_list = []
				for i in data["issues"][issue_url]["pulls"]:
					pull_list.append(i["id"])
				if not  pull_id in pull_list:
					data["issues"][issue_url]["pulls"].append({"id":pull_id})
			except:
				data["error"].append({"url":issue_url})
	
	print( json.dumps(data) )


if __name__ == "__main__":
	main()
