import os
import glob

if __name__ == "__main__":
	repo_list = glob.glob("repositorys/*")
	for repo in repo_list:
		os.mkdir("corpus/"+repo.split("/")[-1])
		

