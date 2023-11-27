from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Project
from ...middleware import validator
import json

@csrf_exempt
def deleteProject(request,id:int)->JsonResponse:
    """Endpoint for deleting an Project in the database

    Parameters
    ----------
    request : request
        Delete request
        
    id : int
        id of deleted Project

    Returns
    -------
    JsonResponse
        Json containing Results if Project was deleted successfully
    """
    
    response_data = {
            "success": True,
            "message": "Project deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Project.objects.filter(id = id).exists()
        if idExists:
            project = get_object_or_404(Project,id=id)
            project.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Project Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
