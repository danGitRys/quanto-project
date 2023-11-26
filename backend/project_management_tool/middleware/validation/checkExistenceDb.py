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
        """Checking if a Project with this Id exists

        Parameters
        ----------
        checkId : int
            Project Id to be checked

        Returns
        -------
        bool
            Project with this Id existing or not
        """
        return Project.objects.filter(id=checkId).exists()
    
    def employee_id(checkId:int)->bool:
        """Check if a Employee with this Id exists

        Parameters
        ----------
        checkId : int
            Employee id to be checked

        Returns
        -------
        bool
            Employee with this id exists or not
        """
        return Employee.objects.filter(id=checkId).exists()
    
    def assignemt_exists(employeeId:int,projectId:int)->bool:
        """Check if a assignment with these paramters exists

        Parameters
        ----------
        employeeId : int
            Employee Id of the Assignment
        projectId : int
            Project Id of the Assignment

        Returns
        -------
        bool
            Assignment with this Id exists or not
        """
        return Assignment.objects.filter(Q(fk_project=projectId) & Q(fk_employee=employeeId)).exists()
    
    def position_id(position:int)->bool:
        """Check if a position with this id exists

        Parameters
        ----------
        position : int
            Position Id to be Checked

        Returns
        -------
        bool
            Position with this Id exists or not
        """
        return Positon.objects.filter(id=position).exists()
    
    def booking_exists(employeeId:int,positionId:int,startTime:str,endTime:str,pauseTime:int)->bool:
        """Check if a booking with these Parameters exists

        Parameters
        ----------
        employeeId : int
            employee Id to be checked
        positionId : int
            positionId to be checked
        startTime : str
            startTime to be checked
        endTime : str
            endTime to be checked
        pauseTime : int
            pauseTime to be checked

        Returns
        -------
        bool
            Assignment with these combination of parameters exists or not
        """
        return Booking.objects.filter(Q(fk_employee=employeeId) & Q(fK_position=positionId) & Q(start=startTime) & Q(end=endTime) & Q(pause=pauseTime))
    
    
    

    
