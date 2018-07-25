import glob

replace_list=(
("\n"," <BR> "),
("(","( "),
(")"," )"),
("."," . "),
("/"," / "),
(","," , ")#正規表現　a-zなどなど
)

def corpus_filter(corpus_str):
	#for line in corpus_str.split("\n"):
	for i in replace_list:
		corpus_str = corpus_str.replace(i[0],i[1])
	return corpus_str
			
def line_generator(gitlog):
	corpus_str = ""
	is_first = True
	for line in gitlog:
		if line[0:7] == "!!!!!!!":
			if not is_first:
				yield corpus_filter(corpus_str)
				corpus_str = ""
			else:
				is_first = False
			yield line[7:-1]
		else:
			corpus_str += line
			
def make_corpus(repo_name,log_dir,result_dir):

	print(log_dir+repo_name+"mygitlogdata.txt")
	gitlog = open(log_dir+repo_name+"mygitlogdata2.txt")
	commit = open(result_dir+repo_name+"commit_message.txt","a")
	diff = open(result_dir+repo_name+"diff.txt","a")

	log_lines = line_generator(gitlog)
	is_odd = True
	for line in log_lines:
		if is_odd:
			commit.write(line+"\n") 
		else:
			diff.write(line+"\n")
		is_odd = not is_odd

	commit.close()
	diff.close()
	gitlog.close()

def main():
	repo_list = glob.glob("repositorys/*")
	for repo in repo_list:
		addr = repo.split("/")
		repo_name = addr[-1]+"/"
		log_dir = addr[-2]+"/"
		result_dir = "corpus/"
		try:
			make_corpus(repo_name,log_dir,result_dir)
		except:
			print("error")
		print("end")

		
if __name__ == "__main__":
	main()
