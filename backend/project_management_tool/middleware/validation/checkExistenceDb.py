from project_management_tool.models import *
from django.db.models import Q
class checkExDB:
    def employee(checkId:str,checkMail:str)->bool:
        """Checking if a Employee already exists in the database

        Parameters
        ----------
        checkId : str
            EmployeeId to be checked
        checkMail : str
            Email to be checked

        Returns
        -------
        bool
            Employee existing with these values or not
        """
        return Employee.objects.filter(Q(emp_id=checkId) | Q(mail=checkMail)).exists()
    
    def team(checkName:str)->bool:
        """Checking if a Team already exists in the database 
        with the given Team Name

        Parameters
        ----------
        checkName : str
            teamName to be checked

        Returns
        -------
        bool
            Team exisiting with these values or not
        """
        return Team.objects.filter(name=checkName).exists()

    def project_id(checkId:int)->bool:
        return Project.objects.filter(id=checkId).exists()
    
    def employee_id(checkId:int)->bool:
        return Employee.objects.filter(id=checkId).exists()
    
    def assignemt_exists(employeeId:int,projectId:int)->bool:
        return Assignment.objects.filter(Q(fk_project=projectId) & Q(fk_employee=employeeId))
    
    

    
