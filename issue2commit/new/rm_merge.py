import json
import sys
import re

data = []
pattern = re.compile(r"Merge pull request",re.IGNORECASE)
for i in json.load(open(sys.argv[1])):
	if pattern.match(i["msg"]):
		continue
	else:
		data.append(i)
print(json.dumps(data))
