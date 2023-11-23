from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authlib import jose
from ..models import Team
from ..jsonValidator import validator
from ..jsonTemplate import *
import json

@csrf_exempt
def createTeam(request):
    if request.method == 'POST':
        if validator.team(json.loads(request.body)):
            requestData = json.loads(request.body)
            print(requestData)
            newTeamName = requestData["name"]
            newTeamInfo = requestData["info"]
            newTeam = Team(name=newTeamName, info=newTeamInfo)
            newTeam.save()

            data = {
                "success": True
            }
        else:
            data = {
                "error": "Invalid Json"
            }
    else:
        data = {
            "error": "Invalid Method"
        }
    
    return JsonResponse(data, safe=False)
