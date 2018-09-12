# parser.py
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
class Parser:
	def __init__(self):
		pass

	def movie_ranking(self):
		rank  = ''
		req = requests.get('http://www.cgv.co.kr/movies')
		soup = BeautifulSoup(req.content, "html.parser")
		rank_count = 1
		div = soup.find("div",{"class":"sect-movie-chart"})
		strong = div.find_all("strong",{"class":"title"})
		for l in strong:
			rank = rank + str(rank_count) +" "+ l.text + "\n"
			rank_count +=1
		return rank

	def music_ranking(self):
		rank = ''
		req = requests.get('http://www.genie.co.kr/')
		soup = BeautifulSoup(req.content, "html.parser")
		rank_count = 1
		tbody = soup.find("tbody")
		a = tbody.find_all("a",{"class":"title ellipsis"})

		for s in a:
			rank = rank + str(rank_count) +" "+ s.text + "\n"
			rank_count +=1

		return rank