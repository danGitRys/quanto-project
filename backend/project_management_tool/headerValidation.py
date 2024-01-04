from authlib import jose
from .models import Assignment, Employee
import os
from dotenv import load_dotenv

load_dotenv()

class HeaderValidation:
    def isAuthorized(request, allowedRoles) -> bool:
        """
        Description
        -----------
        Function to return boolean if the User depending on his company_role is allowed to access this data/procedure or not

        Parameters
        ----------
        request : html request
            html request
        allowedRoles : array of strings
            array of company_roles of persons that have access to the resource

        Returns
        -------
        Boolean
            If person has one of the roles: True
        """

        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        
        if authorization_header:
                # Decode token from header
                public = os.getenv('PUBLIC_KEY')
                print(authorization_header)
                token = authorization_header.split(' ')[1]
                decoded_token = jose.jwt.decode(token,key=public)
                print("access_token:")
                print(decoded_token)

                # Get employee from token
                email = decoded_token["email"]
                emp = Employee.objects.get(mail = email)
                print(emp)
                print(emp.company_role)
                    
                # Check if employee has access to this resource
                if (emp.company_role in allowedRoles):
                    return True
                elif (emp.company_role == 'Admin'):
                    return True
                else:
                    return False
        else:
            print("Error, no Authorization Header included.")
            return False
        
def isAuthorizedPersonal(request, personid) -> bool:
        """
        Description
        -----------
        Function to return boolean if the User is allowed person this data/procedure or not

        Parameters
        ----------
        request : html request
            html request
        allowedRoles : array of strings
            array of company_roles of persons that have access to the resource

        Returns
        -------
        Boolean
            If person has one of the roles: True
        """

        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        
        if authorization_header:
                # Decode token from header
                public = os.getenv('PUBLIC_KEY')
                print(authorization_header)
                token = authorization_header.split(' ')[1]
                decoded_token = jose.jwt.decode(token,key=public)

                # Get employee from token
                email = decoded_token["email"]
                emp = Employee.objects.get(mail = email)
                
                # Check if employee has access to this resource
                if (emp.company_role == 'Admin'):
                    return True
                elif (emp.id == personid):
                    return True
                else:
                    return False
        else:
            return False

def isAuthorizedForProject(request, projectid) -> bool:
        """
        Description
        -----------
        Function to return boolean if the User is allowed person this data/procedure from a specific project or not

        Parameters
        ----------
        request : html request
            html request
        allowedRoles : array of strings
            array of company_roles of persons that have access to the resource

        Returns
        -------
        Boolean
            If person has one of the roles: True
        """

        # Get header from request
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        
        if authorization_header:
                # Decode token from header
                public = os.getenv('PUBLIC_KEY')
                print(authorization_header)
                token = authorization_header.split(' ')[1]
                decoded_token = jose.jwt.decode(token,key=public)

                # Get employee from token
                email = decoded_token["email"]
                emp = Employee.objects.get(mail = email)
                
                # Check if employee has access to this resource
                if (emp.company_role == 'Admin'):
                    return True
                
                allAssignments = Assignment.objects.get.all()
                for assignment in allAssignments:
                    if assignment.fk_project == projectid and assignment.fk_employee == emp.id and assignment.role == 'Leader':
                        return True
                     
                return False
        else:
            return False
