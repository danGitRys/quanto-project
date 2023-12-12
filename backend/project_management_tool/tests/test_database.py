from ..middleware.validation.dateValidator import dateValidator
from ..models import *
from django.test import TestCase

class DateTestClass(TestCase):

    def test_First(self):
        testObject = Team.objects.create(name="Test",info="Test")
        testObject.save()
        result:bool = Team.objects.filter(name="Test").exists()
        self.assertEqual(True,result)

    
        