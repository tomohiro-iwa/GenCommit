import urllib.request as url_req
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
import time


def ranking_page(page):
	l = "https://github.com/search?l=Java&p="
	r = "&q=stars%3A%3E1&s=stars&type=Repositories"
	return l+str(page)+r

def get_repo_list(url):
	repo_list = []
	html = url_req.urlopen(url)
	soup = BeautifulSoup(html,"lxml")
	for tag in soup.select("a.v-align-middle"):
		print(tag["href"])
	return repo_list
		
def main():
	url_list = [ranking_page(i) for i in range(1,101)]
	for url in url_list:
		repo_list = get_repo_list(url)
		for repo in repo_list:
			print(repo)
		time.sleep(10)

if __name__ == "__main__":
	main()
