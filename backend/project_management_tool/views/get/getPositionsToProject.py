from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Positon,Project
from ...middleware import validator
import json
from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired


@csrf_exempt
def getPositionsToProjectId(request, id: int) -> JsonResponse:
    
    response_data = {
        "success": False,
        "message": "",
    }
    if request.method == 'GET':
         if (isTokenExpired(request)==False):
            allowedRoles = ['Admin']
            if (HeaderValidation.isAuthorized(request, allowedRoles)):
                idExists: bool = Project.objects.filter(id=id).exists()
                if idExists:
                    positions = Positon.objects.filter(fk_project=id).all()
                    positionList = []
                    for position in positions:
                        positionList.append(position.toJson())
                    response_data["success"] = True
                    response_data["data"] = positionList
                else:
                    response_data["success"] = False
                    response_data["message"] = "No Position Exists with this Id"
            else:
                 response_data["success"] = False
                 response_data["message"] = "Not Authorized"
         else:
            response_data["success"] = False
            response_data["message"] = "Token expired"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)