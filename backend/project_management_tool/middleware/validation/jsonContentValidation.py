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
    
    def postion(jsonData:json)->json:
        positon_id = jsonData["position_id"]
        fk_project = jsonData["fk_project"]
        rate = jsonData["rate"]
        wd = jsonData["wd"]
        # volume_total = jsonData["volume_total"]
        # volume_remaining = jsonData["volume_remaining"]
        start_date = jsonData["start_date"]
        end_date = jsonData["end_date"]
        positon_id_valid:bool = checkExDB.position_position_id(positon_id)
        print(positon_id_valid)
        fk_project_valid:bool = checkExDB.project_id(fk_project)
        wd_valid:bool = otherValidation.can_convert_to_float(wd)
        rate_valid:bool = otherValidation.can_convert_to_float(rate)
        # volume_total_valid:bool = otherValidation.can_convert_to_float(volume_total)
        # volume_remaining_valid:bool = otherValidation.can_convert_to_float(volume_remaining)
        start_date_valid = dateValidator.validate_date(start_date)
        end_date_valid = dateValidator.validate_date(end_date)

        incorrecList:list = []
        if positon_id_valid:
            incorrecList.append("Position with this id already exists")
        if not fk_project_valid:
            incorrecList.append("Project with this id doesnt exist")
        if not wd_valid:
            incorrecList.append("WD invalid")
        if not rate_valid:
            incorrecList.append("Rate not valid")
        # if not volume_total_valid:
        #     incorrecList.append("Volume total not valid")
        # if not volume_remaining_valid:
        #     incorrecList.append("Volume Remaining invalid")
        if not start_date_valid:
            incorrecList.append("Start Date invalid")
        if not end_date_valid:
            incorrecList.append("End Date not valid")
        
        if len(incorrecList) == 0:
            if not checkExDB.position_position_id_project(positon_id,fk_project):
                 return {
                        "valid":True,
                        "errors": incorrecList,
                    }
            else:
                incorrecList.append("Combination of fk_project and project_id already exists")
                return {
                        "valid":False,
                        "errors": incorrecList
                    }
        
        else:
             return {
                        "valid":False,
                        "errors": incorrecList
                    }

    def project(jsonData:json)->bool:
        p_id = jsonData["p_id"]
        projectname = jsonData["projectname"]
        start_date = jsonData["start_date"]
        end_date = jsonData["end_date"]

        projectIdExists:bool = checkExDB.project_id(p_id)
        projectnameExists:bool = checkExDB.project_name(projectname)
        startDateValid = dateValidator.validate_datetime(start_date)
        endDateValid = dateValidator.validate_datetime(end_date)

        incorrectList = []

        if projectIdExists:
            incorrectList.append("Project with this Id exists already.")
        if projectnameExists:
            incorrectList.append("Project with this Name exists already.")
        if startDateValid:
            incorrectList.append("Start date invalid format")
        if endDateValid:
            incorrectList.append("End date invalid format")

        if not projectIdExists and not projectnameExists and not startDateValid and not endDateValid:
            return {
                "valid":True,
                "errors": incorrectList
            }
        else:
            return {
                "valid":False,
                "errors": incorrectList
            }

    def employee(jsonData:json)->bool:
        emp_id = jsonData["emp_id"]
        email = jsonData["email"]
        phone = jsonData["phone"]

        employeeIdExists:bool = checkExDB.employee_id(emp_id)
        emailExists:bool = checkExDB.project_name(email)
        phoneExists:bool = dateValidator.validate_datetime(phone)

        incorrectList = []

        if employeeIdExists:
            incorrectList.append("Employee with this Id exists already. ")
        if emailExists:
            incorrectList.append("Employee with this Name exists already. ")
        if phone:
            incorrectList.append("An Employee is already using this phonenumber. ")

        if not employeeIdExists and not emailExists and not phoneExists:
            return {
                "valid":True,
                "errors": incorrectList
            }
        else:
            return {
                "valid":False,
                "errors": incorrectList
            }
