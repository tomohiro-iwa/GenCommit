import json
import sys

data = json.load(open(sys.argv[1]))
result = {}
for i in data:
	url = i["html_url"]	
	if not "issue" in url:
		continue
	body = i["body"]
	result[url] = body
print(json.dumps(result))

	


