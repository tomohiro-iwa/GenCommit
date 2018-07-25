import sys

def main():
	word_freq = {}
	for line in open(sys.argv[1]):
		words = line.split(" ")

		for one_word in words:
			if one_word in word_freq:
				word_freq[one_word]+=1
			else:
				word_freq[one_word]=1
	word_ranking =  sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
	for i in word_ranking:
		print(i[0],"\t",i[1])	
if __name__ == "__main__":
	main()
