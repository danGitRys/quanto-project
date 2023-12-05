from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Assignment
from ...middleware import timeTable

import json

@csrf_exempt
def createAssignment(request)->JsonResponse:
    response_data = {
                    "success": True,
                    "message": "Assignment created successfully.",
                }
    
    if request.method == 'GET':
       pass
       table = timeTable(1)
   


    return JsonResponse(response_data)
