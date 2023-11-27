from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee
from ...middleware import validator
import json

@csrf_exempt
def deleteEmployee(request,id:int)->JsonResponse:
    """Endpoint for deleting an Employee in the database

    Parameters
    ----------
    request : request
        Delete request
        
    id : int
        id of deleted Employee

    Returns
    -------
    JsonResponse
        Json containing Results if Employee was deleted successfully
    """
    
    response_data = {
            "success": True,
            "message": "Employee deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Employee.objects.filter(id = id).exists()
        if idExists:
            employee = get_object_or_404(Employee,id=id)
            employee.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Employee Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
