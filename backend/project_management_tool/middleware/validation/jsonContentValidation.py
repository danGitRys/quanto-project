from .checkExistenceDb import *
from .enumValidation import *
from .dateValidator import *
from .otherValidaton import *
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
    
    def booking(jsonData:json)->bool:
        fk_employee = jsonData["fk_employee"]
        fk_position = jsonData["fk_position"]
        start = jsonData["start"]
        end = jsonData["end"]
        pause = jsonData["pause"]
        fk_employee_Valid:bool = checkExDB.employee_id(fk_employee)
        fk_positionValid:bool = checkExDB.position_id(fk_position)
        startValid:bool = dateValidator.validate_datetime(start)
        endValid:bool = dateValidator.validate_datetime(end)
        pauseValid:bool = otherValidation.validPauseInteger(pause)
        bookingAlreadyExists:bool = checkExDB.booking_exists(fk_employee,fk_position,start,end,pause)

        incorrectList = []

        if not fk_employee_Valid:
            incorrectList.append("Employee with this Id doesnt Exist")
        if not fk_positionValid:
            incorrectList.append("Position with this Id doesnt Exist")
        if not startValid:
            incorrectList.append("DateFormat for start Date invalid")
        if not endValid:
            incorrectList.append("Dateformat for end Date invalid")
        if not pauseValid:
            incorrectList.append("Pause Value incorretc, may not be under null")
        if bookingAlreadyExists:
            incorrectList.append("Booking Already exists")
        
        if startValid and endValid and pauseValid:

            differenceResult = dateValidator.validateBookingTimes(start,end,pause)
            differenceResultValid = differenceResult["valid"]
            differenceResultErrors = differenceResult["errors"]
            
            if differenceResultValid:

                if fk_employee_Valid and fk_employee_Valid and differenceResultValid and not bookingAlreadyExists:

                    return {
                        "valid":True,
                        "errors": incorrectList,
                    }
                else:
                    return {
                        "valid":False,
                        "errors": incorrectList + differenceResultErrors
                    }
            
            else: 
                return {
                        "valid":False,
                        "errors": incorrectList + differenceResultErrors
                    }
        
        else:
            return {
                        "valid":False,
                        "errors": incorrectList
                    }
        

        







        


