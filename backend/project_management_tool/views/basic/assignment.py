from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from ...models import Assignment
import json
from ...middleware import validator
@method_decorator(csrf_exempt, name='dispatch')

class AssignmentView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Assignment.objects.filter(id=id_param).exists()
        if idExists:
            assignment = get_object_or_404(Assignment, id=id_param)
            assignmentJson = assignment.toJson()
            response_data["success"] = True
            response_data["data"] = assignmentJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Booking Entry with this Id"
        

        return JsonResponse(response_data)
        return HttpResponse("Get")

    def post(self,request ,*args, **kwargs):
        try:
            print(request)
            request_data = json.loads(request.body)
            validationResult = validator.assignment(request_data)
            is_valid = validationResult["valid"]
            validation_Errors = validationResult["errors"]
            print(is_valid)
            print(validation_Errors)

            if is_valid:
                new_fk_project = request_data["fk_project"]
                new_fk_employee = request_data["fk_employee"]
                new_role = request_data["role"]
                newAssignment = Assignment(fk_project=new_fk_project,fk_employee=new_fk_employee,role=new_role)
                newAssignment.save()
                

                response_data = {
                    "success": True,
                    "message": "Assignment created successfully.",
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
            "message": "Assignment deleted successfully.",
            }
        id_param = kwargs.get('id')
        idExists:bool =  Assignment.objects.filter(id = id_param).exists()
        if idExists:
            assignment = get_object_or_404(Assignment,id=id_param)
            assignment.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Assignment Exists with this Id"
        return JsonResponse(response_data)
  