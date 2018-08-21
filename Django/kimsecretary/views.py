import re
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime , json
from parser import *
import json
import random
from kimsecretary.play import PlayDB
from kimsecretary.eat import EatDB
from kimsecretary.doOrNot import DoOrNot
from kimsecretary.parser import * 
current_msg = '안녕'
category = 0
terminal = False

def keyboard(request):

	return JsonResponse({'type' : 'buttons', 'buttons' : ['김비서!!!!!!!!', '너 할 줄 아는 게 뭐야?!!!!!']})

@csrf_exempt
def message(request):

	global current_msg
	global category
	global terminal
	# input이 json 형식으로 들어온 것을 parsing
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	#return_str = return_str.replace(" ","")
	input_type = return_json_str['type']  # 어떤 타입의 메세지가 들어왔는지 (ex. 사진 등)

	play_Handler = PlayDB()	# 놀 것 추천 클래스
	eat_Handler = EatDB()
	question = DoOrNot()
	parser_rank = Parser()
	
	play_Question = re.compile('(뭐|모|머)(하|할)') # 질문에 '하'가 들어가면 '놀 것 추천'	
	
	if return_str == "싫어":
		if terminal == False:
			return JsonResponse({
                	'message': {
                        'text': ' 전 조아요♡ '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})

		else:
			return_str = current_msg
	
	if return_str == '김비서!!!!!!!!':
		current_msg = return_str
		return JsonResponse({
                	'message': {
                        'text': ' 네 회장님, 부르셨나요? 궁금하신 사항 있으시다면 "도움말"을 눌러주세요 '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	elif return_str == '너 할 줄 아는 게 뭐야?!!!!!':
		current_msg = return_str
		return JsonResponse({
                	'message': {
                		'text': ' 회장님의 식사 메뉴 결정, 스케쥴 결정, 그 외 잡다한 결정을 도와드리고 있습니다. 더 궁금하신 사항은 "도움말"을 참고해주세요.  '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	elif return_str == "영화순위":
		return JsonResponse({
               		'message': {
                		'text': "요즘 상영중인 영화 순위입니다.\n\n"+ parser_rank.movie_ranking()
               			},
               			'keyboard': {
                     			'type' : 'text' , 
               			}})
	elif return_str == "노래순위":
		return JsonResponse({
			'message': {
			'text': "요즘 인기있는 노래 순위입니다.\n\n"+ parser_rank.music_ranking()
				},
				'keyboard': {
				'type' : 'text' , 
				}})

	elif return_str == "멜론순위":
		return JsonResponse({
			'message': {
			'text': "요즘 인기있는 노래 순위입니다.\n\n"+ parser_rank.melon_ranking()
				},
				'keyboard': {
				'type' : 'text' , 
				}})


	elif return_str == '개발자':
		current_msg = return_str
		return JsonResponse({
                	'message': {
                		'text': ' 중앙대학교 \n 생명과학 컴퓨터공학 16학번 김혜린 \n 컴퓨터공학 14학번 이동규 '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})	
	elif return_str == '도움말':
		current_msg = return_str
		return JsonResponse({
                	'message': {
                		'text': '질문형식은 다음과 같습니다. \n 1. ~/~/~ 중 뭐할까 or 골라줘 \n 2. ~ 할까 말까 or 볼까 말까 등 \n 3. 뭐하지 or 뭐먹지 등 \n 형식에 맞춰 질문해주시기 바랍니다!'
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})


	elif question.isQuestionOf(return_str):
		current_msg = return_str
		return JsonResponse({
                	'message': {
                    	'text': question.isQuestionOf_answer(return_str)
                		},
                		'keyboard': {
                      		'type' : 'text' , 
                		}
     	   	})

	elif play_Question.search(return_str):
		category = 5
		current_msg = return_str
		return JsonResponse({
                	'message': {
                        'text': '다음 중에서 원하시는 서비스를 골라주세요!'
                		},
                		'keyboard': {
                      	  		'type' : 'buttons',
				'buttons' : ['영화 추천','노래 추천','장소 추천']      
                		}
     	   	})

	elif question.isQuestion(return_str):
		current_msg = return_str
		return JsonResponse({
                	'message': {
                    	'text': question.isQuestion_answer(return_str)
                		},
                		'keyboard': {
                      		'type' : 'text' , 
                		}
     	   	})

	#먹을 것 추천
	elif return_str in eat_Handler.eat_questions:
		category = 1
		current_msg = return_str
		return JsonResponse({
                	'message': {
                        'text': '다음 중에서 원하시는 음식 종류를 골라주세요!'
                	},
                	'keyboard': {
                      	'type' : 'buttons',
			'buttons' : ['한식','일식','양식','중식','아무거나']      
                	}
     	   	})

	elif (return_str in eat_Handler.eat_category) and (category == 1):
		current_msg = return_str
		terminal = True
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat_Handler.getEat(return_str))+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})

	elif (return_str == '아무거나') and (category == 1):
		eat_rand = rand(eat_Handler.eat_all)
		terminal = True
		current_msg = return_str
		return JsonResponse({
                	'message': {
                    	'text': ' 오늘은 '+ rand(eat_rand) +' 어떠세요?'
                		},
                		'keyboard': {
                      		'type' : 'text' , 
                		}
     	   	})

	
	#놀 것 추천
	elif return_str in play_Handler.play_category:
		current_msg = return_str
		if (return_str == '영화 추천') and (category == 5):
			category = 2
			return JsonResponse({
                		'message': {
                    	    	'text': ' 어떤 장르가 좋으세요? '
                			},
                			'keyboard': {
                      	  			'type' : 'text' , 
                			}
     	   		})
			
		elif (return_str == '노래 추천') and (category == 5):
			terminal = True
			return JsonResponse({
                		'message': {
                    	    	'text': ' 오늘은 '+ rand(play_Handler.music_list) + ' 어떠세요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',
                			}
     	   		})

		elif (return_str == '갈곳 추천') and (category == 5):
			terminal = True
			return JsonResponse({
                		'message': {
                    	    'text': ' 오늘은 ' + rand(play_Handler.place_list) + ' 가볼까요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',  
                			}
     	   		})

		else:
			return JsonResponse({
                		'message': {
                    	    'text': ' 갑자기 무슨 소리세요 회장님; '
                			},
                			'keyboard': {
                      	  			'type' : 'text',  
                			}
     	   		})

	elif (return_str in play_Handler.movie_genre) and (category == 2):
		current_msg = return_str
		terminal = True
		return JsonResponse({
                	'message': {
                    	'text': ' 오늘은 '+ rand(play_Handler.getMovie(return_str)) +' 어떠세요?'
                		},
                		'keyboard': {
                      		'type' : 'text' , 
                		}
     	   	})

	elif return_str == "좋아":
		if terminal == True:
			terminal = False
			category = 0	
			return JsonResponse({
                		'message': {
                    		'text': ' 탁월한 선택이십니다. 이제 퇴근해도 되나요? '
                			},
                			'keyboard': {
                      			'type' : 'text' , 
                			}})
	



		else:
			return JsonResponse({
                		'message': {
                    		'text': ' 아..네ㅋ; '
                			},
                			'keyboard': {
                      			'type' : 'text' , 
                			}

     	   	})


	#잘못된 input 예외처리
	else:
		if input_type == 'photo':
			msg = "회장님 사진은 아직 볼 수 없어요. 다시 입력해주세요."
		elif input_type == 'video':
			msg = "회장님...동영상은 집에서 혼자 보세요. 다시 입력해주세요."
		elif input_type == 'audio':
			msg = "회장님 녹음파일은 안돼요. 다시 입력해주세요."
		else:
			msg = "회장님 잘 못 들어서 그런데 다시 말씀해주시겠어요?"

		return JsonResponse({
                	'message': {
                        'text': msg
                		},
                		'keyboard': {
                       	 	'type': 'text',      
                		}
     	   	})


def rand(list):
	rand_num = random.randrange(0,len(list))
	return list[rand_num]