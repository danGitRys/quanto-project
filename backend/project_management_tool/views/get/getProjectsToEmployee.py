from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Employee, Project, Assignment
from ...middleware import validator
import json

@csrf_exempt
def getPositionsToProjectId(request, id: int) -> JsonResponse:

    response_data = {
        "success": False,
        "message": "",
    }

    if request.method == 'GET':
        project_exists = Project.objects.filter(id=id).exists()
        if project_exists:
            employee_list = Employee.objects.filter(assignments__fk_project=id).values('id', 'p_id', 'name', 'company', 'start_date', 'end_date', 'fk_creator', 'creation_date')
            response_data["success"] = True
            response_data["data"] = list(employee_list)
        else:
            response_data["success"] = False
            response_data["message"] = "No Position Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
