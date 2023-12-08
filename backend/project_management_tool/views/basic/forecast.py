from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from ...models import Forecast
import json
from ...middleware import validator
@method_decorator(csrf_exempt, name='dispatch')

class ForecastView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
    }
        id_param = kwargs.get('id')
        idExists: bool = Forecast.objects.filter(id=id_param).exists()
        if idExists:
            forecast = get_object_or_404(Forecast, id=id)
            forecastJson = forecast.toJson()
            response_data["success"] = True
            response_data["data"] = forecastJson
        else:
            response_data["success"] = False
            response_data["message"] = "No  Forecast with this Id"

        return JsonResponse(response_data)
    
    def post(self,request ,*args, **kwargs):
        try:
            request_data = json.loads(request.body)
            is_valid = True

            if is_valid:
               
                new_fk_employee = request_data["fk_employee"]
                new_fk_position = request_data["fk_position"]
                new_start = request_data["start"]
                new_end = request_data["end"]
                new_info = request_data["info"]
                newForecast = Forecast(fk_employee=new_fk_employee,fk_position=new_fk_position,start=new_start,end=new_end,info=new_info)
                newForecast.save()
                response_data = {
                    "success": True,
                    "message": "Forecast created successfully.",
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
        return JsonResponse(response_data)
    
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    def delete(self, *args, **kwargs):
        response_data = {
            "success": True,
            "message": "Forecast deleted successfully.",
            }
        id_param = kwargs.get('id')
        idExists:bool =  Forecast.objects.filter(id = id).exists()
        if idExists:
            forecast = get_object_or_404(Forecast,id=id)
            forecast.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Forecast Exists with this Id"

        return JsonResponse(response_data)