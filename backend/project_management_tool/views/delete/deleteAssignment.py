from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Assignment
from ...middleware import validator
import json

@csrf_exempt
def deleteAssignment(request,assignment_id)->JsonResponse:
    
    response_data = {
            "success": True,
            "message": "Assignment deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Assignment.objects.filter(id = assignment_id).exists()
        if idExists:
            assignment = get_object_or_404(Assignment,id=assignment_id)
            assignment.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Assignment Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
