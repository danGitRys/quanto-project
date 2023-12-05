from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from ...middleware import *
from ...models import Positon
from django.http import JsonResponse
@csrf_exempt
def createPositon(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("Post")
        try:
            request_data = json.loads(request.body)
            is_valid = validator.position(request_data)
            valid = is_valid["valid"]
            print(is_valid)

            if valid:
               
                new_position_id = request_data["position_id"]
                new_fk_project = request_data["fk_project"]
                new_rate = request_data["rate"]
                new_wd = request_data["wd"]
                new_volume_total = request_data["volume_total"]
                new_volume_remaining = request_data["volume_remaining"]
                new_start_date = request_data["start_date"]
                new_end_date = request_data["end_date"]
                newPosition = Positon(fk_project = new_fk_project,position_id=new_position_id,rate=new_rate,wd=new_wd,volume_total=new_volume_total,volume_remaining=new_volume_remaining,start_date=new_start_date,end_date=new_end_date)
                newPosition.save()

                response_data = {
                    "success": True,
                    "message": "Project created successfully.",
                }
            else:
                response_data = {
                    "success": False,
                    "error": "Invalid JSON format or missing required fields.",
                }
        except json.JSONDecodeError:
            response_data = {
                "success": False,
                "error": "Invalid JSON format.",
            }
    else:
        response_data = {
            "success": False,
            "error": "Invalid HTTP method. Only POST is allowed.",
        }

    # if a GET (or any other method) we'll create a blank form
   

    return JsonResponse(response_data)