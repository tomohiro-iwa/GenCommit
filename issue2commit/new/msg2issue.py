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

#print(json.dumps(id2issue))
id_list2 = []
for line in msg_file:
	line = line.strip()
	hash_msg = line.split(" ___EndOfhash___ ")
	hash_id = hash_msg[0]
	msg = hash_msg[1]

	tag_match = re.search(sharp_num,msg)
	if tag_match:
		issue_id = tag_match.group().replace("#","")
		id_list2.append(issue_id)
		try:
			issue = id2issue[issue_id]
		except:
			continue
		one = {"msg":msg, "issue":issue,"hash":hash_id}
		data.append(one)

print(json.dumps(data))
