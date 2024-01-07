from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from ...models import Employee
import json
from ...middleware import validator
from ...middleware.validation.jsonFormValidator import formValidator
from ...middleware.validation import checkExistenceDb
@method_decorator(csrf_exempt, name='dispatch')

class EmployeeView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Employee.objects.filter(id=id_param).exists()
        if idExists:
            employee = get_object_or_404(Employee, id=id_param)
            employeeJson = employee.toJson()
            response_data["success"] = True
            response_data["data"] = employeeJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Employee with this Id"
    
        return JsonResponse(response_data)
        return HttpResponse("Get")
    
    def post(self,request ,*args, **kwargs):
        try:
            request_data = json.loads(request.body)
            print(request_data)
            print("called")
            is_valid = validator.employee((request_data))

            if is_valid:
                new_emp_id = request_data["emp_id"]
                new_forename = request_data["forename"]
                new_surname = request_data["surname"]
                new_mail = request_data["email"]
                new_phone = request_data["phone"]
                new_fk_team_id = request_data["fk_team_id"]
                new_team_role = request_data["team_role"]

                if(checkExistenceDb.checkExDB.employee(new_emp_id,new_mail)):
                     print("Person exists already, still continuing")

                new_employee = Employee(emp_id = new_emp_id,forename = new_forename,surname = new_surname,mail=new_mail,phone=new_phone,fk_team_id = new_fk_team_id,team_roll=new_team_role)
                new_employee.save()

                response_data = {
                    "success": True,
                    "message": "Employee created successfully.",
                }
            else:
                response_data = {
                    "success": False,
                    "error": "Invalid JSON format or missing required fields.",
                }
        except json.JSONDecodeError:
            print("decode error")
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
            "message": "Employee deleted successfully.",
            }
        id_param = kwargs.get('id')
        idExists:bool =  Employee.objects.filter(id = id).exists()
        if idExists:
            employee = get_object_or_404(Employee,id=id)
            employee.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Employee Exists with this Id"
        return JsonResponse(response_data)