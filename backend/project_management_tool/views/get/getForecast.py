from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Forecast
from ...middleware import validator
import json


@csrf_exempt
def getForecast(request, id: int) -> JsonResponse:
    """ Endpoint for getting Forecast out of the Database
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
        JSON with Data of the Forecast
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Forecast.objects.filter(id=id).exists()
        if idExists:
            forecast = get_object_or_404(Forecast, id=id)
            forecastJson = forecast.toJson()
            response_data["success"] = True
            response_data["data"] = forecastJson
        else:
            response_data["success"] = False
            response_data["message"] = "No  Forecast with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
