from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authlib import jose
from ..models import Employee
from ..jsonValidator import validator
from ..jsonTemplate import *
import json


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def timeRegis(request):
    if request.method == "POST":
        data = {
            "text": "Hey"
        }
        return JsonResponse(data)
