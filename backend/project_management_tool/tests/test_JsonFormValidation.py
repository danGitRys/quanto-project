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