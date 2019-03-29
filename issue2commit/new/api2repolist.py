import json

data = json.load(open("hoge"))

for i in data:
	print(i["full_name"])
