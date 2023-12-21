from authlib import jose
from .models import Employee
import os
from dotenv import load_dotenv

load_dotenv()

class HeaderValidation:
    def isAuthorized(authorization_header, allowedRoles) -> bool:
        """
        Description
        -----------
        Function to return boolean if the User is allowed to access this data/procedure or not

        Parameters
        ----------
        authorization_header : Authorization Header with 'Bearer Authentication'
            Get Request Header
        allowedRoles : array of strings
            array of company_roles of persons that have access to the resource

        Returns
        -------
        Boolean
            If person has one of the roles: True
        """
        
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
                else:
                    return False
        else:
            return False
