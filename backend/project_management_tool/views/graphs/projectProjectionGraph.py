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
from ...middleware.sqlQuery.graph import projectQuerys
from ...middleware.time.dateBack import dateBack
from datetime import datetime,date
@method_decorator(csrf_exempt, name='dispatch')

class ProjectProjectionGraphView(View):
    def get(self,request,id,weeks):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = id
        week_param = weeks
        print(id_param)
        print(week_param)

        tempVolume = projectQuerys.usedVolumeUntilDate(id_param,date.today())
        print("----------Final Result--------------------------------------")
        print(tempVolume)
        idExists: bool = Project.objects.filter(id=id_param).exists()
        if idExists:
            currentProject = Project.objects.filter(id=id_param).first()
            currentProjectVolume = projectQuerys.totalVolume(id_param)
            currentProjectVolumeInt = currentProjectVolume["volume"]
           
            projectStartDate = currentProject.start_date
            projectEndDate = currentProject.end_date
            xValues = []
            yValues = []
            for currentDate in dateRange.range_date(projectStartDate,projectEndDate):
                xValues.append(currentDate)
            initDate = dateBack.getDateWeeksBack(week_param)
            #initDate = datetime.strptime("%Y-%m-%d",initDate)
           
            #projectStartDate = datetime.strptime('%Y-%M-%D',projectStartDate)
            if initDate<projectStartDate:
                initDate=projectStartDate
            print(initDate)

            firstVolume = projectQuerys.usedVolumeUntilDate(id_param,initDate)
            if initDate == projectStartDate:
                firstVolume = 0
            secondVolume = projectQuerys.usedVolumeUntilDate(id_param,date.today())
            print(firstVolume)
            print(secondVolume)

            dateDiff = date.today() - initDate
            dateDiffDays = dateDiff.days
            volumeDiff = secondVolume-firstVolume
            if dateDiffDays == 0:
                dailyIncrease = 0
            else:
                dailyIncrease = volumeDiff/dateDiffDays
            print(dateDiffDays)

            secondYValues = []
            existingValues = []
            for currentDate in dateRange.range_date(projectStartDate,date.today()):
                currentVolume = projectQuerys.usedVolumeUntilDate(id_param,currentDate)
                yValues.append(currentVolume)
                secondYValues.append(currentProjectVolumeInt)
            
            futureValues = []
            futureVolume = secondVolume
            for futureDate in dateRange.range_date(date.today(),projectEndDate):
                if futureDate==date.today():
                    continue
                #print(futureDate)
                futureVolume += dailyIncrease
                yValues.append(futureVolume)
                secondYValues.append(currentProjectVolumeInt)
                #print(futureVolume)
            yValuesNew = []
            tempPositionValues = {
                    "positionName": "Normal",
                    "yValues": yValues
                }
            tempPositionValues2 = {
                    "positionName": "Normal",
                    "yValues": secondYValues
                }
            yValuesNew.append(tempPositionValues)
            yValuesNew.append(tempPositionValues2)
           
            response_data["data"] = {
                'xData':xValues,
                'yData':yValuesNew
            }
            print("Works")
            
        else:
            print("here")
            response_data["success"] = False
            response_data["message"] = "No Project exists with this Id"
            response_data["weeks"] = week_param
        

        return JsonResponse(response_data)
        

    def post(self,request ,*args, **kwargs):
        
        response_data = {
                "success": False,
                "error": "Post not supported",
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    