from django.shortcuts import render
import random
from websocket import create_connection
import json


# Create your views here.

def index(request):
    return render(request,'emotion_app/index.html')


def emotion(request):

    ws = create_connection("wss://api.sakura.io/ws/v1/73104f77-912c-47bf-b431-ee7afdf76ff8")

    result = ws.recv()




    dict_emo = json.loads(result)
    ws.close()

    print(dict_emo)
    if(dict_emo["type"] == "channels"):
        happy = dict_emo["payload"]["channels"][0]
        angry = dict_emo["payload"]["channels"][1]
        sad = dict_emo["payload"]["channels"][2]
        enjoy = dict_emo["payload"]["channels"][3]
        shocked = dict_emo["payload"]["channels"][4]
        emo_list = [happy,angry,sad,enjoy,shocked]
        for emo in emo_list:
            print(emo)
            if emo["value"] == 100:
                if emo["channel"] == 0:
                    return render(request,'emotion_app/happy.html')
                elif emo["channel"] == 1:
                    return render(request,'emotion_app/angry.html')
                elif emo["channel"] == 2:
                    return render(request,'emotion_app/sad.html')
                elif emo["channel"] == 3:
                    return render(request,'emotion_app/enjoy.html')
                elif emo["channel"] == 4:
                    return render(request,'emotion_app/shocked.html')
                else:
                    return render(request,'emotion_app/nodata.html')
            else:
                return render(request,'emotion_app/nodata.html')

    return render(request,'emotion_app/nodata.html')
