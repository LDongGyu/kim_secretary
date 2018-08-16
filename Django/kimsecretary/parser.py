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
		req = requests.get('https://www.melon.com')
		soup = BeautifulSoup(req.content, "html.parser")
		rank_count = 1
		div = soup.find("div",{"class":"list_wrap typeRealtime"})
		p = div.find_all("p",{"class":"song"})

		for s in p:
			temp= s.find("a",{"class":"ellipsis mlog"})
			rank = rank + str(rank_count) +" "+ temp.text + "\n"
			rank_count +=1

		return rank
