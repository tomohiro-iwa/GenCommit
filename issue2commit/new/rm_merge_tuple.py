import sys
import re

diff = open("diff.txt")
issu = open("issu.txt")
msg = open("msg.txt")

out_diff = open("diff2.txt","w")
out_issu = open("issu2.txt","w")
out_msg = open("msg2.txt","w")

pattern = re.compile(r"Merge pull request",re.IGNORECASE)

for i,j,k in zip(diff,issu,msg):
	if not pattern.match(k):
		out_diff.write(i)
		out_issu.write(j)
		out_msg.write(k)
