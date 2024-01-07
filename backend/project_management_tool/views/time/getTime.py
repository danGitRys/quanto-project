from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Forecast
from ...middleware import validator
import json
from datetime import datetime




#Remove?


@csrf_exempt
def getTime(request) -> JsonResponse:
    """Backendroute to get the current Date and Time

    Parameters
    ----------
    request : _type_
        get request

    Returns
    -------
    JsonResponse
        Json containing the success status and the current Date
    """
   
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        now = datetime.now()
        response_data["date"]=now
       
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
