from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired
from django.http import JsonResponse
from ...models import Team

def getTeamRoles(request):
    """Endpoint for getting a List of all Teamroles

    Parameters
    ----------
    request : request
        post request

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
        response_data["success"] = False
        response_data["message"] = "Token expired"
        
    else:
        if (HeaderValidation.isAuthorized(request, allowedRoles)):
            rolesList = ["Teamleader", "Member"]
            if request.method == 'GET':
                response_data = { "roles": rolesList }
        else:
            response_data["success"] = False
            response_data["message"] = "Not Authorized"


    return JsonResponse(response_data)