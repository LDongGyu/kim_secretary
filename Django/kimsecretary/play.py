class PlayDB:

	play_category = ['영화 추천','노래 추천','장소 추천'] #카테고리
	movie_genre = ['SF','로맨스','공포','액션','애니메이션','히어로','재난','코믹','스릴러'] #영화 장르	
	movie_SF = ['인터스텔라','그래비티','라이프','인셉션']
	movie_romance = ['뷰티인사이드','그시절 우리가 좋아했던 소녀']
	movie_horror = ['곤지암','애나벨']
	movie_action = ['마녀','테이큰','미션임파서블','범죄도시']
	movie_ani = ['겨울왕국','미니언즈']
	movie_hero = ['어벤저스','아이언맨']
	movie_disaster = ['해운대','타워','판도라','볼케이노','투모로우','2012','지오스톰','감기']
	movie_comic = ['럭키','삼총사','청년경찰']
	movie_thriller = ['추격자','황해','괴물']
	movie_all = [movie_SF,movie_romance,movie_horror,movie_action,movie_ani,movie_hero,movie_disaster,movie_comic,movie_thriller]
	music_list = ['닐로 - 지나오다','멜로망스 - 동화','테이 - 같은 베개','자우림-있지']
	place_list = ['홍대','신촌','안산','강남','이태원']

	def __init__(self):
		pass

	def getMovie(self,genre):
		select = self.movie_all[self.movie_genre.index(genre)]
		return select

	def getQuestions(self):
		return self.play_questions

	def getCategory(self):
		return self.play_category

	def getGenre(self):
		return self.movie_genre
