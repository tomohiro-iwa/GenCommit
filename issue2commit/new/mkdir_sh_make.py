repo_list = open("repo_list.txt").read().split("\n")
for i in repo_list:
	print("./get_issue_list.py " + i[1:] + " > corpus/"+i[1:]+"/api.json")
