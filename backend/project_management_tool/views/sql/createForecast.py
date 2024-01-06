from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee,Booking,Forecast
from ...middleware import validator
from ...middleware import eligiblePositionIds
from ...middleware import dateGenerator
from ...middleware import roundTime
import json
import random



#Remove?


@csrf_exempt
def createForecastsSql(request) -> JsonResponse:
    """ Endpoint for getting Booking Data out of the Database
    Parameters
    ----------
    request : request
        Get Request
    id : int
        describe the path for dynamic routing 
    Returns
    -------
    JsonResponse
        if success = True 
        JSON with Data of the Booking Entry
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
       allEmployees = Employee.objects.all()
       for employee in allEmployees:
           employeeJson = employee.toJson()
           employeeId = employeeJson["id"]
           print(employeeId)
           listPossiblePositions = eligiblePositionIds(employeeId).toJsonTotal()
           print(listPossiblePositions)

           for day in range(1,60000):
               dateGen = dateGenerator(day)
               startDate = dateGen.generateStartDate()
               endDate = dateGen.generateEndDate()
               startDateRounded = roundTime.round_to_quarter_hour(startDate)
               endDateRounded = roundTime.round_to_quarter_hour(endDate)
               
               randomPosition = random.choice(listPossiblePositions)
               randomPositionId = randomPosition["position_id"]
               infoData = 'test'
               newForecast = Forecast(fk_employee=employeeId,fk_position=randomPositionId,start=startDateRounded,end=endDateRounded,info=infoData)
               #newBooking = Booking(fk_employee=employeeId,fk_position=randomPositionId,start=startDate,end=endDate,pause=pauseTime,time=workingTime)
               newForecast.save()
               #print(startDate)
               
               
               
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
