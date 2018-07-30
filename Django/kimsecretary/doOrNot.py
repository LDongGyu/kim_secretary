import re
import random

class DoOrNot:

	question_of  = re.compile('(./)*.중.*까') 	
	question = re.compile('.*(할|볼|먹을|달릴|쏠|쨀|버릴|살|지를|뽑을|갈|죽을|잘|마실)까')

	def __init__(self):
		pass

	def isQuestionOf(self,string):
		return self.question_of.search(string)

	def isQuestion(self,string):
		return self.question.search(string)

	def isQuestion_answer(self,string):
		main_question = string[string.find('까')-1]
		random_number = random.randrange(0,2)
		
		if random_number < 1:
			return main_question
		else:
			return main_question+'지마'

	def isQuestionOf_answer(self,string):
		parsing = string.split('/')
		last_index = len(parsing)-1
		parsing[0] = parsing[0][parsing[0].rfind(' ')+1:]
		parsing[last_index] = parsing[last_index][:parsing[last_index].find(' ')]
		return parsing[last_index]