from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee
from ...middleware import validator
import json


@csrf_exempt
def getEmployee(request, id: int) -> JsonResponse:
    """ Endpoint for getting Employee out of the Database
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
        JSON with Data of the Employee
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Employee.objects.filter(id=id).exists()
        if idExists:
            employee = get_object_or_404(Employee, id=id)
            employeeJson = employee.toJson()
            response_data["success"] = True
            response_data["data"] = employeeJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Employee with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
