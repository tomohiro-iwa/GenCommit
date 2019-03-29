import sys
f = open(sys.argv[1])
num = int(sys.argv[2])
out = open("diff3.txt","w")

for line in f:
	line = line.replace("\n","")
	words = line.split(" ")
	out.write(" ".join(words[:num])+"\n")
