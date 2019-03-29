import sys
data1 = set(open(sys.argv[1]).read().strip().split("\n"))
data2 = set(open(sys.argv[2]).read().strip().split("\n"))


print(*list(data1 -data2),sep="\n")


