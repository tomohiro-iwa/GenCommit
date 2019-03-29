#! /usr/bin/python3
import sys
import re
import json

sharp_num = re.compile(r"#[0-9]+")
data = []
msg_file = open(sys.argv[1]+"/msg.txt")
api_file = open(sys.argv[1]+"/api.json")
id2issue = {}
for i in json.load(api_file):
	issue_id = str(i["number"])
	body = str(i["body"])
	issue_txt = i["title"] + " __EoT__ " + body
	id2issue[issue_id] = issue_txt

for line in msg_file:
	msg = line.strip()

	tag_match = re.search(sharp_num,msg)
	if tag_match:
		issue_id = tag_match.group().replace("#","")
		try:
			issue = id2issue[issue_id]
		except:
			continue
		one = {"msg":msg, "issue":issue}
		data.append(one)

print(json.dumps(data))
