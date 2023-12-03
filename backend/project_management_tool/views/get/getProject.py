from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Project
from ...middleware import validator
import json


@csrf_exempt
def getProject(request, id:int) -> JsonResponse:
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
        idExists: bool = Project.objects.filter(id=id).exists()
        if idExists:
            project = get_object_or_404(Project, id=id)
            projectJson = project.toJson()
            response_data["success"] = True
            response_data["data"] = projectJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Project Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
