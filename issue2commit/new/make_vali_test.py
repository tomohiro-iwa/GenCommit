import sys
import random

def count_lines(path):
    with open(path) as f:
        return sum([1 for _ in f])

i0 = open("diff2.txt")
i1 = open("issu2.txt")
i2 = open("msg2.txt")

valid0 = open("diff.valid.txt","w")
valid1 = open("issu.valid.txt","w")
valid2 = open("msg.valid.txt","w")

test0 = open("diff.test.txt","w")
test1 = open("issu.test.txt","w")
test2 = open("msg.test.txt","w")

train0 = open("diff.train.txt","w")
train1 = open("issu.train.txt","w")
train2 = open("msg.train.txt","w")

valid_n = int(sys.argv[1])
test_n = int(sys.argv[2])

all_num = range(count_lines("msg2.txt"))

drip = random.sample(all_num,valid_n+test_n)

drip_valid = drip[:valid_n]
drip_test = drip[valid_n:]

count = 0
for i,j,k in zip(i0,i1,i2):
	if count in drip_valid:
		valid0.write(i)
		valid1.write(j)
		valid2.write(k)
	elif count in drip_test:
		test0.write(i)
		test1.write(j)
		test2.write(k)
	else:
		train0.write(i)
		train1.write(j)
		train2.write(k)
	count +=1
		
