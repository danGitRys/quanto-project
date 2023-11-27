from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Forecast
from ...middleware import validator
import json

@csrf_exempt
def deleteForecast(request,id:int)->JsonResponse:
    """Endpoint for deleting an Forecast in the database

    Parameters
    ----------
    request : request
        Delete request
        
    id : int
        id of deleted Forecast

    Returns
    -------
    JsonResponse
        Json containing Results if Forecast was deleted successfully
    """
    
    response_data = {
            "success": True,
            "message": "Forecast deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Forecast.objects.filter(id = id).exists()
        if idExists:
            forecast = get_object_or_404(Forecast,id=id)
            forecast.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Forecast Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
