from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
import datetime , json
from parser import *
import json
 
def keyboard(request):
 
        return JsonResponse({'type' : 'buttons', 'buttons' : ['김비서!!!!!!!!', '너 할 줄 아는 게 뭐야?!!!!!']})
 
@csrf_exempt
def message(request):
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
 
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

