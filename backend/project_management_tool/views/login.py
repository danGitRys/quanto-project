from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authlib import jose
from ..models import Employee
from ..middleware.validation import jsonFormValidator
from ..jsonTemplate import *
import json
import os
from dotenv import load_dotenv

load_dotenv()

@csrf_exempt
def login(request)->JsonResponse:
    """Endpoint to validate a Login again the database, and encrypt the sap btp token

    Parameters
    ----------
    request : request
        post request

    Returns
    -------
    JsonResponse
        Json Containing information if Login was successfull or not
    """
    if request.method == "POST":

        if(jsonFormValidator.formValidator.login(json.loads(request.body))):
            decoded = {}
            try:
                public = os.getenv('PUBLIC_KEY')
                data = json.loads(request.body)
                token = data["token"]
                decoded = jose.jwt.decode(token,key=public)
                print(decoded)
                email = decoded["email"]
                
                emp = Employee.objects.get(mail = email)
                data = {
                    "login":True,
                    "employee":emp.toJson()
                }
                
            except Exception as e:
                print(e)
                data = {
                    "login":False,
                }
            
          
            

        else:
             data = {
                "Error":"Invalid Json"
            }

    

    else:
        data = invalidMethod
    
    return JsonResponse(data)

    
