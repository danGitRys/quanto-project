from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Project, Assignment,Forecast,Positon,Booking,Employee
from ...middleware import validator
import json
from django.db.models import Q


@csrf_exempt
def getTableData(request, id: int) -> JsonResponse:
    
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Project.objects.filter(id=id).exists()
        if idExists:
            projectAssignments = Assignment.objects.filter(fk_project = id).all()
            employeeList = []
            for assignment in projectAssignments:
                tempJson = assignment.toJson()
                employeeList.append(tempJson)
            print(employeeList)

            empList = []
            for employee in employeeList:
                print(employee)
                employeeId = employee["fk_employee"]
                tempEmployee = Employee.objects.filter(id=employeeId).first()
                print(employeeId)
                print("here")

                tempEmpJson = {"employee":tempEmployee.toJson(),
                               "projects": None}

                assignedProjects = Assignment.objects.filter(fk_employee = employeeId).all()
                print(assignedProjects)
                projectList = []
                for project in assignedProjects:

                    print("PROJECT PROJECT PROJECT")
                    tempProjectJson = {"project":project.toJson(),
                                       "positions":None}
                    print(project)
                    tempJson = project.toJson()
                    projectId = tempJson["fk_project"]
                    print(projectId)
                    positionList = []


                    positionIds = Positon.objects.filter(fk_project=projectId).all()
                    for position in positionIds:

                        

                        positionJson = position.toJson()
                        positionId = positionJson["id"]
                        print(positionJson)
                        tempPositionJson = {"position":positionJson,
                                            "bookings": None,
                                            "forecasts": None}
                        bookingList = []
                        forecastList = []


                        forecasts = Forecast.objects.filter(Q(fk_position=positionId) & Q(fk_employee=employeeId)).all()

                        for forecast in forecasts:
                            print("forecasts----------------------------------------")
                            forecastJson = forecast.toJson()
                            forecastList.append(forecastJson)
                            print(forecastJson)
                        

                        bookings = Booking.objects.filter(Q(fK_position=positionId) & Q(fk_employee=employeeId)).all()
                        for booking in bookings:
                            print("bookings----------------------------------------")
                            bookingJson = booking.toJson()
                            bookingList.append(bookingJson)
                            print(bookingJson)
                        print("!!!!!!!!!!!!!!!!!")
                        print(len(bookingList))
                        if len(bookingList) != 0:
                            print("True")
                           
                            tempPositionJson["bookings"] = bookingList
                        if len(forecastList) != 0: 
                            tempPositionJson["forecasts"] = forecastList
                        positionList.append(tempPositionJson)
                        print("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
                        
                    
                    if len(positionList) != 0:
                        tempProjectJson["positions"]= positionList
                        #print(positionList)
                    
                    projectList.append(tempProjectJson)
                    
                    if len(projectList) != 0:
                        tempEmpJson["projects"]=projectList
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print(projectList)
                empList.append(tempEmpJson)
                print("aaölfjaöfjaefjkaöfawfawfaw")
                print(len(empList))
                response_data["data"] = empList
            


                

            #bookingJson = booking.toJson()
            response_data["success"] = True
            #response_data["data"] = bookingJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Entry with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
