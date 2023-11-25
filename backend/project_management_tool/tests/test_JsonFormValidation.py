from ..middleware import *

from django.test import TestCase
class JsonFormClass(TestCase):

    def test_validateTeamJson(self):
        testJson = {
                    "name":"test2",
                    "info":"test2"
                    }
        
        validationResult = jsonValidator.validator.team(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateTeamJsonFail(self):
        testJson = {
                    "name":"test2",
                    "infoTest":"test2"
                    }
        
        validationResult = jsonValidator.validator.team(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateTeamJsonFailV2(self):
        testJson = {
                    "name":"test2",
                    "info":1
                    }
        
        validationResult = jsonValidator.validator.team(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateTeamJsonFailV3(self):
        testJson = {
                    "name":1,
                    "info":"test"
                    }
        
        validationResult = jsonValidator.validator.team(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateLoginJson(self):
        testJson = {
                    "token":"test2"
                    
                    }
        
        validationResult = jsonValidator.validator.login(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateLoginJsonFail(self):
        testJson = {
                    "toker":"test2"
                    
                    }
        
        validationResult = jsonValidator.validator.login(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateLoginJsonFail(self):
        testJson = {
                    "toker":1
                    
                    }
        
        validationResult = jsonValidator.validator.login(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateAssignmentJson(self):
        testJson = {
                    "fk_project": 1,
                    "fk_employee": 2,
                    "role": "Admin",
                    
                    }
        
        validationResult = jsonValidator.validator.assignment(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateAssignmentJsonFail(self):
        testJson = {
                    "fk_project": "String",
                    "fk_employee": 2,
                    "role": "Admin",
                    
                    }
        
        validationResult = jsonValidator.validator.assignment(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateAssignmentJsonFailV2(self):
        testJson = {
                    "fk_project": 2,
                    "fk_employee": 2,
                    
                    
                    }
        
        validationResult = jsonValidator.validator.assignment(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateEmployeeJson(self):
        testJson = {
                    "emp_id": "db3",
                "forename": "Franz",
                "surname": "Dieter",
                "mail": "franz@dieter",
                "phone": "122323",
                "fk_team_id":2,
                "team_roll":"Member"
                    
                    }
        
        validationResult = jsonValidator.validator.employee(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateEmployeeJsonFailV1(self):
        testJson = {
                    "emp_id": "db3",
                "forename": "Franz",
                "surname": "Dieter",
                "mail": "franz@dieter",
                "phone": "122323",
                "fk_team_id":"2",
                "team_roll":"Member"
                    
                    }
        
        validationResult = jsonValidator.validator.employee(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateEmployeeJsonFailV2(self):
        testJson = {
                    "emp_id": "db3",
                "forename": "Franz",
                "surname": "Dieter",
                "mail": "franz@dieter",
                "phone": "122323",
                "fk_team_id":"2",
                
                    
                    }
        
        validationResult = jsonValidator.validator.employee(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateBookingJson(self):
        testJson = {
                   "fk_employee": 1,
                    "fk_position": 2,
                    "start": "start",
                    "end": "ende",
                    "pause":"pause",
                    "time": "zeit",
                    
                    }
        
        validationResult = jsonValidator.validator.booking(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateBookingJsonV2(self):
        testJson = {
                   "fk_employee": 1,
                    "fk_position": 2,
                    "start": "start",
                    "end": "ende",
                    "pause":"pause",
                   
                    
                    }
        
        validationResult = jsonValidator.validator.booking(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateBookingJsonFailV1(self):
        testJson = {
                   "fk_employee": 1,
                    "fk_position": 2,
                    "start": "start",
                    "end": "ende",
                    "pause":"pause",
                    "time": 2,
                    
                    }
        
        validationResult = jsonValidator.validator.booking(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateBookingJsonFailV2(self):
        testJson = {
                   "fk_employee": 1,
                    "fk_position": 2,
                    "start": "start",
                   
                    "pause":"pause",
                    "time": "zeit",
                    
                    }
        
        validationResult = jsonValidator.validator.booking(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateForecastJson(self):
        testJson = {
                  "fk_employee": 2,
                "fk_position": 2,
                "start": "2323",
                "end": "2323",
                "info": "3223",
                    
                    }
        
        validationResult = jsonValidator.validator.forecast(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateForecastJsonFailV1(self):
        testJson = {
                  "fk_employee": 2,
                "fk_positioner": 2,
                "start": "2323",
                "end": "2323",
                "info": "3223",
                    
                    }
        
        validationResult = jsonValidator.validator.forecast(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateForecastJsonFailV1(self):
        testJson = {
                  "fk_employee": "2",
                "fk_positioner": 2,
                "start": "2323",
                "end": "2323",
                "info": "3223",
                    
                    }
        
        validationResult = jsonValidator.validator.forecast(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateProjectJson(self):
        testJson = {
                  "p_id": "p1",
                "name": "mercedes",
                "company": "mercedes",
                "start_date": "start",
                "end_date": "start",
                "fk_creator": 1,
                "creation_date": "today",
                    
                    }
        
        validationResult = jsonValidator.validator.project(testJson)
        self.assertEqual(validationResult,True)
    
    def test_validateProjectJsonFailV1(self):
        testJson = {
                  "p_id": 1,
                "name": "mercedes",
                "company": "mercedes",
                "start_date": "start",
                "end_date": "start",
                "fk_creator": 1,
                "creation_date": "today",
                    
                    }
        
        validationResult = jsonValidator.validator.project(testJson)
        self.assertEqual(validationResult,False)
    
    def test_validateProjectJsonFailV2(self):
        testJson = {
                  "p_id": 1,
                "name": "mercedes",
                "company": "mercedes",
                
                "end_date": "start",
                "fk_creator": 1,
                "creation_date": "today",
                    
                    }
        
        validationResult = jsonValidator.validator.project(testJson)
        self.assertEqual(validationResult,False)
    
