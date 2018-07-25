import json

f = open("result.txt")
data = json.load(f)

for i in data["items"]:
	print(i["url"])
