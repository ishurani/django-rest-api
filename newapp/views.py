from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from newapp.models import thought
from django.http import JsonResponse
import json
import random
from rest_framework.decorators import api_view
from rest_framework.request import Request
import threading
import schedule
import time
thought_dict={}

def get_Thought():
    global thought_dict
    print("From print_time", time.time())
    t= thought.objects.all().count()
    n = random.randint(1,t)
    thought_list=thought.objects.get(id=n)
    thought_dict={'Today\'s Thought':thought_list.thought_name}
    print(thought_dict)


def run():
    global thought_dict

    print(threading.currentThread().getName())
    #schedule.every(5).seconds.do(get_Thought)
    schedule.every().day.at("11:59").do(get_Thought)
    while True:
        schedule.run_pending()
        time.sleep(1)



threading.Thread(name = 'timer', target=run).start()

@csrf_exempt
@api_view(['GET'])
def index(request):
        global thought_dict
        if request.method == 'GET':
                return JsonResponse(json.dumps(thought_dict),safe=False)
