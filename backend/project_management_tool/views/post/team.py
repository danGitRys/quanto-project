from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import Team
from ...middleware import validator
import json

@csrf_exempt
def createTeam(request)->JsonResponse:
    """Endpoint for creating a Team in the Database

    Parameters
    ----------
    request : request
        post request

    Returns
    -------
    JsonResponse
        Json Containing Information about Insertion Process
    """
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            is_valid = validator.team(request_data)

            if is_valid:
                new_team_name = request_data["name"]
                new_team_info = request_data["info"]
                new_team = Team(name=new_team_name, info=new_team_info)
                new_team.save()

                response_data = {
                    "success": True,
                    "message": "Team created successfully.",
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

def getTeams(request):
    teamslist = []
    allTeams = Team.objects.all()
    for team in allTeams:
        teamslist.append(team.toJson())
    if request.method == 'GET':
        response_data = { "teams": teamslist }
    return JsonResponse(response_data)

def getTeamRoles(request):
    rolesList = ["Teamleader", "Member"]
    if request.method == 'GET':
        response_data = { "roles": rolesList }
    return JsonResponse(response_data)
        
