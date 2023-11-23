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
    
    def assignment(jsonData):
        assignmentSchema = {
            "type": "object",
            "properties": {
                "fk_project": {"type": "integer"},
                "fk_employee": {"type": "integer"},
                "role": {"type": "string"},
               
               
            },
            # Specify required keys
            "required": ["fk_project","fk_employee","role"],
        }
        try:
            validate(instance=jsonData, schema=assignmentSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def employee(jsonData):
        employeeSchema = {
            "type": "object",
            "properties": {
                "emp_id": {"type": "string"},
                "forename": {"type": "string"},
                "surname": {"type": "string"},
                "mail": {"type": "string"},
                "phone": {"type": "string"},
                "fk_team_id":{"type":"integer"},
                "team_roll": {"type": "string"},
                
               
               
            },
            # Specify required keys
            "required": ["emp_id"],
        }
        try:
            validate(instance=jsonData, schema=employeeSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def booking(jsonData):
        bookingSchema = {
            "type": "object",
            "properties": {
                "fk_employee": {"type": "string"},
                "fk_position": {"type": "string"},
                "surname": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"},
                "pause":{"type":"integer"},
                "time": {"type": "string"},
                
               
               
            },
            # Specify required keys
            "required": ["fk_employee"],
        }
        try:
            validate(instance=jsonData, schema=bookingSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def forecast(jsonData):
        forecastSchema = {
            "type": "object",
            "properties": {
                "fk_employee": {"type": "string"},
                "fk_position": {"type": "string"},
                "surname": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"},
                "info": {"type": "string"},
                
               
            },
            # Specify required keys
            "required": ["fk_employee"],
        }
        try:
            validate(instance=jsonData, schema=forecastSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def project(jsonData):
        projectSchema = {
            "type": "object",
            "properties": {
                "p_id": {"type": "string"},
                "name": {"type": "string"},
                "company": {"type": "string"},
                "start_date": {"type": "string"},
                "end_date": {"type": "string"},
                "fk_creator": {"type": "integer"},
                "creation_date": {"type": "string"},
                
               
            },
            # Specify required keys
            "required": ["p_id"],
        }
        try:
            validate(instance=jsonData, schema=projectSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
