import re

def msg2tag(msg):
	id_match = re.search("#[0-9]+",msg)
	if id_match:
		tag = id_match.group()
		return tag.replace("#","")
	else:
		return ""

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

