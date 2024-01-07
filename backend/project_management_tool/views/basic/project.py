from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ...models import Project
from django.shortcuts import get_object_or_404
from ...middleware import validator
from ...middleware.validation.headerValidation import HeaderValidation
from ...middleware.validation.tokenExpirationCheck import isTokenExpired

@method_decorator(csrf_exempt, name='dispatch')

class ProjectView(View):
    def get(self,*args, **kwargs):
        response_data = {
        "success": True,
        "message": "",
        }
        print(self)
        print(args)
        print(kwargs)
        allowedRoles = ['Admin']
        id_param = kwargs.get('id')
        if (isTokenExpired(args[0])==False):
        
            if (HeaderValidation.isAuthorized(args[0], allowedRoles)):
                idExists: bool = Project.objects.filter(id=id_param).exists()
                if idExists:
                    project = get_object_or_404(Project, id=id_param)
                    projectJson = project.toJson()
                    response_data["success"] = True
                    response_data["data"] = projectJson
                else:
                    response_data["success"] = False
                    response_data["message"] = "No Project exists with this Id"
            else:
                 response_data["success"] = False
                 response_data["message"] = "Not Authorized"
        else:
            response_data["success"] = False
            response_data["message"] = "Token expired"


        

        return JsonResponse(response_data)
        return HttpResponse("Get")
    
    def post(self,request ,*args, **kwargs):
        response_data = {
        "success": False,
        "message": "",
        }
        try:
            request_data = json.loads(request.body)
            is_valid = validator.project(request_data)

            if is_valid:
               
                new_p_id = request_data["p_id"]
                new_name = request_data["name"]
                new_company = request_data["company"]
                new_start_date = request_data["start_date"]
                new_end_date = request_data["end_date"]
                new_fk_creator = request_data["fk_creator"]
                new_creation_date = request_data["creation_date"]
                newProject = Project(p_id = new_p_id,name=new_name,company=new_company,start_date=new_start_date,end_date=new_end_date,fk_creator=new_fk_creator,creation_date=new_creation_date)
                newProject.save()

                response_data = {
                    "success": True,
                    "message": "Project created successfully.",
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
    
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    def delete(self, *args, **kwargs):
        id_param = kwargs.get('id')
        response_data = {
            "success": True,
            "message": "Project deleted successfully.",
            }
        
        idExists:bool =  Project.objects.filter(id = id_param).exists()
        if idExists:
            project = get_object_or_404(Project,id=id)
            project.delete()
            response_data["success"] = True
        else:
            response_data["success"] = False
            response_data["message"] = "No Project Exists with this Id"
        

        return JsonResponse(response_data)