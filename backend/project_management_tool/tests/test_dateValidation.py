from ..middleware.validation.dateValidator import dateValidator
from django.test import TestCase

class DateTestClass(TestCase):

    def test_date_valid(self):
        result = dateValidator.validate_date("2002-12-12")
        self.assertEqual(result,True)
    
    def test_date_Fail(self):
        result = dateValidator.validate_date("2002-13-12")
        self.assertEqual(result,False)


    def test_date_Fail_V2(self):
        result = dateValidator.validate_date("2002-12-122")
        self.assertEqual(result,False)
    
    def test_date_Fail_V3(self):
        result = dateValidator.validate_date("21.11.2012")
        self.assertEqual(result,False)
             
    
    def test_datetime_valid(self):
        result = dateValidator.validate_datetime("2002-12-12 12:12:12")
        self.assertEqual(result,True)
    
    def test_datetime_Fail(self):
        result = dateValidator.validate_datetime("2002-12-12 12:70:12")
        self.assertEqual(result,False)
    
    def test_datetime_Fail_V2(self):
        result = dateValidator.validate_datetime("2002-12-12 25:10:12")
        self.assertEqual(result,False)
    
    def test_datetime_Fail_V3(self):
        result = dateValidator.validate_datetime("2002-12-12 25:10")
        self.assertEqual(result,False)

    def test_datetime_Fail_V4(self):
        result = dateValidator.validate_datetime("2022-12-01 25")
        self.assertEqual(result,False)
        
    def test_datetime_Fail_V5(self):
        result = dateValidator.validate_datetime("2022-12-01 25:")
        self.assertEqual(result,False)
        
    def test_datetime_Fail_V6(self):
        result = dateValidator.validate_datetime("2022-12-01 23:0")
        self.assertEqual(result,False)
        
    def test_date_Fail_V7(self):
        result = dateValidator.validate_date("21.11.2012")
        self.assertEqual(result, False)