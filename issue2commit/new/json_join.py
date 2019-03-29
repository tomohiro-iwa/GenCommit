import json 
import glob

result = {}

file_list = glob.glob("test_corpus/*/commit.json")

isuu = open("issu.txt")
diff = open("diff.txt")
msg = open("msg.txt")

for i in file_list:
	try:
		#result.update(json.load(open(i)))
		pass
	except:
		pass

data = json.load(open(file_list[0]))
for i in data:
	data[i]
