from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Booking
from ...middleware import validator
import json


@csrf_exempt
def createBooking(request) -> JsonResponse:
    """Enpoint for creating a Booking in the database

    Parameters
    ----------
    request : request
        Get or Post request

    Returns
    -------
    JsonResponse
        Json Containing Results if Booking creation was successfull
    """
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_validResult = validator.booking(request_data)
            is_valid = is_validResult["valid"]
            errors = is_validResult["errors"]
            print(errors)

            if is_valid:

                new_fk_employee = request_data["fk_employee"]
                new_fk_position = request_data["fk_position"]
                new_start = request_data["start"]
                new_end = request_data["end"]
                new_pause = request_data["pause"]
                # new_time = request_data["time"]
                newBooking = Booking(fk_employee=new_fk_employee, fK_position=new_fk_position,
                                     start=new_start, end=new_end, pause=new_pause)  # ,time=new_time
                newBooking.save()

                response_data = {
                    "success": True,
                    "message": "Booking created successfully.",
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
