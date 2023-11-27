from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee
from ...middleware import validator
import json

@csrf_exempt
def deleteEmployee(request,id)->JsonResponse:
    
    response_data = {
            "success": True,
            "message": "Employee deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Employee.objects.filter(id = id).exists()
        if idExists:
            assignment = get_object_or_404(Employee,id=id)
            assignment.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Employee Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
