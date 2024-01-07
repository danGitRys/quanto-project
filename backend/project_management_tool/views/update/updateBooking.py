from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Booking
from ...middleware import validator
import json


@csrf_exempt
def updateBooking(request, booking_id) -> JsonResponse:
    """Endpoint for updating a Booking in the database

    Parameters
    ----------
    request : HttpRequest
        PUT request
    booking_id : int
        ID of the booking to be updated

    Returns
    -------
    JsonResponse
        JSON containing results if the booking update was successful
    """
    if request.method == 'PUT':
        try:
            # Load JSON data out of the request into a Python dictionary
            request_data = json.loads(request.body)
            # Check if data is valid via the validator
            is_validResult = validator.booking(request_data)
            is_valid = is_validResult["valid"]
            errors = is_validResult["errors"]
            print(errors)
            print(is_valid)

            if is_valid:
                # Retrieve the existing booking from the database
                existing_booking = Booking.objects.get(id=booking_id)

                
                existing_booking.start = request_data["start"]
                existing_booking.end = request_data["end"]
                

                # Save the updated data back to the database
                existing_booking.save()

                response_data = {
                    "success": True,
                    "message": "Booking updated successfully.",
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
            "error": "Invalid HTTP method. Only PUT is allowed.",
        }

    return JsonResponse(response_data)
