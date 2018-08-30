import random

class EatDB:

	eat_questions = ['뭐먹지','머먹지','뭐먹을지','머먹을지','뭐먹을까'] #질문 형식
	eat_category = ['한식','일식','중식','양식']
	eat_k = ['김치찌개','부대찌개','김치전','삼겹살','치킨','라면']
	eat_j = ['회','초밥','회덮밥','라멘','일본가정식','돈카츠']
	eat_c = ['짜장면','짬뽕','탕수육','훠궈','마라탕']
	eat_w = ['파스타','피자','스테이크']
	eat_all =[eat_k, eat_j, eat_c,eat_w]

	def __init__(self):
		pass
	
	def getEat(self,genre):
		select = self.eat_all[self.eat_category.index(genre)]
		return select