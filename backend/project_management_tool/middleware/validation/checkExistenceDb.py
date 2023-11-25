from project_management_tool.models import *
from django.db.models import Q
class checkExDB:
    def employee(checkId:str,checkMail:str)->bool:
        return Employee.objects.filter(Q(emp_id=checkId) | Q(mail=checkMail)).exists()
    
    def team(checkName:str)->bool:
        return Team.objects.filter(name=checkName).exists()
    

    