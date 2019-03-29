#! /usr/bin/python3
import sys
import re
import json
import random

data = json.load(open(sys.argv[1]))
random.shuffle(data)
print(json.dumps(data))
