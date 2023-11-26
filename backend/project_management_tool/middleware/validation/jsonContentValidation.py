from .checkExistenceDb import *
class jsonContentValidator:

    def team(jsonData):
        name = jsonData["name"]
        nameValid:bool = checkExDB.team(name)
        
        return not nameValid
