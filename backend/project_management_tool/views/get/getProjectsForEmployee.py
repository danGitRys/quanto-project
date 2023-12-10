from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Employee, Project, Assignment
from ...middleware import validator
from ...middleware import assignedProjects
import json

@csrf_exempt
def getProjectsForEmployee(request, id: int) -> JsonResponse:
    """ Endpoint for getting Projects for an Employee out of the Database
    Parameters
    ----------
    request : request
        Get Request
    id : int
        describe the path for dynamic routing 

    Returns
    -------
    JsonResponse
        if success = True 
        JSON with Data of the Projects
    """
    response_data = {
        "success": False,
        "message": "",
    }

    if request.method == 'GET':
        # Überprüfe, ob der Mitarbeiter existiert
        if not Employee.objects.filter(id=id).exists():
            response_data["success"] = False
            response_data["message"] = "Employee does not exist"
            return JsonResponse(response_data)

        # Verwende die assignedProjects-Klasse, um die SQL-Abfrage auszuführen
        projects_query = assignedProjects(id)
        projects_data = projects_query.toJsonTotal()

        if projects_data:
            response_data["success"] = True
            response_data["data"] = projects_data
        else:
            response_data["success"] = False
            response_data["message"] = "No Projects Exist for this Employee"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
