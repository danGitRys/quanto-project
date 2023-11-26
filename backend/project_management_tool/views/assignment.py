from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Assignment
from ..middleware import validator
import json

@csrf_exempt
def createAssignment(request)->JsonResponse:
    """Enpoint for creating an Assignment in the database

    Parameters
    ----------
    request : request
        Get or Post request

    Returns
    -------
    JsonResponse
        Json Containing Results if Assignment creatin was successfull
    """
    if request.method == 'POST':
        try:
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
    else:
        response_data = {
            "success": False,
            "error": "Invalid HTTP method. Only POST is allowed.",
        }

    return JsonResponse(response_data)
