from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee,Project,Assignment
from ...middleware import validator
import json


@csrf_exempt
def getEmployeesToProjectId(request, id: int) -> JsonResponse:
    
    response_data = {
        "success": False,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Project.objects.filter(id=id).exists()
        if idExists:
            assignments = Assignment.objects.filter(fk_project=id).all()
            employeeIdList = []
            for assignment in assignments:
                employeeIdList.append(assignment.fk_employee)
            employees = Employee.objects.filter(id__in=employeeIdList).all()
            employeeList = []
            for employee in employees:
                employeeList.append(employee.toJson())
            response_data["success"] = True
            response_data["data"] = employeeList
        else:
            response_data["success"] = False
            response_data["message"] = "No Position Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)