from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from ...models import Booking
import json
from ...middleware import validator
@method_decorator(csrf_exempt, name='dispatch')

class BookingView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Booking.objects.filter(id=id).exists()
        if idExists:
            booking = get_object_or_404(Booking, id=id)
            bookingJson = booking.toJson()
            response_data["success"] = True
            response_data["data"] = bookingJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Entry with this Id"
        
        return JsonResponse(response_data)
        return HttpResponse("Get")
    
    def post(self,request ,*args, **kwargs):
        try:
            request_data = json.loads(request.body)
            is_validResult = validator.booking(request_data)
            is_valid = is_validResult["valid"]
            print(is_valid)
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
        return JsonResponse(response_data)
    
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    def delete(self, *args, **kwargs):
        response_data = {
            "success": True,
            "message": "Booking deleted successfully.",
            }
        id_param = kwargs.get('id')
        idExists:bool =  Booking.objects.filter(id = id).exists()
        if idExists:
            booking = get_object_or_404(Booking,id=id)
            booking.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Exists with this Id"
        return JsonResponse(response_data)