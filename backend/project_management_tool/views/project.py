from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Project
from ..jsonValidator import validator
import json

@csrf_exempt
def createProject(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_valid = validator.project(request_data)

            if is_valid:
               
                new_p_id = request_data["p_id"]
                new_name = request_data["name"]
                new_company = request_data["company"]
                new_start_date = request_data["start_date"]
                new_end_date = request_data["end_date"]
                new_fk_creator = request_data["fk_creator"]
                new_creation_date = request_data["creation_date"]
                newProject = Project(p_id = new_p_id,name=new_name,company=new_company,start_date=new_start_date,end_date=new_end_date,fk_creator=new_fk_creator,creation_date=new_creation_date)
                newProject.save()

                response_data = {
                    "success": True,
                    "message": "Project created successfully.",
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
