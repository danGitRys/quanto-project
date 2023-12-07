from .jsonFormValidator import *
from .jsonContentValidation import *
import json

class validator:

    def team(jsondata:json)->bool:
        """Validating if the Form and the Content
        matches the requirements

        Parameters
        ----------
        jsondata : json
            Json to be validated

        Returns
        -------
        bool
            Json valid or not
        """

        if(formValidator.team(jsondata)):
            print("Form passt")
            if(jsonContentValidator.team(jsondata)):
                print("Inhalt passt")
                return True

            else:
                return False
        else:
            return False
    
    def assignment(jsondata:json)->bool:
        if(formValidator.assignment(jsondata)):
          

            contentResult = jsonContentValidator.assignment(jsondata)
            contentValid = contentResult["valid"]
            contentError = contentResult["errors"]
            if contentValid:
                return {
                    "valid":True,
                    "errors":contentError
                }
            else:
                return {
                    "valid":False,
                    "errors":contentError
                }
        else:
            return  {
                    "valid":False,
                    "errors":["Invalid Json Form"]
                }
    
    def booking(jsondata:json)->bool:
        if(formValidator.booking(jsondata)):
          

            contentResult = jsonContentValidator.booking(jsondata)
            contentValid = contentResult["valid"]
            contentError = contentResult["errors"]
            if contentValid:
                return {
                    "valid":True,
                    "errors":contentError
                }
            else:
                return {
                    "valid":False,
                    "errors":contentError
                }
        else:
            return  {
                    "valid":False,
                    "errors":["Invalid Json Form"]
                }
    
    def position(jsondata:json)->json:
        if(formValidator.position(jsondata)):
            contentResult = jsonContentValidator.postion(jsondata)
            print(contentResult)
            contentValid = contentResult["valid"]
            contentError = contentResult["errors"]
            print("Form apsst")
            if contentValid:
                return {
                    "valid":True,
                    "errors":contentError
                }
            else:
                return {
                    "valid":False,
                    "errors":contentError
                }
        else:
            return  {
                    "valid":False,
                    "errors":["Invalid Json Form"]
                }