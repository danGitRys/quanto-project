from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Forecast
from ..middleware import validator
import json

@csrf_exempt
def createForecast(request)->JsonResponse:
    """Endpoint to create a Forecast Entry in the Database

    Parameters
    ----------
    request : request
        post request

    Returns
    -------
    JsonResponse
        Json Containing Information about insertion Process
    """
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_valid = validator.forecast(request_data)

            if is_valid:
               
                new_fk_employee = request_data["fk_employee"]
                new_fk_position = request_data["fk_position"]
                new_start = request_data["start"]
                new_end = request_data["end"]
                new_info = request_data["info"]
                newForecast = Forecast(fk_employee=new_fk_employee,fk_position=new_fk_position,start=new_start,end=new_end,info=new_info)

                response_data = {
                    "success": True,
                    "message": "Forecast created successfully.",
                }
            else:
                response_data = {
                    "success": False,
                    "error": "Invalid JSON format or missing required fields.",
                }
        except json.JSONDecodeError:
            response_data = {
                "success": False,
                "error": "Invalid JSON format.",
            }
    else:
        response_data = {
            "success": False,
            "error": "Invalid HTTP method. Only POST is allowed.",
        }

    return JsonResponse(response_data)
