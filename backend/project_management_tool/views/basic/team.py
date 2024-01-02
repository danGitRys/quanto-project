from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ...models import Team
from django.shortcuts import get_object_or_404
from ...middleware import validator
@method_decorator(csrf_exempt, name='dispatch')

class TeamView(View):
    def get(self, *args, **kwargs):
        response_data = {
        "success": False,
        "message": "",
        }
        id_param = kwargs.get('id')
        idExists: bool = Team.objects.filter(id=id_param).exists()
        if idExists:
            team = get_object_or_404(Team, id=id_param)
            teamJson = team.toJson()
            response_data["success"] = True
            response_data["data"] = teamJson
        else:
            response_data["success"] = False
            response_data["message"] = "No Team Exists with this Id"
        return JsonResponse(response_data)

    def post(self,request, *args, **kwargs):
        response_data = {
        "success": False,
        "message": "",
        }
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
        
        return JsonResponse(response_data)
        
        return HttpResponse('Post')
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    def delete(self, *args, **kwargs):
        id_param = kwargs.get('id')
        response_data = {
            "success": True,
            "message": "Team deleted successfully.",
            }
   
        idExists:bool =  Team.objects.filter(id = id_param).exists()
        if idExists:
            team = get_object_or_404(Team,id=id_param)
            team.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Team Exists with this Id"
   
      

    

        return JsonResponse(response_data)