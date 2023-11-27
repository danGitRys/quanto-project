from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Team
from ...middleware import validator
import json

@csrf_exempt
def deleteTeam(request,id:int)->JsonResponse:
    """Endpoint for deleting an Team in the database

    Parameters
    ----------
    request : request
        Delete Request
        
    id : int
        id of deleted Team

    Returns
    -------
    JsonResponse
        Json containing Results if Team was deleted successfully
    """
    
    response_data = {
            "success": True,
            "message": "Team deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Team.objects.filter(id = id).exists()
        if idExists:
            team = get_object_or_404(Team,id=id)
            team.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Team Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
