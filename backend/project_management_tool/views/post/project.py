from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Project
from ...middleware import *
import json

@csrf_exempt
def createProject(request)->JsonResponse:
    """Endpoint to create a new Project in the database

    Parameters
    ----------
    request : request
        post reqeust

    Returns
    -------
    JsonPesponse
        Json Containing information about insertion success
    """
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_valid = validator.project(request_data)
            print(is_valid)
            if is_valid["valid"]:
               
                new_p_id = request_data["p_id"]
                new_name = request_data["projectname"]
                new_company = request_data["customername"]
                new_start_date = request_data["start_date"]
                new_end_date = request_data["end_date"]
                new_fk_creator = request_data["fk_creator"]
                new_creation_date = request_data["creation_date"]
                newProject = Project(p_id = new_p_id,name=new_name,company=new_company,start_date=new_start_date,end_date=new_end_date,fk_creator=new_fk_creator,creation_date=new_creation_date)
                newProject.save()

                response_data = {
                    "success": True,
                    "message": "Project created successfully.",
                    "data": { 
                        "projectid": newProject.id,
                    },
                }
            else:
                response_data = {
                    "success": False,
                    "error": is_valid["errors"],
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
