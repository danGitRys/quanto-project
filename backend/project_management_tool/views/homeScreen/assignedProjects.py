from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Assignment
from ...middleware import assignedProjects

import json

@csrf_exempt
def getAssignedProjects(request,id: int)->JsonResponse:
    response_data = {
                    "success": True,
                    "message": "Assignment created successfully.",
                }
    
    if request.method == 'GET':
       pass
       projects = assignedProjects(id)
       projects.executeQuery()
   


    return JsonResponse(response_data)
