from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Booking
from ...middleware import validator
import json

@csrf_exempt
def deleteBooking(request,id:int)->JsonResponse:
    """Endpoint for deleting a Booking record from the database

    Parameters
    ----------
    request : request
        Delete request
        
    id : int
        id of deleted Booking record

    Returns
    -------
    JsonResponse
        Json containing Results if Booking was deleted successfully
    """
    
    response_data = {
            "success": True,
            "message": "Booking deleted successfully.",
            }
    if request.method == 'DELETE':
        idExists:bool =  Booking.objects.filter(id = id).exists()
        if idExists:
            booking = get_object_or_404(Booking,id=id)
            booking.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"
      

        
           
    
   


    return JsonResponse(response_data)
