from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ...models import Positon
from django.shortcuts import get_object_or_404
from ...middleware import validator
from ...middleware import dateRange
from ...middleware import positionBookings
from ...middleware.sqlQuery.timeTable import positionQuerys,projectQuerys
from datetime import datetime
@method_decorator(csrf_exempt, name='dispatch')

class TimeTableForecastView(View):
    def get(self,*args, **kwargs):
        response_data = {
                "success": False,
                "error": "Post not supported",
            }
       
        return JsonResponse(response_data)
        

    def post(self,request ,*args, **kwargs):
        

        """ 
        start_date
        end_date
        employee_id
        project_id
        """
        request_data = json.loads(request.body)
        start_date = request_data["start_date"]
        end_date = request_data["end_date"]
        start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
        end_date_object = datetime.strptime(end_date,'%Y-%m-%d')
        start_date = start_date_object.date()
        end_date = end_date_object.date()
        employee_id = request_data["employee_id"]
        project_id = request_data["project_id"]
        dataList = []
        for currentDate in dateRange.range_date(start_date,end_date):
            inProjectData = projectQuerys.timeInProjectForecastDay(project_id,employee_id,currentDate)
            outsideProjectData = projectQuerys.timeNotInProjectForecastDay(project_id,employee_id,currentDate)
            inProjectVolume = inProjectData["volume"][0]
            outsideProjectVolume = outsideProjectData["volume"][0]
            if inProjectVolume is None:
                inProjectVolume = 0
            if outsideProjectVolume is None:
                outsideProjectVolume = 0
            dataList.append({
                'date':currentDate,
                'inProject':inProjectVolume,
                'outsideProject':outsideProjectVolume
            })
            print(inProjectVolume)
            print(currentDate)
        response_data = {
                "success": True,
                "error": "",
                "data":dataList
            }
        return JsonResponse(response_data)
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    