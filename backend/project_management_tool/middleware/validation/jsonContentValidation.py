from .checkExistenceDb import *
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
