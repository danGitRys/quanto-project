from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Assignment
from ...middleware import assignedProjects

import json

@csrf_exempt
def getAssignedProjects(request,id: int)->JsonResponse:
    response_data = {
                    "success": False,
                    "message": "Error Invalid Method",
                }
    
    if request.method == 'GET':
       pass
       projects = assignedProjects(id)
       jsonList = projects.toJsonTotal()
       print(jsonList)
       response_data["data"] = jsonList
       response_data["success"] = True
       response_data["message"] = "Success"
   


    return JsonResponse(response_data)
