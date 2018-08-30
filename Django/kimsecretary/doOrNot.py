import re
import random

class DoOrNot:

	question_of  = re.compile('(./)*.중.*(골라.*|까)') 	
	question = re.compile('.*(할|볼|먹을|달릴|쏠|쨀|버릴|살|지를|뽑을|갈|죽을|잘|마실)까')

	def __init__(self):
		pass

	def isQuestionOf(self,string):
		return self.question_of.search(string)

	def isQuestion(self,string):
		return self.question.search(string)

	def isQuestion_answer(self,string):
		main_question = string[:string.find('까')]
		random_number = random.randrange(0,2)
		
		if main_question == '할':
			if random_number < 1:
				main_question = "일단 해봐ㅎ"
			else:
				main_question = "하지마ㅜㅜ"

		elif main_question == '볼':
			if random_number < 1:
				main_question = "당연히 봐야지ㅋㅋㅋㅋ"
			else:
				main_question = "보지마ㅡㅡ..."

		elif main_question == '먹을':
			if random_number < 1:
				main_question = "일단 먹어 맛있게 먹으면 0kcal"
			else:
				main_question = "먹지마...체중계 올라가봐..."

		elif main_question == '달릴':
			if random_number < 1:
				main_question = "달려달려~~~ 3차까지 달려!"
			else:
				main_question = "달리지마 나 힘들어..."

		elif main_question == '쏠':
			if random_number < 1:
				main_question = "오늘은 너가 다 쏴"
			else:
				main_question = "쏘지마 감당 안돼"

		elif main_question == '쨀':
			if random_number < 1:
				main_question = "인생 뭐있나 째"
			else:
				main_question = "어디가 ㅡㅡ; 째지마"

		elif main_question == '버릴':
			if random_number < 1:
				main_question = "버려 갖고 있으면 짐이야 짐"
			else:
				main_question = "버리지마 아까워 ㅜㅜ"

		elif main_question == '살':
			if random_number < 1:
				main_question = "고민할바에 걍 사버려!!!"
			else:
				main_question = "사지마;; 돈 아까워"

		elif main_question == '지를':
			if random_number < 1:
				main_question = "인생 뭐있냐; 질러!!"
			else:
				main_question = "지르지마;; 돈 얼마나 남았어?"

		elif main_question == '뽑을':
			if random_number < 1:
				main_question = "뽑아버렿ㅎㅎㅎㅎㅎ"
			else:
				main_question = "뽑지마"

		elif main_question == '갈':
			if random_number < 1:
				main_question = "ㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱ가"
			else:
				main_question = "브라운아이즈 - 가지마가지마"

		elif main_question == '죽을':
			return "생명은 소중합니다."

		elif main_question == '잘':
			if random_number < 1:
				main_question = "가서 발 닦고 코자"
			else:
				main_question = "벌써 자는거야? 자지마"

		elif main_question == '마실':
			if random_number < 1:
				main_question = "마셔마셔~ 언제까지 어깨춤을 추게할꺼야~"
			else:
				main_question = "오늘도?? 마시지마ㅡㅡ"

		else:
			return "모르겠어요. 회장님 다시 물어봐주세요"

		return main_question

	def isQuestionOf_answer(self,string):
		parsing = string.split('/')
		last_index = len(parsing)-1
		parsing[0] = parsing[0][parsing[0].rfind(' ')+1:]
		parsing[last_index] = parsing[last_index][:parsing[last_index].find(' ')]
		
		return parsing[random.randrange(0,last_index+1)]