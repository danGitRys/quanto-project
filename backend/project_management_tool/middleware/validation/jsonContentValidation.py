from .checkExistenceDb import *
from .enumValidation import *
import json
class jsonContentValidator:

    def team(jsonData:json)->bool:
        """Checking if the content of the given Json is valid
        Checks if the team name already exists in the Database

        Parameters
        ----------
        jsonData : json
            Json to be Checked

        Returns
        -------
        bool
            Json containing valid content or not
        """
        name = jsonData["name"]
        nameValid:bool = checkExDB.team(name)
        
        return not nameValid
    
    def assignment(jsonData:json)->bool:
        fk_project = jsonData["fk_project"]
        fK_employee = jsonData["fk_employee"]
        role = jsonData["role"]
        fk_projectValid:bool = checkExDB.project_id(fk_project)
        fK_employeeValid: bool = checkExDB.employee_id(fK_employee)
        roleValid: bool = enumValidation.assignementRole(role)
        assignmentExists:bool = checkExDB.assignemt_exists(fK_employee,fk_project)

        incorrectList = []

        if not fk_projectValid:
            incorrectList.append("Project with this Id doesnt exist")
        if not fK_employeeValid:
            incorrectList.append("Employee with this Id doesnt exist")
        if not roleValid:
            incorrectList.append("Role doesnt exist")
        if assignmentExists:
            incorrectList.append("Assignment already exists")
        
        if fk_projectValid and fK_employeeValid and role and not assignmentExists:
            return {
                "valid":True,
                "errors": incorrectList
            }
        else:
            return {
                "valid":False,
                "errors": incorrectList
            }

        


