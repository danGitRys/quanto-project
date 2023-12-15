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


    # Project Checks
    def project_id(checkId:int)->bool:
        return Project.objects.filter(id=checkId).exists()
    
    def project_p_id(checkId:int)->bool:
        return Project.objects.filter(p_id=checkId).exists()
    
    def project_name(checkName:int)->bool:
        return Project.objects.filter(name=checkName).exists()
    

    # Employee Checks
    def employee_id(checkId:int)->bool:
        return Employee.objects.filter(emp_id=checkId).exists()
    
    def employee_mail(checkMail:int)->bool:
        return Employee.objects.filter(mail=checkMail).exists()
    
    def employee_phone(checkPhone:int)->bool:
        return Employee.objects.filter(phone=checkPhone).exists()
    

    # Assignment Checks
    def assignemt_exists(employeeId:int,projectId:int)->bool:
        return Assignment.objects.filter(Q(fk_project=projectId) & Q(fk_employee=employeeId)).exists()
    

    # Position Checks
    def position_id(position:int)->bool:
        return Positon.objects.filter(id=position).exists()
    
    def position_position_id(position:str)->bool:
        return Positon.objects.filter(position_id=position).exists()

    def position_position_id_project(position:str,project:int)->bool:
        return Positon.objects.filter(Q(position_id=position) & Q(fk_project=project)).exists()
    

    # Position Checks
    def booking_exists(employeeId:int,positionId:int,startTime:str,endTime:str,pauseTime:int)->bool:
        return Booking.objects.filter(Q(fk_employee=employeeId) & Q(fK_position=positionId) & Q(start=startTime) & Q(end=endTime) & Q(pause=pauseTime)).exists()
    
    
    

    
