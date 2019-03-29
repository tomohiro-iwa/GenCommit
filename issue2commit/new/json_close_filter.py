import json
import re
import sys

fix_p = re.compile(r"fix[eds]* #[0-9]+",re.IGNORECASE)
close_p = re.compile(r"close[ds]? #[0-9]+",re.IGNORECASE)
resolv_p = re.compile(r"resolve[ds]? #[0-9]+",re.IGNORECASE)

result = []
for i in json.load(open(sys.argv[1])):
	match_fix = re.search(fix_p,i["msg"])
	match_close = re.search(close_p,i["msg"])
	match_resolve = re.search(resolv_p,i["msg"])
	if match_fix or match_close or match_resolve:
		result.append(i)
print(json.dumps(result))
