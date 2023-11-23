import json
import jsonschema
from jsonschema import validate

class validator:

    def team(jsonData):
        teamSchema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "info": {"type": "string"},
               
               
            },
            # Specify required keys
            "required": ["name"],
        }
        try:
            validate(instance=jsonData, schema=teamSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def login(jsonData):
        loginSchema = {
            "type": "object",
            "properties": {
                "token": {"type": "string"},
               
               
            },
            # Specify required keys
            "required": ["token"],
        }
        try:
            validate(instance=jsonData, schema=loginSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
