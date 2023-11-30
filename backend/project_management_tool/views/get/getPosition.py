from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Positon
from ...middleware import validator
import json


@csrf_exempt
def getPosition(request, id: int) -> JsonResponse:
    """ Endpoint for getting Positon out of the Database
    Parameters
    ----------
    request : request
        Get Request
    id : int
        _description_

    Returns
    -------
    JsonResponse
        if success = True 
        JSON with Data of the Position
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Positon.objects.filter(id=id).exists()
        if idExists:
            position = get_object_or_404(Positon, id=id)
            positionJson = position.toJson()
            response_data["success"] = True
            response_data["data"] = positionJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Position Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
