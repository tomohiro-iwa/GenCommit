import sys

data1_hash = []
data1 = {}
for i in open(sys.argv[1]+"/hash_msg.txt"):
	line = i.split(" ___EndOfhash___ ")
	data1[line[0]] = line[1].strip()
	data1_hash.append(line[0])
data2_hash = []

for i in open(sys.argv[1]+"/mrg_hash.txt"):
	data2_hash.append(i.strip())

data1_hash = set(data1_hash)
data2_hash = set(data2_hash)

and12 = data1_hash and data2_hash 
print(and12)

for i in list(and12):
	if i in data1:
		print(data1[i])


