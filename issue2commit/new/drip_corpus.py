import sys
import json


data_dir = "corpus2/"+sys.argv[1]


data = json.load(open(data_dir+"/corpus.json","r"))

out_issu = open("issu.txt","a")
out_diff = open("diff.txt","a")
out_msg = open("msg.txt","a")

for i in data:
	out_issu.write(i["issu"]+"\n")
	out_diff.write(i["diff"]+"\n")
	out_msg.write(i["msg"]+"\n")
