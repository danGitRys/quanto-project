from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Team
from ...middleware import validator
import json


@csrf_exempt
def getTeam(request, id) -> JsonResponse:

    response_data = {
        "success": True,
        "message": "",
    }
    if request.method == 'GET':
        idExists: bool = Team.objects.filter(id=id).exists()
        if idExists:
            team = get_object_or_404(Team, id=id)
            teamJson = team.toJson()
            response_data["success"] = True
            response_data["data"] = teamJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Team Exists with this Id"
    else:
        response_data["success"] = False
        response_data["message"] = "Invalid Method"

    return JsonResponse(response_data)
