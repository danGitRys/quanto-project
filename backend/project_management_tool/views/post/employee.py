from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ...models import Employee
import json
from ...jsonTemplate import *
from ...middleware import *
from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired

@csrf_exempt
def getEmployee(request)->JsonResponse:
        """Function to get all Employees in the database

        Parameters
        ----------
        request : request
            Get request

        Returns
        -------
        JsonResponse
            All Employess as Json
        """

        if request.method == 'GET':
            employeeList = []
            allEmployees = Employee.objects.all()
            for employee in allEmployees:
                employeeList.append(employee.toJson())
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
def createEmployee(request)->JsonResponse:
    """Endpoint to create a Employee in the Database

    Parameters
    ----------
    request : request
        post request

    Returns
    -------
    JsonResponse
        Json Containing information about insertion Process
    """

    allowedRoles = ['Admin']
    if (isTokenExpired(request)):
        if (HeaderValidation.isAuthorized(request, allowedRoles)):
            if request.method == 'POST':
                try:
                    request_data = json.loads(request.body)
                    is_valid = validator.employee(request_data)
                    print(is_valid)
                    if is_valid["valid"]:
                        
                        new_emp_id = request_data["emp_id"]
                        new_forename = request_data["forename"]
                        new_surname = request_data["surname"]
                        new_mail = request_data["email"]
                        new_phone = request_data["phone"]
                        new_fk_team_id = request_data["fk_team_id"]
                        new_team_role = request_data["team_role"]

                        new_employee = Employee(emp_id = new_emp_id,forename = new_forename,surname = new_surname,mail=new_mail,phone=new_phone,fk_team_id = new_fk_team_id,team_roll=new_team_role)
                        new_employee.save()

                        response_data = {
                            "success": True,
                            "message": "Employee created successfully.",
                        }
                    else:
                        response_data = {
                            "success": False,
                            "error": is_valid["errors"],
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
        else:
            response_data = {
                    "success": False,
                    "error": "Not Authorized",
            }
    else:
        response_data["success"] = False
        response_data["message"] = "Token expired"

    return JsonResponse(response_data)

