from ..models import Employee
from django.db.models import Q
class checkExDB:
    def employee(checkId:str,checkMail:str)->bool:
        return Employee.objects.filter(Q(emp_id=checkId) | Q(mail=checkMail)).exists()

    