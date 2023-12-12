from django.test import TestCase
from ..middleware.validation.mailValidation import MailValidator
class MailFormClass(TestCase):

    def test_validMailV1(self):
        result = MailValidator.validate_mail("test@gmail.de")
        self.assertEqual(result,True)
    
    def test_validMailV2(self):
        result = MailValidator.validate_mail("test1223@gmail.de")
        self.assertEqual(result, True)
        
    def test_validMailV3(self):
        result = MailValidator.validate_mail("test@gmail123.de")
        self.assertEqual(result, True)
    
    def test_validMail_Fail_V1(self):
        result = MailValidator.validate_mail("test@gmail")
        self.assertEqual(result,False)
    
    def test_validMail_Fail_V2(self):
        result = MailValidator.validate_mail("test.de")
        self.assertEqual(result,False)
        
        