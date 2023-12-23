import json
import jsonschema
from jsonschema import validate

class formValidator:

    def team(jsonData:json)->bool:
        """Validating if the given json matches the
        required teamSchema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
        teamSchema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "info": {"type": "string"},
               
               
            },
            # Specify required keys
            "required": ["name","info"],
        }
        try:
            validate(instance=jsonData, schema=teamSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def login(jsonData:json)->bool:
        """Validating if the given json matches the
        required loginSchema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
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
    
    def assignment(jsonData:json)->bool:
        """Validating if the given json matches the
        required Assignment Schema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
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
    
    def employee(jsonData:json)->bool:
        """Validating if the given json matches the
        required Employee Schema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
        employeeSchema = {
            "type": "object",
            "properties": {
                "emp_id": {"type": "string"},
                "forename": {"type": "string"},
                "surname": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "fk_team_id":{"type":"integer"},
                "team_role": {"type": "string"},
            },
            # Specify required keys
            "required": ["emp_id","forename","surname","email","phone","fk_team_id","team_role"],
        }
        try:
            validate(instance=jsonData, schema=employeeSchema)
        except jsonschema.exceptions.ValidationError as err:
           
            return False
        return True
    
    def booking(jsonData:json)->bool:
        """Validating if the given json matches the
        required bookingSchema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
        bookingSchema = {
            "type": "object",
            "properties": {
                "fk_employee": {"type": "integer"},
                "fk_position": {"type": "integer"},
                "start": {"type": "string"},
                "end": {"type": "string"},
                "pause":{"type":"string"},
                "time": {"type": "string"},
            },
            # Specify required keys
            "required": ["fk_employee","fk_position","start","end","pause"],
        }
        try:
            validate(instance=jsonData, schema=bookingSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def forecast(jsonData:json)->bool:
        """Validating if the given json matches the
        required forecast Schema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
        forecastSchema = {
            "type": "object",
            "properties": {
                "fk_employee": {"type": "integer"},
                "fk_position": {"type": "integer"},
                "start": {"type": "string"},
                "end": {"type": "string"},
                "info": {"type": "string"},
                
               
            },
            # Specify required keys
            "required": ["fk_employee","fk_position","start","end","info"],
        }
        try:
            validate(instance=jsonData, schema=forecastSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def project(jsonData:json)->bool:
        """Validating if the given json matches the
        required Project Schema

        Parameters
        ----------
        jsonData : json
            json to be validated

        Returns
        -------
        bool
            Result if the json matches the Schema
        """
        projectSchema = {
            "type": "object",
            "properties": {
                "p_id": {"type": "string"},
                "projectname": {"type": "string"},
                "customername": {"type": "string"},
                "start_date": {"type": "string"},
                "end_date": {"type": "string"},
                "fk_creator": {"type": "integer"},
                "creation_date": {"type": "string"},
                
               
            },
            # Specify required keys
            "required": ["p_id","projectname","customername","start_date","end_date","fk_creator","creation_date"],
        }
        try:
            validate(instance=jsonData, schema=projectSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
    
    def position(jsonData:json)->bool:
       
        positionSchema = {
            "type": "object",
            "properties": {
                "position_id": {"type": "string"},
                "fk_project": {"type": "integer"},
                "rate": {"type": "integer"},
                "wd": {"type": "integer"},
                "start_date": {"type": "string"},
                "end_date": {"type": "string"},
            },
            # Specify required keys
            "required": ["position_id","fk_project","rate","start_date","end_date"],
        }
        try:
            validate(instance=jsonData, schema=positionSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True
    
