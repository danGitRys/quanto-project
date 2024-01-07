from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Project
from ...middleware import validator
import json


@csrf_exempt
def getAllProjects(request) -> JsonResponse:
    """ Endpoint for getting Project out of the Database
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
        JSON with Data of the Project
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
            projects = Project.objects.all()
            project_list = [project.toJson() for project in projects]
            response_data["success"] = True
            response_data["data"] = project_list
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
