# Importieren der benötigten Django-Module und benutzerdefinierten Klassen
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Employee, Project, Assignment
from ...middleware import validator
from ...middleware import assignedProjects
import json


# Dekorator, um CSRF-Schutz für die Funktion zu deaktivieren
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
    # Initialisierung der Antwortdaten
    response_data = {
        "success": False,
        "message": "",
    }

    # Überprüfen, ob die Anfrage eine GET-Anfrage ist
    if request.method == 'GET':
        # Überprüfe, ob der Mitarbeiter existiert
        if not Employee.objects.filter(id=id).exists():
            response_data["success"] = False
            response_data["message"] = "Employee does not exist"
            return JsonResponse(response_data)

        # Verwende die assignedProjects-Klasse, um die SQL-Abfrage auszuführen
        projects_query = assignedProjects(id)
        projects_data = projects_query.toJsonTotal()

        # Überprüfen, ob Projektdaten vorhanden sind
        if projects_data:
            response_data["success"] = True
            response_data["data"] = projects_data
        else:
            response_data["success"] = False
            response_data["message"] = "No Projects Exist for this Employee"
    else:
        # Fehlerfall: Ungültige Anfragemethode
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    # Rückgabe der Antwortdaten als JsonResponse
    return JsonResponse(response_data)
