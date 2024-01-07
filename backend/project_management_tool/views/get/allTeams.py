from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired
from django.http import JsonResponse
from ...models import Team

def getAllTeams(request):
    """Endpoint for getting a list of all Teams in the Database

    Parameters
    ----------
    request : request
        get request

    Returns
    -------
    JsonResponse
        Json Containing Information about Insertion Process
    """

    response_data = {
        "success": False,
        "message": "",
    }

    allowedRoles = ['Admin', 'Employee']
    if (isTokenExpired(request)):
        if (HeaderValidation.isAuthorized(request, allowedRoles)):
            teamslist = []
            allTeams = Team.objects.all()
            for team in allTeams:
                teamslist.append(team.toJson())
            if request.method == 'GET':
                response_data = { "teams": teamslist }
        else:
            response_data["success"] = False
            response_data["message"] = "Not Authorized"
    else:
        response_data["success"] = False
        response_data["message"] = "Token expired"

    return JsonResponse(response_data)