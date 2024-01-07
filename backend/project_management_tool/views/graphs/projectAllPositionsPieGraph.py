from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ...models import Positon,Project
from django.shortcuts import get_object_or_404
from ...middleware import validator
from ...middleware import dateRange
from ...middleware import positionBookings
from ...middleware import positionQuerys
from datetime import datetime
@method_decorator(csrf_exempt, name='dispatch')

class ProjectPositionsPieGraphView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Project.objects.filter(id=id_param).exists()
        if idExists:
            currentProject = Project.objects.filter(id=id_param).first()
            projectStartDate = currentProject.start_date
            projectEndDate = currentProject.end_date
            xValues = []
            yValues = []
            for currentDate in dateRange.range_date(projectStartDate,projectEndDate):
                xValues.append(currentDate)

            projectPositons = Positon.objects.filter(fk_project=id_param).all()
            for position in projectPositons:
                currentPositionId = position.id
                currentPositionInfo = positionQuerys.totalVolume(currentPositionId)
                volumeInfoUsed = positionQuerys.usedVolume(currentPositionId)
                #print(currentPositionInfo)
                #print(volumeInfoUsed)
            

                
                
              

            print("Works")
            
        else:
            response_data["success"] = False
            response_data["message"] = "No Project exists with this Id"
        

        return JsonResponse(response_data)
        

    def post(self,request ,*args, **kwargs):
        
        response_data = {
                "success": False,
                "error": "Post not supported",
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    