from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime , json
from parser import *
import json
import random
 
def keyboard(request):
 
	return JsonResponse({'type' : 'buttons', 'buttons' : ['김비서!!!!!!!!', '너 할 줄 아는 게 뭐야?!!!!!']})
 
@csrf_exempt
def message(request):

	# input이 json 형식으로 들어온 것을 parsing
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	input_type = return_json_str['type'] # 어떤 타입의 메세지가 들어왔는지 (ex. 사진 등)

	# 놀 것 추천 변수들
	play_answer_type = ['뭐하지','머하지','모하지','뭐하지?','머하지?','모하지?'] #질문 형식
	play_category = ['영화 추천','노래 추천','장소 추천'] #카테고리
	movie_genre = ['SF','로멘스','공포','액션','애니메이션','히어로','재난','코믹','스릴러'] #영화 장르	
	music_list = ['닐로 - 지나오다','멜로망스 - 동화','테이 - 같은 베개']
	place_list = ['홍대','신촌','안산','혜린이네 집','강남','이태원']	

	if return_str == '김비서!!!!!!!!':
        	return JsonResponse({
                	'message': {
                        'text': ' 네 회장님, 부르셨나요? '
                	},
                	'keyboard': {
                        	'type': 'text',      
                	}
     	   	})
	elif return_str == '너 할 줄 아는 게 뭐야?!!!!!':
		return JsonResponse({
                	'message': {
                        'text': ' 회장님의 식사 메뉴 결정, 스케쥴 결정, 그 외 잡다한 결정을 도와드리고 있습니다.  '
                	},
                	'keyboard': {
                        	'type': 'text',      
                	}
     	   	})
	
	#놀 것 추천
	elif return_str in play_answer_type:
		return JsonResponse({
                	'message': {
                        'text': '다음 중에서 원하시는 서비스를 골라주세요!'
                		},
                		'keyboard': {
                      	  		'type' : 'buttons',
				'buttons' : ['영화 추천','노래 추천','장소 추천']      
                		}
     	   	})
	elif return_str in play_category:
		if return_str == '영화 추천':
			return JsonResponse({
                		'message': {
                    	    	'text': ' 어떤 장르가 좋으세요? '
                			},
                			'keyboard': {
                      	  			'type' : 'text'  
                			}
     	   		})
		elif return_str == '노래 추천':
			return JsonResponse({
                		'message': {
                    	    	'text': ' 오늘은 '+ rand(music_list) + ' 어떠세요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',
                			}
     	   		})

		else:
			return JsonResponse({
                		'message': {
                    	    'text': ' 오늘은 ' + rand(place_list) + ' 가볼까요?'
                			},
                			'keyboard': {
                      	  			'type' : 'text',  
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
			msg = "회장님 잘못들어서 그런데 다시 말씀해주시겠어요?"

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
