from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Employee
from ..jsonValidator import validator
import json
from ..jsonTemplate import *

@csrf_exempt
def getEmployee(request):
     print(request.body)
     if request.method == 'GET':
          employeeList = []
          allEmployees = Employee.objects.all()
          for employee in allEmployees:
               employeeList.append(employee.toJson())
               print(employee.toJson())
          data = {
               "employees": employeeList
          }
          print(employeeList)
          
          return JsonResponse(data)
     elif request.method == 'POST':
          data = invalidMethod
        
     
     else:
           data = {
               "type":"else"
          }

     return JsonResponse(data)


@csrf_exempt
def createEmployee(request):
  

    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_valid = validator.employee(request_data)

            if is_valid:
                new_emp_id = request_data["emp_id"]
                new_forename = request_data["forename"]
                new_surname = request_data["surname"]
                new_mail = request_data["mail"]
                new_phone = request_data["phone"]
                new_fk_team_id = request_data["fk_team_id"]
                new_team_roll = request_data["team_roll"]
                new_employee = Employee(emp_id = new_emp_id,forename = new_forename,surname = new_surname,mail=new_mail,phone=new_phone,fk_team_id = new_fk_team_id,team_roll=new_team_roll)
                new_employee.save()

                response_data = {
                    "success": True,
                    "message": "Employee created successfully.",
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
    else:
        response_data = {
            "success": False,
            "error": "Invalid HTTP method. Only POST is allowed.",
        }

    return JsonResponse(response_data)
          

