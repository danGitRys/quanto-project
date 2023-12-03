from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Assignment
from ...middleware import validator
import json


@csrf_exempt
def getAssignment(request, id: int) -> JsonResponse:
    """ Endpoint for getting Assignment Data out of the Database
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
        JSON with Data of the Assignment Entry
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Assignment.objects.filter(id=id).exists()
        if idExists:
            assignment = get_object_or_404(Assignment, id=id)
            assignmentJson = assignment.toJson()
            response_data["success"] = True
            response_data["data"] = assignmentJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Entry with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
