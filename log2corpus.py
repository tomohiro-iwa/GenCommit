import glob
import re
import unicodedata

## 改行　+++ ---数値タグ化
## filter
### 大文字小文字統一　ステミング
patarn = re.compile(r"([a-zA-Z0-9]*)")
katakana = re.compile(r"[ア-ン]")
rep_list = [
re.compile(r"\n"),r"<BR>"
]
def corpus_filter(corpus_str):
	#for i in 
	return patarn.sub(r" \1 ",corpus_str)
			
def line_generator(gitlog):
	result = []
	corpus_str = ""
	is_first = True
	for line in gitlog:
		if line[0:7] == "!!!!!!!":
			result.append( corpus_filter(line[7:-1]) )
			if is_first:
				is_first = False
			else:
				result.append(corpus_filter(corpus_str))
				yield result
				result = []
				corpus_str = ""
		else:
			corpus_str += line

def make_corpus(repo_name,log_dir,result_dir):
	print(log_dir+repo_name+"mygitlogdata.txt")

	gitlog = open(log_dir+repo_name+"mygitlogdata2.txt")
	commit = open(result_dir+repo_name+"commit_message.txt","a")
	diff = open(result_dir+repo_name+"diff.txt","a")

	log_lines = line_generator(gitlog)
	for line in log_lines:

		if katakana.search(line[1]):
			continue
		commit.write(line[0]+"\n") 
		diff.write(line[1]+"\n")

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
		#make_corpus(repo_name,log_dir,result_dir)
		print("end")


if __name__ == "__main__":
	main()
