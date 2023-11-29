from ...models import *
from .checkExistenceDb import *
from .enumValidation import *
class jsonUpdateConentValidation:

    def assignment(jsonData,assignmentId:int):
        keys = jsonData.keys()
        validDict = {"fk_projectValid":None,"fk_employeeValid":None,"roleValid":None,"combinationWillExist":None}
        for key in keys:
            print(key)
            print("------------")
            if key == "fk_project":
                fk_projectValid:bool = checkExDB.project_id(jsonData["fk_project"])
                validDict["fk_projectValid"] = fk_projectValid
            elif key == "fk_employee":
                fk_employeeValid:bool = checkExDB.employee_id(jsonData["fk_employee"])
                validDict["fk_employeeValid"] = fk_employeeValid
            elif key == "role":
                roleValid:bool = enumValidation.assignementRole(jsonData["role"])
                validDict["roleValid"] = roleValid
         

        print(validDict)
        print(validDict.values())

        if not True in validDict.values():
            return {
                "successfull":False,
                "error": "No Valid Database Matches: " + validDict
            }
        else:
            print("One True")
            filtered_dict = {key: value for key, value in validDict.items() if value is True}
            print(filtered_dict)
            #TODO Find solution to check every case
            #Idee Merge the new Values with the old values and insert this in the select statement
            
            


