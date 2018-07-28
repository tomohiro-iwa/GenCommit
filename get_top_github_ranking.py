import urllib.request as url_req
from bs4 import BeautifulSoup

def ranking_page(page):
	l = "https://github.com/search?l=Java&p="
	r = "&q=stars%3A%3E1&s=stars&type=Repositories"
	return l+str(page)+r

def get_repo_list(soup):
	repo_list = []
	for tag in soup.select("a.v-align-middle"):
		print(tag["href"])
	return repo_list
		
def main():
	for i in range(1,101):
		html = url_req.urlopen(ranking_page(i))
		soup = BeautifulSoup(html,"lxml")
		for repo in get_repo_list(soup):	
			print(repo)

if __name__ == "__main__":
	main()
