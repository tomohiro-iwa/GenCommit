import sys

def count_lines(path):
    with open(path) as f:
        return sum([1 for _ in f])

data_dir = "corpus/"+sys.argv[1]
count = 0


issu = open(data_dir+"/issu.txt","r").read().split("\n")
diff = open(data_dir+"/diff.txt","r").read().split("\n")
msg = open(data_dir+"/msg.txt","r").read().split("\n")
#print(len(diff))
#print(len(issu))
#print(len(msg))
#quit()
if True :#len(diff) == len(issu) == len(msg) and len(diff) != 0:
	out_issu = open("issu.txt","a")
	out_diff = open("diff.txt","a")
	out_msg = open("msg.txt","a")

	for i in range(len(diff)):
		if issu[i] != "" and diff[i] != "" and msg[i]!="":
				out_issu.write(issu[i]+"\n")
				out_diff.write(diff[i]+"\n")
				out_msg.write(msg[i]+"\n")
else:
	print(sys.argv[1])
