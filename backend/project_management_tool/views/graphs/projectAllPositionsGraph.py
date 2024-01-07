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
from datetime import datetime
from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired
@method_decorator(csrf_exempt, name='dispatch')

class ProjectPositionsGraphView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        if (isTokenExpired(args[0])):
            allowedRoles = ['Admin']
            if (HeaderValidation.isAuthorized(args[0], allowedRoles)):
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
                        currentPositionName = position.position_name
                        currentPositonY_Values = []
                        #print(position)
                        currentVolume = 0
                        for currentDate in dateRange.range_date(projectStartDate,projectEndDate):
                        #x_data.append(currentDate)
                            tempPositionBookings = positionBookings(currentDate,currentPositionId).executeQueryJsonResult()
                            volume = int(tempPositionBookings["volume"])
                            currentVolume += volume
                            currentPositonY_Values.append(currentVolume)

                    
                            #print(volume)
                        tempPositionValues = {
                            "positionName": currentPositionName,
                            "yValues": currentPositonY_Values
                        }
                        yValues.append(tempPositionValues)

                        postionData = {
                            "xData": xValues,
                            "yData":yValues
                        }
                        response_data["data"] = postionData
                    

                        
                        
                    

                    print("Works")
                    
                else:
                    response_data["success"] = False
                    response_data["message"] = "No Project exists with this Id"
            else:
                response_data["success"] = False
                response_data["message"] = "Token expired"
        else:
            response_data["success"] = False
            response_data["message"] = "Invalid Method"
        

        return JsonResponse(response_data)
        

    def post(self,request ,*args, **kwargs):
        
        response_data = {
                "success": False,
                "error": "Post not supported",
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    