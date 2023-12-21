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

class PositionGraphView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Positon.objects.filter(id=id_param).exists()
        if idExists:
            position = get_object_or_404(Positon, id=id_param)
            
        else:
            response_data["success"] = False
            response_data["message"] = "No Position exists with this Id"
        

        return JsonResponse(response_data)
        return HttpResponse("Get")

    def post(self,request ,*args, **kwargs):
        
        response_data = {
                "success": False,
                "error": "Post not supported",
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    