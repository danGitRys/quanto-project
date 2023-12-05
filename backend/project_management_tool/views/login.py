from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authlib import jose
from ..models import Employee
from ..jsonValidator import validator
from ..jsonTemplate import *
import json
@csrf_exempt
def login(request):
    if request.method == "POST":

        if(validator.login(json.loads(request.body))):
            decoded = {}
            try:
                public = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArcTWSGwEAalCoWpGMO+G\nyzDkWUeRGWxp9FA5i7jhS2122lrlvMCEoJfuQ6WcsvnsA6Qed6X0bIY31JYuHqhO\nbJ/cR7I9LqI+VPgJatjlGkQAb/AHfD0oAtyAvSH7eFyuaRtE2piVx2+mvASETDnB\ndR2MvrrY3hrr3Te7NRNtAZs1CqhjJPONPCRrINuwlZ+USynhMe0Vju3ajmPDgEQZ\nvu4sBaWmfOA6d3h8pFulkW6VCNA00KTR9MjG4qJVSAYhlkR1bSeed1gIP13e0/h1\nRB7udUckgdjXOSdNwLg1sIxZgHsKmyxcr6eCGeKgXu7OXyHspi48nDBtYgwP/jOy\nkwIDAQAB\n-----END PUBLIC KEY-----"
                data = json.loads(request.body)
                token = data["token"]
                decoded = jose.jwt.decode(token,key=public)
                email = decoded["email"]
                
                emp = Employee.objects.get(mail = email)
                data = {
                    "login":True,
                    "employee":emp.toJson()
                }
                
            except Exception as e:
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

    
