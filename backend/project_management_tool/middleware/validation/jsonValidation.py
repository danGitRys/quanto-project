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