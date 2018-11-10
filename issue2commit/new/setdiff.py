#! /usr/bin/python3
import sys
set1 = set(open(sys.argv[1]).read().split("\n"))
set2 = set(open(sys.argv[2]).read().split("\n"))

print( *list(set1-set2),sep="\n" )
