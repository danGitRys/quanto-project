from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee,Booking
from ...middleware import validator
from ...middleware import eligiblePositionIds
from ...middleware import dateGenerator
import json
import random




#Remove?



@csrf_exempt
def createBookingsSql(request) -> JsonResponse:
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
       counter = 0
       for employee in allEmployees:
           employeeJson = employee.toJson()
           employeeId = employeeJson["id"]
           #print(employeeId)
           print("Employee-------------------------------------------------------------------------------------------")
           print(counter)
           counter +=1
           listPossiblePositions = eligiblePositionIds(employeeId).toJsonTotal()
           #print(listPossiblePositions)

           for day in range(0,30):
               dateGen = dateGenerator(-day)
               startDate = dateGen.generateStartDate()
               endDate = dateGen.generateEndDate()
               pauseTime = dateGen.generatePauseTime(startDate,endDate)
               workingTime = dateGen.calculateTimeDifference(startDate,endDate)-pauseTime
               randomPosition = random.choice(listPossiblePositions)
               randomPositionId = randomPosition["position_id"]
               #print(randomPositionId)
               #print("Id             "+  str(randomPositionId))
               newBooking = Booking(fk_employee=employeeId, fK_position=randomPositionId,
                                     start=startDate, end=endDate, pause=pauseTime)
               newBooking.save()
               del(newBooking)
               #newBooking = Booking(fk_employee=employeeId,fk_position=randomPositionId,start=startDate,end=endDate,pause=pauseTime,time=workingTime)
               #print(newBooking)

               #print(startDate)
               
               
               
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
