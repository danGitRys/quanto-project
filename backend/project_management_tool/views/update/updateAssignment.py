from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Assignment
from ...middleware.validation.jsonUpdateFormValidation import jsonUpdateFormValidation
from ...middleware.validation.jsonUpateConentValidation import jsonUpdateConentValidation
import json
@csrf_exempt
def updateAssignment(request,assignment_id):
    if request.method == 'PUT':
        try:
            print("put")
            # Your PUT logic here
            response_data = {
                "success": True,
                "message": "Assignment updated successfully.",
            }
            idExists:bool =  Assignment.objects.filter(id = assignment_id).exists()

            if idExists:
                print("Id Exists")
                request_data = json.loads(request.body)
                print(request_data)
                validParameterForm:bool = jsonUpdateFormValidation.assignment(request_data.keys())
                result = jsonUpdateConentValidation.assignment(request_data,assignment_id)
                print(result)
                print(validParameterForm)
                print("here")
            else:
                print("Id doenst Exist")
        
        except json.JSONDecodeError:
            response_data = {
                "success": False,
                "error": "Invalid JSON format.",
            }


    else:
        print("invalid")
        response_data = {
            "success": False,
            "message": "Invalid request method. Only PUT is allowed.",
        }

    return JsonResponse(response_data)
