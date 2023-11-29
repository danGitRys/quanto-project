from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Booking
from ...middleware import validator
import json


@csrf_exempt
def getBooking(request, id: int) -> JsonResponse:
    """ Endpoint for getting Booking Data out of the Database
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
        JSON with Data of the Booking Entry
    """
    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Booking.objects.filter(id=id).exists()
        if idExists:
            booking = get_object_or_404(Booking, id=id)
            bookingJson = booking.toJson()
            response_data["success"] = True
            response_data["data"] = bookingJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Entry with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
