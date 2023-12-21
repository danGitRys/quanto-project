from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ...models import Positon
from django.shortcuts import get_object_or_404
from ...middleware import validator
@method_decorator(csrf_exempt, name='dispatch')

class PositionView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Positon.objects.filter(id=id_param).exists()
        if idExists:
            position = get_object_or_404(Positon, id=id_param)
            positionJson = assignment.toJson()
            response_data["success"] = True
            response_data["data"] = positionJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Position exists with this Id"
        

        return JsonResponse(response_data)
        return HttpResponse("Get")

    def post(self,request ,*args, **kwargs):
        try:
            request_data = json.loads(request.body)
            is_valid = validator.position(request_data)
            print(is_valid)
            valid = is_valid["valid"]
            errors = is_valid["errors"]
            print(valid)

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
                    "message": "Position created successfully.",
                }
            else:
                response_data = {
                    "success": False,
                    "error": errors,
                }
        except json.JSONDecodeError:
            response_data = {
                "success": False,
                "error": "Invalid JSON format.",
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    