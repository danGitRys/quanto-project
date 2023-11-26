from .jsonFormValidator import *
from .jsonContentValidation import *

class validator:

    def team(jsondata):

        if(formValidator.team(jsondata)):
            print("Form passt")
            if(jsonContentValidator.team(jsondata)):
                print("Inhalt passt")
                return True

            else:
                return False
        else:
            return False