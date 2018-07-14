from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime , json
from parser import *
import json
import random
from kimsecretary.play import PlayDB
import re

def keyboard(request):

	return JsonResponse({'type' : 'buttons', 'buttons' : ['김비서!!!!!!!!', '너 할 줄 아는 게 뭐야?!!!!!']})

@csrf_exempt
def message(request):

	# input이 json 형식으로 들어온 것을 parsing
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	#return_str = return_str.replace(" ","")
	input_type = return_json_str['type']  # 어떤 타입의 메세지가 들어왔는지 (ex. 사진 등)

	# 먹을 것 추천 변수들
	eat_questions = ['뭐먹지','머먹지','뭐먹을지','머먹을지'] #질문 형식
	eat_category = ['한식','일식','중식','양식']
	eat_k = ['김치찌개','부대찌개','김치전','삼겹살','치킨','라면']
	eat_j = ['회','초밥','회덮밥','라멘','일본가정식','돈카츠']
	eat_c = ['짜장면','짬뽕','탕수육','훠궈','마라탕']
	eat_w = ['파스타','피자','스테이크']

	play_Handler = PlayDB()	# 놀 것 추천 클래스
	play_Question = re.compile('하') # 질문에 '하'가 들어가면 '놀 것 추천'

	if return_str == '김비서!!!!!!!!':
        	return JsonResponse({
                	'message': {
                        'text': ' 네 회장님, 부르셨나요? 궁금하신 사항 있으시다면 "도움말"을 눌러주세요 '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	elif return_str == '너 할 줄 아는 게 뭐야?!!!!!':
		return JsonResponse({
                	'message': {
                		'text': ' 회장님의 식사 메뉴 결정, 스케쥴 결정, 그 외 잡다한 결정을 도와드리고 있습니다. 더 궁금하신 사항은 "도움말"을 참고해주세요.  '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	elif return_str == '개발자':
		return JsonResponse({
                	'message': {
                		'text': ' 중앙대학교 \n 생명과학 컴퓨터공학 16학번 김혜린 \n 컴퓨터공학 14학번 이동규 '
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	elif return_str == '도움말':
		return JsonResponse({
                	'message': {
                		'text': ' [음식]을 추천 받고 싶으시면 [먹]이 들어가게 질문해주시고,\n [놀 것]을 추천 받고 싶으시다면 [하]가 들어가게 질문해주세요! \n ex) 뭐먹지? , 머먹징 , 뭐하지? , 모하쥥 등등'
                	},
                	'keyboard': {
                        'type': 'text',      
                	}
     	   	})
	
	#먹을 것 추천
	elif return_str in eat_questions:
		return JsonResponse({
                	'message': {
                        'text': '다음 중에서 원하시는 음식 종류를 골라주세요!'
                	},
                	'keyboard': {
                      	'type' : 'buttons',
			'buttons' : ['한식','일식','양식','중식','아무거나!']      
                	}
     	   	})
	
	elif return_str =='한식':
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat_k)+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})
	elif return_str == '일식' :
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat_j)+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})
	elif return_str == '양식' :
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat_w)+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})
	elif return_str == '중식' :
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat_c)+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})
	elif return_str == '아무거나!' :
		rand_eat = rand(eat_category)
		if rand_eat == '한식':
			eat = eat_k
		elif rand_eat == '일식':
			eat = eat_j
		elif rand_eat == '양식':
			eat = eat_w
		else:
			eat = eat_c
		
		return JsonResponse({
			'message': {
			'text' : '오늘의 식사 메뉴로는 '+ rand(eat)+' 어때요?'
			},
			'keyboard': {
                        'type': 'text',      
                	}
		})

	#놀 것 추천
	elif play_Question.search(return_str):
		return JsonResponse({
                	'message': {
                        'text': '다음 중에서 원하시는 서비스를 골라주세요!'
                		},
                		'keyboard': {
                      	  		'type' : 'buttons',
				'buttons' : ['영화 추천','노래 추천','장소 추천']      
                		}
     	   	})
	elif return_str in play_Handler.play_category:
		if return_str == '영화 추천':
			return JsonResponse({
                		'message': {
                    	    	'text': ' 어떤 장르가 좋으세요? '
                			},
                			'keyboard': {
                      	  			'type' : 'text' , 
                			}
     	   		})
		elif return_str == '노래 추천':
			return JsonResponse({
                		'message': {
                    	    	'text': ' 오늘은 '+ rand(play_Handler.music_list) + ' 어떠세요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',
                			}
     	   		})

		else:
			return JsonResponse({
                		'message': {
                    	    'text': ' 오늘은 ' + rand(play_Handelr.place_list) + ' 가볼까요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',  
                			}
     	   		})
	elif return_str in play_Handler.movie_genre:
		return JsonResponse({
                	'message': {
                    	'text': ' 오늘은 '+ rand(play_Handler.getMovie(return_str)) +' 어떠세요?'
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
